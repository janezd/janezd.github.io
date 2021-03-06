import os
import re
import struct
from collections import defaultdict
import unicodedata
from urllib.request import urlopen
import markdown

site_title = "Vidra - Računalništvo brez računalnika"
static_files = ("o_strani.md", "sorodne_strani.md")
photos_url = "http://dajmi.fri.uni-lj.si/vidra/slike/"


def parse_images(md):
    def get_image_size(fname):
        with urlopen(fname) as fhandle:
            size = 2
            ftype = 0
            while not 0xc0 <= ftype <= 0xcf:
                fhandle.read(size)
                byte = fhandle.read(1)
                while ord(byte) == 0xff:
                    byte = fhandle.read(1)
                ftype = ord(byte)
                size = struct.unpack('>H', fhandle.read(2))[0] - 2
            fhandle.read(1)
            return struct.unpack('>HH', fhandle.read(4))

    if not os.path.exists("thumbs"):
        return "", ""
    images = [x for x in os.listdir("thumbs")
              if os.path.splitext(x)[1] == ".jpg"]
    order = md.Meta.get("slike") or []
    ordered = []
    for img in " ".join(order).split():
        for i, img1 in enumerate(images):
            if os.path.splitext(img1)[0].endswith(img):
                ordered.append(images.pop(i))
                break
        else:
            print(images)
            raise ValueError("Image {} does not exist".format(img))
    images = ordered + images
    img_thumbs = '<div class="thumbs">{}</div>'.format("\n".join(
        '<img src="thumbs/{}" onclick="openGallery({})"/>'.format(img, i)
        for i, img in enumerate(images)))
    sizes = (get_image_size(photos_url + img) for img in images)
    img_list = use_template(
        gallery,
        list="\n".join("    {{src: '{}{}', w: {}, h: {}}},".
                       format(photos_url, img, w, h) for img, (h, w) in zip(images, sizes))
    )
    return img_thumbs, img_list


class ActLinks(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        el = markdown.util.etree.Element("a")
        act = m.group(2)
        if "|" in act:
            link, el.text = act.split("|")
        else:
            link = el.text = act
        el.text = el.text.strip()
        link = no_carets(link).lower()
        if not os.path.exists(os.path.join("..", link, "index.md")):
            print("Warning: missing internal link from {} to {}".
                format(os.path.split(os.getcwd())[-1], link))
        el.set("href", "../" + link)
        return el


class ActLinkExtension(markdown.extensions.Extension):
    def extendMarkdown(self, md, md_globals):
        ACTIVITY_LINK_RE = r"\(\(([^\)]+)\)\)"
        activitylinkPattern = ActLinks(ACTIVITY_LINK_RE)
        md.inlinePatterns.add('activity_link', activitylinkPattern,
            "<not_strong")


def parse_section(files):
    if not files:
        return ""
    s = ""
    line = '<p><a href="{}">{}</a></p>\n'
    for fname in files:
        if fname.startswith("http"):
            s += line.format(*fname.split(" ", 1))
        elif fname: 
            if not os.path.exists(fname):
                print("Warning: missing file {}/{}".
                    format(os.path.split(os.getcwd())[-1], fname))
            s += line.format(fname, os.path.splitext(fname)[0])
    return s


def insert_section(template, id, heading, content):
	if content:
		content = "<h2>{}</h2>{}".format(heading, content)
	return template.replace("{{{{{}}}}}".format(id), content)


def no_carets(s):
    s = unicodedata.normalize("NFD", s)
    s = s.strip().replace(chr(780), "").replace(" ", "-")
    return s


def use_template(template, **kwargs):
    return re.sub(r"\{\{(.*?)\}\}", lambda x: kwargs[x.group(1)], template)


def build_page():
    md = markdown.Markdown(extensions=["markdown.extensions.meta",
                                       ActLinkExtension()])
    main = md.convert(open("index.md").read())
    meta = defaultdict(str)
    meta.update(md.Meta)

    img_thumbs, img_list = parse_images(md)            
    duration = ("<b>Trajanje</b>: " + md.Meta.get("trajanje")[0]
                if "trajanje" in md.Meta else "")
    title = md.Meta.get("naslov")[0]
    summary = " ".join(md.Meta.get("povzetek"))
    html = tpl
    for id, heading, meta in (
            ("plan", "Potek učne ure", "priprava"),
            ("material", "Učni listi in druge datoteke", "datoteke"),
            ("resources", "Viri", "viri"), ("source", "Vir", "vir"),
            ("video", "Video posnetki", "video"),
            ("links", "Povezave", "povezave")):
        html = insert_section(
            html, id, heading, parse_section(md.Meta.get(meta)))
    html = use_template(html, **locals())
    html = use_template(base, body=html, title="Vidra - " + title)
    open("index.html", "wt").write(html)
    return title, summary


base_dir = os.getcwd()
tpl = open("scripts/page.tpl").read()
base = open("scripts/base.tpl").read()
gallery = open("scripts/gallery.tpl").read()
base_root = base.replace("../", "")
static = base_root.replace('<div id="body">',
                           '<div id="body" class="no-sidebox">')

for fname in static_files:
    body = markdown.markdown(open(fname).read())
    mo_title = re.search("<h1>(.*?)</h1>", body)
    title = mo_title and ("Vidra - " + mo_title.group(1)) or site_title
    html = use_template(static, **locals())
    open(os.path.splitext(fname)[0] + ".html", "w").write(html)

all_pages = []
for act in open("scripts/list.txt"):
    try:
        act = act.strip()
        dir = no_carets(act.lower())
        os.chdir(dir)
        title, summary = build_page()
        all_pages.append((dir, title, summary))
    except Exception as err:
        print("Error while parsing {}:\n{}".format(act, err))
    finally:
        os.chdir(base_dir)


entries = ['<div class="toc"><a href="{0}" class="thumbnail"><img src="{0}/thumbnail.png"/></a>'
           '<div class="desc"><a href="{0}"><h2>{1}</h2><p>{2}</p></a></div></div>'.
           format(dir, title, summary)
           for dir, title, summary in all_pages]
tocdivs = "\n".join('<div id="col{}">{{}}</div>'.format(i) for i in "12")
mid = (len(entries) + 1)// 2
entries = tocdivs.format("\n".join(entries[:mid]),
                         "\n".join(entries[mid::]))
toc = use_template(base_root, body=entries, title=site_title)
open("index.html", "wt").write(toc)

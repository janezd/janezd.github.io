import os
import re
import shutil
from collections import defaultdict
import unicodedata
import markdown

static_files = ("vidra.css", "o_strani.txt", "sorodne_strani.txt", "favicon.ico")

def parse_section(files, dir, outdir):
    if not files:
        return ""
    s = ""
    line = '<p><a href="{}">{}</a></p>\n'
    for fname in files:
        if fname.startswith("http"):
            s += line.format(*fname.split(" ", 1))
        elif fname: 
            shutil.copyfile(os.path.join(dir, fname), os.path.join(outdir, fname))
            s += line.format(fname, os.path.splitext(fname)[0])
    return s

def insert_section(template, id, heading, content):
	if content:
		content = "<h2>{}</h2>{}".format(heading, content)
	return template.replace("{{{{{}}}}}".format(id), content)

def no_carets(s):
    s = unicodedata.normalize("NFD", dir)
    s = s.replace(chr(780), "").replace(" ", "-")
    return s

def build_page(dir):
    new_dir = no_carets(dir)
    outdir = os.path.join(base_out, new_dir)
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    shutil.copyfile(os.path.join(dir, "thumbnail.png"),
                    os.path.join(outdir, "thumbnail.png"))
    md = markdown.Markdown(extensions=["markdown.extensions.meta"])
    main_html = md.convert(open(os.path.join(dir, "main.txt")).read())
    meta = defaultdict(str)
    meta.update(md.Meta)

    html = tpl.replace("{{main}}", main_html)
    if "trajanje" in md.Meta:
        duration = "<b>Trajanje</b>: " + md.Meta.get("trajanje")[0]
    else:
        duration = ""
    html = html.replace("{{duration}}", duration)
    title = md.Meta.get("naslov")[0]
    summary  = " ".join(md.Meta.get("povzetek"))
    html = html.replace("{{title}}", title)
    html = html.replace("{{summary}}", summary)
    for id, heading, meta in (
            ("plan", "Potek učne ure", "priprava"),
            ("material", "Učni listi in druge datoteke", "datoteke"),
            ("resources", "Viri", "viri"), ("source", "Vir", "vir"),
            ("video", "Video posnetki", "video"),
            ("links", "Povezave", "povezave")):
        html = insert_section(html, id, heading,
                              parse_section(md.Meta.get(meta), dir, outdir))

    html = base.replace("{{body}}", html)
    open(os.path.join(outdir, "main.html"), "wt").write(html)
    return new_dir, title, summary


tpl = open("page.tpl").read()
base = open("base.tpl").read()
base_root = base.replace("../", "")
static = base_root.replace('<div id="body">',
                           '<div id="body" class="no-sidebox">')
os.chdir("..")

base_out = os.path.expanduser("~/Desktop/vidra")
if not os.path.exists(base_out):
    os.mkdir(base_out)

for fname in static_files:
    shutil.copyfile(fname, os.path.join(base_out, fname))
for fname in static_files:
    mode = "tb"[os.path.splitext(fname)[1] in (".ico",)]
    contents = open(fname, "r" + mode).read()
    if os.path.splitext(fname)[1] == ".txt":
        contents = markdown.markdown(contents)
        fname = fname[:-3] + "html"
    if os.path.splitext(fname)[1] == ".html":
        contents = static.replace("{{body}}", contents)
    open(os.path.join(base_out, fname), "w" + mode).write(contents)

all_pages = []
for dir in sorted(os.listdir(".")):
    if os.path.exists(os.path.join(dir, "main.txt")):
        try:
            new_dir, title, summary = build_page(dir)
            all_pages.append((new_dir, title, summary))
        except Exception as err:
            print("Error while parsing {}:\n{}".format(dir, err))


entries = ['<div class="toc"><a href="{0}/main.html" class="thumbnail"><img src="{0}/thumbnail.png"/></a>'
           '<div class="desc"><a href="{0}/main.html"><h2>{1}</h2><p>{2}</p></a></div></div>'.
           format(dir, title, summary)
           for dir, title, summary in all_pages]
tocdivs = "\n".join('<div id="col{}">{{}}</div>'.format(i) for i in "12")
entries = tocdivs.format("\n".join(entries[:(len(entries) + 1)// 2]),
                         "\n".join(entries[len(entries) // 2:]))
open(os.path.join(base_out, "index.html"), "wt").write(base_root.replace("{{body}}", entries))
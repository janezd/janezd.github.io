import os
import re
import shutil
from collections import defaultdict
import unicodedata
import webbrowser
import markdown

site_title = "Vidra - Računalništvo brez računalnika"
static_files = ("vidra.css", "o_strani.txt", "sorodne_strani.txt", "favicon.ico", "CNAME")

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

def use_template(template, **kwargs):
    return re.sub(r"\{\{(.*?)\}\}", lambda x: kwargs[x.group(1)], template)

def build_page(dir):
    new_dir = no_carets(dir)[3:].lower()
    outdir = os.path.join(base_out, new_dir)
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    shutil.copyfile(os.path.join(dir, "thumbnail.png"),
                    os.path.join(outdir, "thumbnail.png"))
    md = markdown.Markdown(extensions=["markdown.extensions.meta"])
    main = md.convert(open(os.path.join(dir, "main.txt")).read())
    meta = defaultdict(str)
    meta.update(md.Meta)

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
        html = insert_section(html, id, heading,
                              parse_section(md.Meta.get(meta), dir, outdir))
    html = use_template(html, **locals())
    html = use_template(base, body=html, title="Vidra - " + title)
    open(os.path.join(outdir, "index.html"), "wt").write(html)
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
        mo_title = re.search("<h1>(.*?)</h1>", contents)
        title = mo_title and ("Vidra - " + mo_title.group(1)) or site_title
        contents = use_template(static, body=contents, title=title)
    open(os.path.join(base_out, fname), "w" + mode).write(contents)

all_pages = []
for dir in sorted(os.listdir(".")):
    if os.path.exists(os.path.join(dir, "main.txt")):
        try:
            new_dir, title, summary = build_page(dir)
            all_pages.append((new_dir, title, summary))
        except Exception as err:
            print("Error while parsing {}:\n{}".format(dir, err))


entries = ['<div class="toc"><a href="{0}" class="thumbnail"><img src="{0}/thumbnail.png"/></a>'
           '<div class="desc"><a href="{0}"><h2>{1}</h2><p>{2}</p></a></div></div>'.
           format(dir, title, summary)
           for dir, title, summary in all_pages]
tocdivs = "\n".join('<div id="col{}">{{}}</div>'.format(i) for i in "12")
mid = (len(entries) + 1)// 2
entries = tocdivs.format("\n".join(entries[:mid]),
                         "\n".join(entries[mid::]))
toc = use_template(base_root, body=entries, title=site_title)
index = os.path.join(base_out, "index.html")
open(index, "wt").write(toc)

import http.server
import socketserver
os.chdir(base_out)
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", 8000), Handler)
webbrowser.open_new_tab("http://127.0.0.1:8000")
httpd.serve_forever()

import os
import re
import shutil
from collections import defaultdict
import markdown

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

def build_page(dir):
    outdir = os.path.join(base_out, dir)
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    md = markdown.Markdown(extensions=["markdown.extensions.meta"])
    main_html = md.convert(open(os.path.join(dir, "main.txt")).read())
    html = tpl.replace("{{main}}", main_html)

    meta = defaultdict(str)
    meta.update(md.Meta)

    thumb = os.path.join(dir, "thumbnail.png")
    if os.path.exists(thumb):
        shutil.copyfile(thumb, os.path.join(outdir, "thumbnail.png"))
        thumb = '<img id="thumb" src="thumbnail.png"/>'
    else:
        thumb = ''
    html = html.replace("{{thumbnail}}", thumb)

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

    open(os.path.join(outdir, "main.html"), "wt").write(html)
    return title, summary


tpl = open("page.tpl").read()
toc = open("toc.tpl").read()
os.chdir("..")

base_out = os.path.expanduser("~/Desktop/vidra")
if not os.path.exists(base_out):
    os.mkdir(base_out)
shutil.copyfile("vidra.css", os.path.join(base_out, "vidra.css"))

all_pages = []
for dir in sorted(os.listdir(".")):
    if os.path.exists(os.path.join(dir, "main.txt")):
        title, summary = build_page(dir)
        all_pages.append((dir, title, summary))

entries = "\n".join('<tr><th><a href="{0}/main.html"><img src="{0}/thumbnail.png"/></a></th>'
                    '<td><a href="{0}/main.html"><h2>{1}</h2><p>{2}</p></a></td></tr>'.
                    format(dir, title, summary)
                    for dir, title, summary in all_pages)
open(os.path.join(base_out, "index.html"), "wt").write(toc.replace("{{entries}}", entries))
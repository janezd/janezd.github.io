import os
import re
import shutil
from collections import defaultdict
import markdown

static_files = ("vidra.css", )

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
    return title, summary


tpl = open("page.tpl").read()
base = open("base.tpl").read()
base_root = base.replace("../", "")
os.chdir("..")

base_out = os.path.expanduser("~/Desktop/vidra")
if not os.path.exists(base_out):
    os.mkdir(base_out)

for fname in static_files:
    shutil.copyfile(fname, os.path.join(base_out, fname))
for fname in os.listdir("."):
    if os.path.splitext(fname)[1] == ".html":
        contents = open(fname).read()
        contents = base_root.replace("{{body}}", contents)
        open(os.path.join(base_out, fname), "wt").write(contents)

all_pages = []
for dir in sorted(os.listdir(".")):
    if os.path.exists(os.path.join(dir, "main.txt")):
        try:
            title, summary = build_page(dir)
            all_pages.append((dir, title, summary))
        except Exception as err:
            print("Error while parsing {}:\n{}".format(dir, err))


entries = ['<tr><th><a href="{0}/main.html"><img src="{0}/thumbnail.png"/></a></th>'
           '<td><a href="{0}/main.html"><h2>{1}</h2><p>{2}</p></a></td></tr>'.
           format(dir, title, summary)
           for dir, title, summary in all_pages]
tocdivs = "\n".join(
    '<div id="col{}"><table class="toc">{{}}</table></div>'.format(i) for i in "12")
entries = tocdivs.format("\n".join(entries[:(len(entries) + 1)// 2]),
                         "\n".join(entries[len(entries) // 2:]))
entries = '<div id="body">\n{}\n<div class="clear"></div>\n</div>'.format(entries)
open(os.path.join(base_out, "index.html"), "wt").write(base_root.replace("{{body}}", entries))
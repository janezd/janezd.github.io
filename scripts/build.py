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


tpl = open("page.tpl").read()
os.chdir("..")

base_out = os.path.expanduser("~/Desktop/vidra")
if not os.path.exists(base_out):
    os.mkdir(base_out)

shutil.copyfile("vidra.css", os.path.join(base_out, "vidra.css"))

for dir in os.listdir("."):
    main = os.path.join(dir, "main.txt")
    if not os.path.exists(main):
        continue

    outdir = os.path.join(base_out, dir)
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    md = markdown.Markdown(extensions=["markdown.extensions.meta"])
    main_html = md.convert(open(main).read())
    html = tpl.replace("{{main}}", main_html)

    meta = defaultdict(str)
    meta.update(md.Meta)

    thumb = os.path.join(dir, "thumbnail.png")
    if os.path.exists(thumb):
        shutil.copyfile(thumb, os.path.join(outdir, "thumbnail.png"))
        html = html.replace("{{thumbnail}}",
                            '<img id="thumb" src="thumbnail.png"/>')
    else:
        html = html.replace("{{thumbnail}}", '')
    html = insert_section(html, "plan", "Potek učne ure",
                          parse_section(md.Meta.get("priprava"), dir, outdir))
    if "trajanje" in md.Meta:
        duration = "<b>Trajanje</b>: " + md.Meta.get("trajanje")[0]
    else:
        duration = ""
    html = html.replace("{{duration}}", duration)

    html = insert_section(html, "material", "Učni listi in druge datoteke",
    	                  parse_section(md.Meta.get("datoteke"), dir, outdir))

    html = insert_section(html, "resources", "Viri",
                          parse_section(md.Meta.get("viri"), dir, outdir))

    html = insert_section(html, "source", "Vir",
                          parse_section(md.Meta.get("vir"), dir, outdir))

    html = insert_section(html, "video", "Video posnetki",
                          parse_section(md.Meta.get("video"), dir, outdir))

    html = insert_section(html, "links", "Povezave",
                          parse_section(md.Meta.get("povezave"), dir, outdir))

    open(os.path.join(outdir, "main.html"), "wt").write(html)

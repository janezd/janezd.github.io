import os
import re
import shutil
import markdown

sections = [("Potek učne ure", "P"),
            ("Učni listi in druge datoteke", "U")]

def parse_section(dir, code, outdir, prefix):
    section = []
    for fname in os.listdir(dir):
        mo = re.match(code + "(?P<nr>\\d\\d) (?P<wholename>(?P<name>.*)\.\w+)", fname)
        if mo:
            newname = prefix + mo.group("wholename")
            section.append(mo.group("nr", "name") + (newname,))
            shutil.copyfile(os.path.join(dir, fname),
                            os.path.join(outdir, newname))
    return "\n".join('<p><a href="{2}">{1}</a></p>'.format(*x)
	                 for x in sorted(section))

def insert_section(template, id, heading, content):
	if content:
		content = "<h2>{}</h2>{}".format(heading, content)
	return template.replace("{{{{{}}}}}".format(id), content)


tpl = open("page.tpl").read()
os.chdir("..")

if not os.path.exists("web"):
    os.mkdir("web")

for dir in os.listdir("."):
    main = os.path.join(dir, "main.txt")
    if not os.path.exists(main):
        continue

    outdir = os.path.join("web", dir)
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    md = markdown.Markdown(extensions=["markdown.extensions.meta"])
    main_html = md.convert(open(main).read())
    html = tpl.replace("{{main}}", main_html)

    prefix = "A" + dir[:2]
    html = insert_section(html, "plan",
    	                  "Potek učne ure",
                          parse_section(dir, "P", outdir, prefix))
    if "trajanje" in md.Meta:
        duration = "<b>Trajanje</b>: " + md.Meta["trajanje"][0]
    else:
        duration = ""
    html = html.replace("{{duration}}", duration)

    html = insert_section(html, "material",
    	                  "Učni listi in druge datoteke",
    	                  parse_section(dir, "U", outdir, prefix))
    open(os.path.join(outdir, "main.html"), "wt").write(html)

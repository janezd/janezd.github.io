import os
import re
import markdown

sections = [("Potek učne ure", "P"),
            ("Učni listi in druge datoteke", "U")]

def parse_section(dir, code):
	section = []
	for fname in os.listdir(dir):
		mo = re.match(code + "(\\d\\d) ((.*)\.\w+)", fname)
		if mo:
			section.append(mo.groups())
	return "\n".join('<p><a href="{1}">{2}</a></p>'.format(*x)
	                 for x in sorted(section))

def insert_section(template, id, heading, content):
	if content:
		content = "<h2>{}</h2>{}".format(heading, content)
	return template.replace("{{{{{}}}}}".format(id), content)


tpl = open("page.tpl").read()
os.chdir("..")

for dir in os.listdir("."):
    main = os.path.join(dir, "main.txt")
    if not os.path.exists(main):
        continue
    md = markdown.Markdown(extensions=["markdown.extensions.meta"])
    main_html = md.convert(open(main).read())
    html = tpl.replace("{{main}}", main_html)

    html = insert_section(html, "plan",
    	                  "Potek učne ure", parse_section(dir, "P"))
    if "trajanje" in md.Meta:
        duration = "<b>Trajanje</b>: " + md.Meta["trajanje"][0]
    else:
        duration = ""
    html = html.replace("{{duration}}", duration)

    html = insert_section(html, "material",
    	                  "Učni listi in druge datoteke",
    	                  parse_section(dir, "U"))
    open(os.path.join(dir, "main.html"), "wt").write(html)

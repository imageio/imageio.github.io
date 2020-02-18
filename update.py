""" Update the index.html with the content from our README.md
"""

import os
from urllib.request import urlopen

project = "imageio"

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

readme_url = "https://raw.githubusercontent.com/%s/%s/master/README.md"
readme_url = readme_url % (project, project)
index_filename = os.path.join(THIS_DIR, "index.html")

# Get sources
html = open(index_filename, "rb").read().decode("utf-8")
readme = urlopen(readme_url).read().decode("utf-8")

# Get interesting part from readme
content = readme.split("-- DIVIDER --")[1].split("\n", 1)[1]

# Inject in html
needle1 = "<section id='content'>"
needle2 = "</section>"
i0 = html.index(needle1) + len(needle1)
i1 = html.index(needle2, i0)
new_html = html[:i0] + "\n\n" + content + "\n\n" + html[i1:]

# Write back
open(index_filename, "wb").write(new_html.encode("utf-8"))

print("index.html is updated. Commit and push to apply.")

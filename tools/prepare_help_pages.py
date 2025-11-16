"""Create help pages to translate.

Reads the ../docs/index.md file entries, and creates the listed pages.
"""
import re
from string import Template

translations = {
    'Project home page': 'Project home page',
}

page_template = '''[$Home_translated]($Novelibre_home) > $Heading

---

# $Heading

---

$Footer

'''

help_dir = '../docs'
page_link_pattern = re.compile(r'\[(.*?)\]\((.*?)\)')
with open(f'{help_dir}/index.md', 'r', encoding='utf-8') as f:
    text = f.read()

page_data = page_link_pattern.findall(text)
for title, file_name in page_data:
    if 'https:' in file_name:
        continue

    text = Template(page_template).safe_substitute(
        {
            'Home_translated': translations['Project home page'],
            'Novelibre_home': 'https://github.com/peter88213/novelibre',
            'Heading':title,
            'Footer': '[English manual](https://peter88213.github.io/nvhelp-en/)'
        }
    )
    with open(f'{help_dir}/{file_name}', 'w', encoding='utf_8') as f:
        f.write(text)


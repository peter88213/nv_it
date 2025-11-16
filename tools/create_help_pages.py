"""Create help pages to translate.

Reads the ../docs/index.md file entries, and creates the listed pages.

"""
import os
import re

help_dir = '../docs'
page_pattern = re.compile(r'\[(.*?)\]\((.*?)\)')

with open(f'{help_dir}/index.md', 'r', encoding='utf-8') as f:
    text = f.read()

page_data = page_pattern.findall(text)
for title, file_name in page_data:
    if 'https:' in file_name:
        continue

    page_name, __ = os.path.splitext(file_name)
    with open(f'{help_dir}/{file_name}', 'w', encoding='utf_8') as f:
        f.write(
            f'[Help index](index.md) > {title}'
            '\n\n---\n\n'
            f'# {title}\n\n'
            '\n\n---\n\n'
            f'[English page](https://peter88213.github.io/nvhelp-en/{page_name}.html)'
        )

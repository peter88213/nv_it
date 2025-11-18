"""Create help pages to translate.

Reads the ../docs/index.md file entries, and creates the listed pages.
"""
import json
import os
import re
from my_template import MyTemplate

help_dir = '../docs/help'
index_page = f'{help_dir}/index.md'
json_dict = '../dictionary/msg_dict.json'
page_link_pattern = re.compile(r'- \[(.*?)\]\((.*?)\)')
page_template = '''[novelibre ${Home page}](https://github.com/peter88213/novelibre) > [Index](../) > [${Online help}](./) > $Heading

---

# $Heading

---

[English manual](https://peter88213.github.io/nvhelp-en/)


Copyright (c) 2025 by Peter Triesberger. All rights reserved.

'''


def translate_special_terms():
    with open(json_dict, 'r', encoding='utf-8') as f:
        dictionary = json.load(f)
    for page_name in os.listdir(help_dir):
        if not page_name.endswith('.md'):
            continue

        page_path = f'{help_dir}/{page_name}'
        print(f'Translating "{page_path}"...')
        with open(page_path, 'r', encoding='utf-8') as f:
            text = f.read()
        text = MyTemplate(text).substitute(dictionary)
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(text)


def create_missing_pages(skip=True):
    print(f'Reading "{index_page}"...')
    with open(index_page, 'r', encoding='utf-8') as f:
        text = f.read()

    page_data = page_link_pattern.findall(text)
    for title, file_name in page_data:
        file_path = f'{help_dir}/{file_name}'
        if 'https:' in file_name:
            continue

        if skip and os.path.isfile(file_path):
            print(f'Skipping "{file_path}"')
            continue

        text = MyTemplate(page_template).safe_substitute(
            {
                'Heading':title,
            }
        )
        print(f'Writing "{file_path}"...')
        with open(file_path, 'w', encoding='utf_8') as f:
            f.write(text)


def main():
    create_missing_pages()
    translate_special_terms()
    print('Done.')


if __name__ == '__main__':
    main()

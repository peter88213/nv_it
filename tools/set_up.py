"""Set up translations for the novelibre language pack.

- Generate the language specific '*.po' dictionaries for novelibre and its plugins.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_it
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os

from settings import *
import translations


def output(message):
    print(f'(set_up) {message}')


def main():
    output(f'Set up novelibre translation files for {languageName}.')

    translationsComplete = True
    for moduleName in os.listdir('../modules'):
        poPath = f'../modules/{moduleName}'
        if not os.path.isdir(poPath):
            continue

        try:
            version = translations.main(
                f'{poPath}/messages.pot',
                f'{poPath}/{languageCode}.po',
                f'../dictionary/msg_dict.json',
            )
            print(version)
        except UserWarning:
            translationsComplete = False
    return translationsComplete


if __name__ == '__main__':
    main()

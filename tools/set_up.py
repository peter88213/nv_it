"""Set up translations for the novelibre language pack.

- Generate the language specific '*.po' dictionaries for novelibre and its plugins.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_xx
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
from settings import *
import translations


def main():
    print(f'Set up novelibre translation files for {languageName}.')

    translationsComplete = True
    for programName in os.listdir('../programs'):
        poPath = f'../programs/{programName}'
        if not translations.main(poPath, app=programName, json=True):
            translationsComplete = False
    return translationsComplete


if __name__ == '__main__':
    main()

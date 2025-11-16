"""Build a novelibre language pack.

- Generate the language specific '*.mo' dictionaries for novelibre and its plugins.
- Create a self-extracting Python archive for distribution.
- Create an optional zipfile.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_it
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
from shutil import copy2
import zipapp
import zipfile

import msgfmt
import set_up
from settings import *


def main():
    print(f'Build a novelibre language pack for {languageName}.')

    # Check whether tranlsations are complete.
    if not set_up.main():
        print('PROGRAM ABORTED. Please complete translations.')
        return False

    # Create the target path.
    localePath = f'locale/{languageCode}/LC_MESSAGES'
    os.makedirs(f'../build/{localePath}', exist_ok=True)
    moFiles = []

    # Create binary message catalogs.
    for programName in os.listdir('../modules'):
        print(programName)
        poPath = f'../modules/{programName}/{languageCode}.po'
        moName = f'{programName}.mo'
        moPath = f'../build/{localePath}/{moName}'
        print(f'Writing "{moPath}" ...')
        msgfmt.make(poPath, moPath)
        moFiles.append(f'{localePath}/{moName}')

    # Create the release package.
    copy2('../src/setuplib.py', '../build')
    distPath = f'../nv_{languageCode}.pyz'
    print(f'Writing "{distPath}" ...')
    zipapp.create_archive('../build', target=distPath, main='setuplib:main', compressed=True)

    # Create the optional zip file.
    copy2('../src/setup.py', '../build')
    zipPath = f'../nv_{languageCode}.zip'
    print(f'Writing "{zipPath}" ...')
    with zipfile.ZipFile(zipPath, 'w') as release:
        os.chdir('../build')
        for file in moFiles:
            release.write(file, compress_type=zipfile.ZIP_DEFLATED)
        release.write('setuplib.py', compress_type=zipfile.ZIP_DEFLATED)
        release.write('setup.py', compress_type=zipfile.ZIP_DEFLATED)

    print('Done.')
    return True


if __name__ == '__main__':
    main()

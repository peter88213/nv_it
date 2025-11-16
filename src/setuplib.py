"""Language pack installer library module. 

Version @release

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_it
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
from pathlib import Path
from shutil import copytree
import sys
import zipfile

PLUGIN = 'nv_it'

pyz = os.path.dirname(__file__)


def extract_tree(sourceDir, targetDir):
    with zipfile.ZipFile(pyz) as z:
        for file in z.namelist():
            if file.startswith(f'{sourceDir}/'):
                z.extract(file, targetDir)


def cp_tree(sourceDir, targetDir):
    copytree(sourceDir, f'{targetDir}/{sourceDir}', dirs_exist_ok=True)


def install(zipped):
    if zipped:
        copy_tree = extract_tree
    else:
        copy_tree = cp_tree

    scriptPath = os.path.abspath(sys.argv[0])
    scriptDir = os.path.dirname(scriptPath)
    os.chdir(scriptDir)

    print(f'*** Installing {PLUGIN} ***')
    homePath = str(Path.home()).replace('\\', '/')
    applicationDir = f'{homePath}/.novx'
    if os.path.isdir(applicationDir):

        # Install the localization files.
        print('Copying locale ...')
        copy_tree('locale', applicationDir)

        # Show a success message.
        print(
            f'\nSucessfully installed {PLUGIN} '
            f'at "{os.path.normpath(applicationDir)}".'
        )
    else:
        print(
            'ERROR: Cannot find a novelibre installation '
            f'at "{os.path.normpath(applicationDir)}".'
        )

    input('Press ENTER to quit.')


def main(zipped=True):
    try:
        install(zipped)
    except Exception as ex:
        print(str(ex))
        input('Press ENTER to quit.')


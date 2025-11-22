"""Language pack installer library module. 

Version @release

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_it
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import locale
import os
from pathlib import Path
from shutil import copy2
from shutil import copytree
import sys
import zipfile
from tkinter import messagebox

PLUGIN = 'nv_it.py'
VERSION = '@release'

pyz = os.path.dirname(__file__)


def check_locale():
    try:
        CURRENT_LANGUAGE = locale.getlocale()[0][:2]
    except:
        # Fallback for old Windows versions.
        CURRENT_LANGUAGE = locale.getdefaultlocale()[0][:2]
    languageCode = PLUGIN[3:].replace('.py', '')
    if CURRENT_LANGUAGE != languageCode:
        messagebox.showwarning(
            title=f'{PLUGIN.replace(".py", "")} installation warning',
            message='The installed translations will not be applied.',
            detail=f'The system language is not "{languageCode}".',
        )


def extract_file(sourceFile, targetDir):
    with zipfile.ZipFile(pyz) as z:
        z.extract(sourceFile, targetDir)


def extract_tree(sourceDir, targetDir):
    with zipfile.ZipFile(pyz) as z:
        for file in z.namelist():
            if file.startswith(f'{sourceDir}/'):
                z.extract(file, targetDir)


def cp_tree(sourceDir, targetDir):
    copytree(sourceDir, f'{targetDir}/{sourceDir}', dirs_exist_ok=True)


def install(zipped):
    if zipped:
        copy_file = extract_file
        copy_tree = extract_tree
    else:
        copy_file = copy2
        copy_tree = cp_tree

    scriptPath = os.path.abspath(sys.argv[0])
    scriptDir = os.path.dirname(scriptPath)
    os.chdir(scriptDir)

    print(f'*** Installing {PLUGIN} {VERSION} ***\n')
    homePath = str(Path.home()).replace('\\', '/')
    applicationDir = f'{homePath}/.novx'
    if os.path.isdir(applicationDir):
        pluginDir = f'{applicationDir}/plugin'
        os.makedirs(pluginDir, exist_ok=True)

        # Install the plugin.
        print(f'Copying "{PLUGIN}" ...')
        copy_file(PLUGIN, pluginDir)

        # Install the localization files.
        print('Copying locale ...')
        copy_tree('locale', applicationDir)

        # Show a success message.
        print(
            f'\nSucessfully installed {PLUGIN} '
            f'at "{os.path.normpath(applicationDir)}".'
        )
        check_locale()
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


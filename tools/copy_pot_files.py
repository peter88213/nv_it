"""Copy the "messages.pot" files from the local novelibre and plugin directories.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_it
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import glob
import os
from shutil import copyfile
from settings import languageCode

ROOT_DIR = '../..'

os.chdir(ROOT_DIR)
programs = ['novelibre']
for plugin in glob.iglob('nv_*', recursive=False):
    programs.append(plugin)
for program in programs:
    potFile = f'{program}/i18n/messages.pot'
    if os.path.isfile(potFile):
        targetPath = f'nv_{languageCode}/programs/{program}'
        os.makedirs(targetPath, exist_ok=True)
        copyfile(potFile, f'{targetPath}/messages.pot')
        print(program)
print('Done.')

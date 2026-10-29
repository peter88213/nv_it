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


def copy_module_pot(module, targetPath):
    potFile = f'{module}/i18n/messages.pot'
    if os.path.isfile(potFile):
        os.makedirs(targetPath, exist_ok=True)
        copyfile(potFile, f'{targetPath}/messages.pot')
        print(module)


os.chdir(ROOT_DIR)
module = 'novelibre'
copy_module_pot(module, f'nv_{languageCode}/modules/{module}')
for plugin in glob.iglob('nv_*', recursive=False):
    copy_module_pot(plugin, f'nv_{languageCode}/plugins/{plugin}')
print('Done.')

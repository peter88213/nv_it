"""Build the nv_it novelibre plugin package.
        
Note: VERSION must be updated manually before starting this script.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_it
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
from shutil import copy2
import sys

import msgfmt
from package_builder import PackageBuilder
import set_up
from settings import *

sys.path.insert(0, f'{os.getcwd()}/../../novelibre/tools')

VERSION = '5.42.0'
LANGUAGE_CODE = 'it'


def output(message):
    print(f'(package_builder) {message}')


class PluginBuilder(PackageBuilder):

    PRJ_NAME = 'nv_it'

    def build_script(self):
        os.makedirs(self.testDir, exist_ok=True)
        copy2(self.sourceFile, self.testFile)
        self.insert_version_number(self.testFile, version=self.version)

    def build_translation(self):
        """Generate the language files for the distribution."""
        output('Creating/updating the translations ...')
        # Check whether translations are complete.
        if not set_up.main():
            output('PROGRAM ABORTED. Please complete translations.')
            return False

        # Create the target path.
        localePath = f'locale/{LANGUAGE_CODE}/LC_MESSAGES'
        moDir = f'{self.testDir}/{localePath}'
        os.makedirs(moDir, exist_ok=True)

        # Create binary message catalogs.
        for moduleName in os.listdir('../modules'):
            if not os.path.isdir(f'../modules/{moduleName}'):
                continue

            output(f'Module: "{moduleName}".')
            poPath = f'../modules/{moduleName}/{LANGUAGE_CODE}.po'
            moName = f'{moduleName}.mo'
            moPath = f'{moDir}/{moName}'
            output(f'Writing "{moPath}" ...')
            msgfmt.make(poPath, moPath)
            self.distFiles.append(
                (moPath, f'{self.buildDir}/{localePath}')
            )


def main():
    pb = PluginBuilder(VERSION)
    pb.run()


if __name__ == '__main__':
    main()

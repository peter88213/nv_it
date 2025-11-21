"""Italian language package plugin for novelibre.

Requires Python 3.7+
Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_plugin
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""
import os
import shutil
import sys

LANGUAGE_CODE = 'it'
TRANSLATIONS_DIR = f'{os.path.dirname(sys.argv[0])}/locale/{LANGUAGE_CODE}'


class Plugin:
    """Template plugin class."""
    VERSION = '@release'
    API_VERSION = '5.43'
    DESCRIPTION = 'Italian language package'
    URL = 'https://github.com/peter88213/nv_it'

    def install(self, model, view, controller):
        pass

    def uninstall(self):
        shutil.rmtree(TRANSLATIONS_DIR, ignore_errors=True)

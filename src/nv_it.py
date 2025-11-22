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
import locale
import os
import shutil
import sys

LANGUAGE_CODE = 'it'
TRANSLATIONS_DIR = f'{os.path.dirname(sys.argv[0])}/locale/{LANGUAGE_CODE}'


class Plugin:
    """Language package plugin class."""
    VERSION = '@release'
    API_VERSION = '5.43'
    DESCRIPTION = 'Italian language package'
    URL = 'https://github.com/peter88213/nv_it'

    def install(self, model, view, controller):
        if not os.path.isdir(TRANSLATIONS_DIR):
            raise UserWarning(
                'Translations not found:'
                f'"{os.path.normpath(TRANSLATIONS_DIR)}".'
            )
        try:
            CURRENT_LANGUAGE = locale.getlocale()[0][:2]
        except:
            # Fallback for old Windows versions.
            CURRENT_LANGUAGE = locale.getdefaultlocale()[0][:2]
        if CURRENT_LANGUAGE != LANGUAGE_CODE:
            view.show_warning(
                title=self.DESCRIPTION,
                message='Cannot apply translations.',
                detail=f'The system language is not "{LANGUAGE_CODE}".',
            )

    def uninstall(self):
        shutil.rmtree(TRANSLATIONS_DIR, ignore_errors=True)

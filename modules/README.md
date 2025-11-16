This directory contains sub-directories for novelibre and each plugin to be translated.

### How to add a plugin translation

1. Move the plugin's folder containing `messages.pot` from `../plugins` here.
2. Run the `../tools/set_up.py` script. This will create an `it.po` file and automatically enter all known translations.
3. Edit `it.po` and add the missing translations.
4. Re-run the `../tools/set_up.py` script. This will add the new translations to the central dictionary. 
5. If you are finished with translating, run the `../tools/build_release.py` script.
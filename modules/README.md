This directory contains sub-directories for novelibre and each plugin to be translated.

### How to add a plugin

1. Move the plugin's folder containing `messages.pot` from `../plugins` here.
2. Run the `../tools/set_up.py` script. This will create a `<your_language>.po` file and automatically enter all known translations.
3. Edit `<your_language>.po` and add the missing translations.
4. Re-run the `../tools/set_up.py` script. This will add the new translations to the central dictionary. 
5. If you are finished with translating, run the `../tools/build_release.py` script.
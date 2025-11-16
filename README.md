# nv_xx

Language pack for [novelibre](https://github.com/peter88213/novelibre/).

---

## How to install the language pack

## Download and install

### Default: Executable Python zip archive

Download the installation package [nv_xx.pyz](https://github.com/peter88213/nv_xx/raw/main/nv_xx.pyz)

- Launch *nv_xx.pyz* by double-clicking (Windows desktop),
- or execute `python nv_xx.pyz` (Windows), resp. `python3 nv_xx.pyz` (Linux) on the command line.

> [!IMPORTANT]
> Many web browsers recognize the download as an executable file and offer to open it immediately. 
> This starts the installation under Windows.
> 
> However, depending on your security settings, your browser may 
> initially  refuse  to download the executable file. 
> In this case, your confirmation or an additional action is required. 
> If this is not possible, you have the option of downloading 
> the zip file. 


### Alternative: Zip file

The package is also available in zip format: [nv_xx.zip](https://github.com/peter88213/nv_xx/raw/main/nv_xx.zip)

- Extract the content of the downloaded zipfile "nv_xx.zip" into an empty folder.
- Move into this folder and launch *setup.py* by double-clicking (Windows/Linux desktop), 
- or execute `python setup.py` (Windows), resp. `python3 setup.py` (Linux) on the command line.

---

## How to create/update the language pack

1. Check/edit the entries in the `tools/settings.py` file.
1. Make sure you have got a recent `messages.pot` file for each program.
2. Run the `tools/set_up.py` script to create or update the `xx.po` message catalogs.
3. Edit the `xx.po` message catalogs in the `programs` subfolders.
4. Run the `tools/build_release.py` script to create the zipfile for distribution.


### Editing a message catalog

A "message catalog" is a dictionary for the program's messages and menu entries. The file name is `xx.po`.

Be sure to use a text editor that writes utf-8 encoded text. Otherwise, it may not work with non-ASCII characters used in your language.

The  `xx.po` dictionary is organized as a set of *message ID (msgid)* - *message string (msgstr)* pairs, where *msgid* means the English term, and *msgstr* means the translated term. This is an example for such a pair where the message string is still missing:

```
msgid "Cannot overwrite file"
msgstr ""
```

Just enter all missing message strings. 
- If a message ID contains placeholders like `{}`, be sure to put them also into the message string.  
- If a message ID starts with `!`, the message string must also start with `!`. 


### Advertising a new/updated language pack

You may want to put a posting in the [novelibre forum](https://github.com/peter88213/novelibre/discussions).

---

## License

This is Open Source software, and *nv_xx* is licenced under GPLv3. See the
[GNU General Public License website](https://www.gnu.org/licenses/gpl-3.0.en.html) for more
details, or consult the [LICENSE](https://github.com/peter88213/nv_progress/blob/main/LICENSE) file.


This directory contains helper scripts for building the language package. 

- `copy_pot_files.py` updates the `message.pot` files of all plugins 
  whose sources are installed locally in `../..`.
- `set_up.py` creates `it.po` files for each module included in `../modules` and synchronizes 
  all translations with the central dictionary `../dictionary/msg_dict.json`.
- `build_release.py` builds the installation packages `../nv_it.pyz` and `../nv_it.zip`. 
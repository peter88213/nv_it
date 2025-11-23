novelibre [Pagina principale](https://github.com/peter88213/novelibre) > [Pagine italiane](../../) > [Aiuto in linea](../) > nv_snapshots

---

# nv_snapshots

**User guide**

This page refers to the latest
[nv_snapshots](https://github.com/peter88213/nv_snapshots/) release. You
can open it with **Aiuto > ${Snapshots Online help}** or `F1`.

The plugin adds a **Snapshots** entry to the *novelibre* **Strumenti** menu,
a **Snapshot** entry to the **File** menu, and a 
**Snapshots Online help** entry to the **Aiuto** menu.

## General

A snapshot is a compressed, titled, and commented version of a *.novx*
file. *nv_snapshots* creates such snapshots on demand and stores them in
a subdirectory of the project folder. This subdirectory is named
*"Snapshots"* and is created automatically if required. Saving a
snapshot is manually triggered via `Ctrl`-`Alt`-`S` or the 
**File > ${Snapshot}** menu command.

Use the **Strumenti > ${Snapshots}** menu command to start the 
**snapshot manager**. The snapshot manager displays the snapshots of the currently
open project in list form. You can select individual snapshots and
export documents from them. LibreOffice/OpenOffice has a document
comparison function that allows you to find and edit the differences
between the snapshot and the current project. You can also easily revert
to any snapshot.

## How to compare the current state of your project with a snapshot

If you do not want to return to a previous state of your project, but
want to undo individual changes since a snapshot was created, you can do
this conveniently using the document comparison function of
LibreOffice/OpenOffice.

1.  Select the desired snapshot in the snapshot manager and export a
    document that you want to compare (e.g. the manuscript).
2.  Export a document of the same kind from the current project and open
    it.
3.  Select **Edit - Track Changes - Compare Document\...**
    (LibreOffice), or **${Edit} > ${Compare Document}** (OpenOffice).
4.  A file selection dialog opens. Select the "snapshot document" and
    click **Insert**.

LibreOffice/OpenOffice combines both documents into the current
document. All text passages that occur in the current project but not in
the snapshot are identified as having been inserted, and all text
passages that got deleted since the snapshot has been created are
identified as deletions.

You can now accept or reject the insertions and deletions. At the end
you may reimport the updated document in *novelibre* in order to
transfer the revised state to the project.

------------------------------------------------------------------------

## Command reference

### *novelibre* main menu entries

#### File > ${Snapshot}

Creates a snapshot as a zip file in the *"Snapshots"* subdirectory of
the current project folder. A dialog for entering a title and a
description will pop up.

##### Ok

Confirm the entry and create the snapshot.

##### Aiuto in linea

Go to this help page.

##### Cancella

Close the dialog without creating a snapshot.


> **Hint**
> 
> If you leave the entry fields empty, the snapshot is given the title
> "Undefined" and can only be identified by its creation date.


-   If there are unsaved changes in the project, you will be prompted to
    save them.
-   If there is already an up-to-date snapshot, no further snapshot will
    be created.

#### Strumenti > ${Snapshots}

Opens the snapshot manager window. It contains the list of snapshots and
a display field for the title and description of the selected snapshot.
The functions of the snapshot manager are accessed via the menu
described below.

#### Aiuto > ${Snapshots Online help}

Starts the system web browser with this page.

------------------------------------------------------------------------

### The snapshot manager menu

#### File > ${Open Snapshot folder}

Opens the current project's snapshot folder with the file manager.

#### File > ${Clean up Snapshot folder}

Deletes ODF documents, XML data files, and document backups in the snapshot folder.

#### File > ${Snapshot}

Creates a snapshot (see above).

#### File > Rimuovi

Deletes the selected snapshot.

#### File > ${Revert}

Overwrites the current project file with the version of the selected
snapshot and reloads the project in *novelibre*. A snapshot of the
current project file is created automatically beforehand.

#### File > Chiudi

Closes the snapshot manager window.

------------------------------------------------------------------------

#### Esporta > Manoscritto

This allows you to create a text document that is split into sections.
File name suffix is `_manuscript_tmp`.

#### Esporta > Descrizione Parte

This allows you to create a text document that contains a **very brief synopsis** with part headings and part descriptions. 
File name suffix is `_parts_tmp`.

#### Esporta > Descrizione del Capitolo

This allows you to create a text document that contains a **brief synopsis** with part/chapter headings and chapter descriptions. 
File name suffix is `_chapters_tmp`.

#### Esporta > Descrizione della sezione

This allows you to create a text document with a **full synopsis** containing part/chapter headings and section descriptions. 
File name suffix is `_sections_tmp`.

#### Esporta > Struttura narrativa

This allows you to create a text document that contains all stages, each with description. 
File name suffix is `_structure_tmp`.

#### Esporta > ${Plot line descriptions}

This allows you to create a text document that contains stages, plot lines, and plot points, each with description. 
File name suffix is
`_plotlines_tmp`.

#### Esporta > Griglia della trame

This allows you to create a spreadsheet. 
File name suffix is `_grid_tmp`.

#### Esporta > Descrizione personaggio

This allows you to create a text document that contains character
descriptions, bio, goals, and notes. File name suffix is
`_characters_tmp`.

#### Esporta > Descrizione Località

This allows you to create a text document that contains location
descriptions. File name suffix is `_locations_tmp`.

#### Esporta > Descrizione oggetto

This allows you to create a text document that contains item
descriptions. File name suffix is `_items_tmp`.

#### Esporta > Files dati XML

This allows you to create a set of XML files containing the project's
characters, locations, items, and plot lines with all their properties.
You can use these files to transfer the corresponding elements
individually or in groups from the snapshot to the current project.

------------------------------------------------------------------------

#### Aiuto > Aiuto in linea

Starts the system web browser with this page.

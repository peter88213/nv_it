[novelibre Pagina principale](https://github.com/peter88213/novelibre) > [Pagine in italiano](../) > [Aiuto online](./) > Capitolo menu

---

# Capitolo menu

**Chapter/part operation**

## Aggiungi capitolo

**Add a new chapter**

With **Capitolo > Aggiungi capitolo** you can add a chapter to the tree.

-   The new chapter is placed at the next free position after the
    selection, if possible.
-   Otherwise, the new chapter is placed at the end of the "Libro"
    branch.
-   The new chapter has an auto-generated title. You can change it in
    the right pane.

> **Hint**
> 
> To automatically name the new chapter and, if necessary, place it above
> the "Trash Bin," subsequently press `F5`.

## Aggiungi parte

**Add a new part**

With **Capitolo > Aggiungi parte** you can add a part to the tree.

-   The new part is placed at the next free position on the chapter
    level after the selection, if possible.
-   Otherwise, the new part is placed at the last position on the
    chapter level.
-   The new part has an auto-generated title. You can change it in the
    right pane.

## Aggiungi capitoli multipli...

**Add new chapters in bulk**

With **Capitolo > Aggiungi capitoli multipli...** you can add up to 20
chapters to the tree.

-   You will be prompted to enter the number of new chapters.
-   The number of chapters to be added at once is limited to 20.
-   The new chapters are placed at the next free position after the
    selection, if possible.
-   Otherwise, the new chapters are placed at the end of the "Libro"
    branch.

> **Hint**
> 
> To automatically name the new chapters and, if necessary, place them
> above the "Trash Bin," subsequently press `F5`.

## Imposta tipo

**Set the type of the selected chapters**

With **Capitolo > Imposta tipo** you can set the
type of the selected chapter to *Normale* or *Non usato* .

> **Note**
> 
> Setting the type of a chapter to *Non usato* will also make its sections
> *Non usato*.

## Cambia livello

**Change the level of the selected chapters**

With **Capitolo > Cambia livello** you can turn chapters into parts and
vice versa.

-   **1º Livello** converts the selected chapters into parts.
-   **2º Livello** converts the selected parts into chapters.


## Assegna colore...

**Assign a color to all selected chapters and parts**

With **Capitolo > Assegna colore...**
you can assign a color to all chapters and parts in a single or multiple selection.
A color picker dialog opens.
If you cancel the color choosing process, the color of the selected chapters and parts remain unchanged.


## Annulla colore

**Reset the colors of all selected chapters and parts**

With **Capitolo > Annulla colore**
you can clear the color assignments for all chapters and parts in a single or multiple selection.

---

## Sposta i capitoli selezionati in un nuovo progetto

**Split one book in two**

With **Capitolo > Sposta i capitoli selezionati in un nuovo progetto** you can create
a new project containing the moved chapters/sections and all related
elements and plot lines/plot points. The selected chapters are removed
from the current project and pasted into an auto-generated project whose
file path you define with a file selection dialog. All relationships of
the moved sections are retained.

## Esporta descrizioni capitolo per la modifica

**Export an ODT document that can be imported again after editing**

With **Capitolo > Esporta descrizioni capitolo per la modifica** you can
create a text document that contains a **brief synopsis** with
part/chapter headings and chapter descriptions that can be edited and
reimported. File name suffix is `_chapters_tmp`.

-  Only "normal" parts and chapters are exported.
   Parts and chapters marked "Unused" are not exported.
-  Parts and chapters can neither be rearranged nor deleted.
-  With *Writer*, you can create parts and chapters by inserting headings
   within the description area:

   -  *Heading 1* → New part title.
   -  *Heading 2* → New chapter title.

   > **Important** 
   > Documents with new parts or chapters are automatically
   > discarded after the *novelibre* project is updated.


## Esporta descrizioni parte per la modifica

**Export an ODT document that can be imported again after editing**

With **Capitolo > Esporta descrizioni parte per la modifica** you can create a
text document that contains a **very brief synopsis** with part headings
and part descriptions. File name suffix is `_parts_tmp`.

-  Parts can neither be rearranged nor deleted.
-  With *Writer*, you can create parts and chapters by inserting headings
   within the description area:

   -  *Heading 1* → New part title.
   -  *Heading 2* → New chapter title.

   > **Important** 
   > Documents with new parts or chapters are automatically
   > discarded after the *novelibre* project is updated.

## Esporta tabella capitoli

**Export an ODS document that can be imported again after editing**

With **Capitolo > Esporta tabella capitoli** you can create a spreadsheet
that contains a row per chapter. The document can be edited with *Calc*
and reimported. File name suffix is `_chapterlist_tmp`.

> **Note**
> 
> You can reorder, hide or delete columns and rows without affecting the
> reimport. Only the first column and the first row, which are hidden by
> default, must not be changed as they contain the structural information
> for the import.
>   
> You can add chapters to the project by inserting rows
> containing at least the new chapter's name. 
> The hidden ID cell must be left empty.

## Esporta tabella parti

**Export an ODS document that can be imported again after editing**

With **Capitolo > Esporta tabella parti** you can create a spreadsheet that
contains a row per part. File name suffix is `_partlist_tmp`.

> **Note**
> 
> You can reorder, hide or delete columns and rows without affecting the
> reimport. Only the first column and the first row, which are hidden by
> default, must not be changed as they contain the structural information
> for the import.
>  
> You can add parts to the project by inserting rows
> containing at least the new part's name. 
> The hidden ID cell must be left empty.

---

## ${Show chapter board in browser}

**Show an HTML report with section cards arranged by chapters**

With **Capitolo > ${Show chapter board in browser}** you can create a HTML file
that contains a board with "index cards" for the chapters and all used sections.
The index cards contain the title and the description of the corresponding element.
The chapter cards are arranged in the first column.
Each chapter card opens a row containing the cards of the assigned sections.

> **Note**
> 
> The report is a temporary file, auto-deleted on program exit. If needed,
> you can have your web browser save or print it.


---

[English manual](https://peter88213.github.io/nvhelp-en/)


Copyright (c) by Peter Triesberger. All rights reserved.

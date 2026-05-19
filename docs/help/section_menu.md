[novelibre Pagina principale](https://github.com/peter88213/novelibre) > [Pagine in italiano](../) > [Aiuto online](./) > Sezione menu

---

# Sezione menu

**Section operation**

## Aggiungi

**Add a new section**

With **Sezione > Aggiungi**, you can add a section to the tree.

-   The new section is placed at the next free position after the
    selection, if possible.
-   Otherwise, no new section is generated.
-   The new section has an auto-generated title. You can change it in
    the right pane.

### Properties of a new section:

-   *Normal* type
-   *Outline* completion status
-   No viewpoint character assigned
-   No plot line or tag assigned
-   No date/time set

## Aggiungi sezioni multiple...

**Add new sections in bulk**

With **Sezione > Aggiungi sezioni multiple...**, you can add up to 20
sections to the tree.

-   You will be prompted to enter the number of new sections.
-   The number of sections to be added at once is limited to 20.
-   The new sections are placed at the next free position after the
    selection, if possible.
-   Otherwise, no new section is generated.


## Clona

With **Sezione > Clona**,
you can create a copy of the selected section.

- The clone is inserted behind the selected section in the project tree.
- The type of the cloned section is "unused".
- The cloned section has all the properties and assignments of the original,
  except for plot point assignments.


---

## Imposta tipo

**Set the type of the selected section**

With **Sezione > Imposta tipo**, you can set the type of the selected
section to *Normale* or *Non usato* .

> **Hint**
> 
> Type change for multiple sections:
> 
> -   Either select multiple sections, or
> -   select a chapter.

## Imposta stato

**Set the section completion status**

With **Sezione > Imposta stato**, you can set the completion status 
of the selected section to 
*Struttura*, *Bozza*, *1ª Revisione*, *2ª Revisione*, or *Fatto*.

> **Hint**
> 
> Status change for multiple sections:
> 
> -   Either select multiple sections, or
> -   select a parent node (Capitolo or Libro)

## Imposta punto di vista...

**Assign a viewpoint character to the section**

With **Sezione > Imposta punto di vista...**, you open a pop-up window with a
dropdown list containing all characters in the tree view's sort order.
Click on the character you want to assign as viewpoint character. If you
click on the topmost entry (the blank one) of the list, this will clear
the viewpoint association.

> **Hint**
> 
> Select a parent node to set the viewpoint for all subordinate sections.


## ${Assign color...}

**Assign a color to all selected sections**

With **Sezione > ${Assign color...}**
you can assign a color to all sections in a single or multiple selection.
A color picker dialog opens.
If you cancel the color choosing process, the color of the selected sections remain unchanged.


## Annulla colore

**Reset the colors of all selected sections**

With **Sezione > Annulla colore**
you can clear the color assignments for all sections in a single or multiple selection.


---

## Esporta descrizioni sezione per la modifica

**Export an ODT document that can be imported again after editing**

With **Sezione > Esporta descrizioni sezione per la modifica**, you can
create a text document with a **full synopsis** containing part/chapter
headings and section descriptions that can be edited and reimported.
File name suffix is `_sections_tmp`.

-  Only "normal" chapters and sections are exported.
   Chapters and sections marked "Unused" are not exported.
-  Section titles are invisible, but appear in the *Navigator*.
-  Chapters and sections can neither be rearranged nor deleted.
-  With *Writer*, you can create sections by inserting headings
   within the description area:

   -  *Heading 1* → New part title.
   -  *Heading 2* → New chapter title.
   -  *Heading 3* → New section title.
   -  *Heading 4* → New appended section title.

   > **Important** 
   > Documents with new sections are automatically
   > discarded after the *novelibre* project is updated.

---

## Tabella sezioni (solo esportazione)

**Export an ODS document**

With **Sezione > Tabella sezioni (solo esportazione)**, you can create a
spreadsheet with a row per section, containing the following data:

-   Section ID (hidden)
-   Section number (link to manuscript)
-   Title
-   Description
-   Viewpoint
-   Date
-   Time
-   Day
-   Duration
-   Tags
-   Section notes
-   Scene
-   Goal
-   Conflict
-   Outcome
-   Status
-   Words total
-   Word count
-   Characters
-   Locations
-   Items

> **Note**
> 
> Only "Normale" sections appear in the section table. Sections of the
> "Non usato" type are omitted.

File name suffix is `_sectionlist`.

Clicking on a section number with `Ctrl` pressed, you can jump to the
corresponding section in the manuscript. However, if you edit this
spreadsheet, you cannot apply the changes with *novelibre* (in contrast
to the plot grid). 
The section table is more intended for extracting the metadata of the
writing project, for example, in the case of abandoning *novelibre*.

## Mostra tabella temporale

**Show an HTML report with a time table**

With **Sezione > Mostra tabella temporale**, you can create a HTML file that
contains a time table, and launch your system's web browser for
displaying it.

In the time table, the dated "Normale" sections are listed in
chronological order. In addition to date/time and duration, the columns
include the section title, description, locations and characters as well
as plot lines with plot notes.

> **Note**
> 
> The report is a temporary file, auto-deleted on program exit. If needed,
> you can have your web browser save or print it.

---

[English manual](https://peter88213.github.io/nvhelp-en/)


Copyright (c) by Peter Triesberger. All rights reserved.

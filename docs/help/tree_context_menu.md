[novelibre Pagina principale](https://github.com/peter88213/novelibre) > [Pagine italiane](../) > [Aiuto in linea](./) > Tree view context menu

---

# Tree view context menu

When right-clicking on a tree element in the left pane, a context menu
opens that belongs to the type of the selected element.

> **Hint**
> 
> Greyed-out entries are not available, e.g. due to "project lock".

## Common context menu entries for the tree view

### Espandi tutto

Shows the whole tree.

### Riduci tutto

Hides all tree elements except the main categories.

### Livello del Capitolo

Hides the sections by collapsing the tree, so that only parts and
chapters are visible.

## Common context menu entries for clipboard operations

> **Hint**
>
>   If the selected element has "children", these will also be copied and pasted.

> **Attention**
>
>   Relationships are not included when copying to the clipboard.
>   This also applies to the section viewpoint and for plot lines/plot points.   


### Taglia

Move the selected element from the tree to the clipboard.
Same as ${`Ctrl`}-`X`.

### Copia

Copy the selected element to the clipboard.
Same as ${`Ctrl`}-`C`.

### Incolla

Paste the element stored in the clipboard to the tree.
Same as ${`Ctrl`}-`V`.



## Libro context menu entries

### Aggiungi Sezione

Adds a new section.

-   The new section is placed at the next free position after the
    selection.
-   The new section has an auto-generated title. You can change it in
    the right pane.

#### Properties of a new section

-   *Normal* type
-   *Outline* completion status
-   No viewpoint character assigned
-   No plot line or tag assigned
-   No date/time set

### Aggiungi Capitolo

Adds a new chapter.

-   The new chapter is placed at the next free position after the
    selection.
-   The new chapter has an auto-generated title. You can change it in
    the right pane.

### Aggiungi Parte

Adds a new part.

-   The new part is placed at the next free position after the
    selection.
-   In the tree, the part is at the same level as the chapters, so the
    chapters are not children of the part. This is to make it easier to
    move the part boundaries.
-   The new part has an auto-generated title. You can change it in the
    right pane.

### Inserire Fase

Inserts a new stage at the next free position at stage level after the
selection.

-   The new stage has an auto-generated title. You can change it in the
    right pane.
-   The new stage is on the second level by default.

### Modifica livello

Changes the level of a chapter or a stage.

-   **primo livello** converts a selected chapter into a part.
-   **secondo livello** converts a selected part into a chapter.

### Esporta questo capitolo

Exports a manuscript containing only the selected chapter. 
If a manuscript already exists,
confirmation is required before exporting.

> **Caution**
> 
> The exported document has the same file name as the complete manuscript.
> If you overwrite it before reimporting, changes to other chapters may be
> lost.

### Cancella

Deletes the selected tree element and its children.

-   Parts and chapters are deleted.
-   Sections are marked "Non utilizzato" and moved to the "Cestino" chapter.
-   Deleting a part has no effect on its subordinate chapters.
-   Deleting a chapter moves its sections to the "Cestino" chapter.
-   The "Cestino" chapter is created automatically, if needed.
-   When deleting the "Cestino" chapter, all its sections are deleted.

### Imposta tipo

Sets the type of the selected chapter or section. This can be 
*Normale* or *Non utilizzato*.

> **Note**
> 
> Setting the type of a chapter to *Non utilizzato* will also make its sections
> *Non utilizzato*.


### Imposta stato

Sets the completion status of the selected section.

> Hint
> 
> Select a parent node to set the status for multiple sections.

### Imposta POV

Sets or clears the viewpoint character of the selected section. A pop-up
window with a dropdown list appears, containing all characters in the
tree view's sort order. Click on the character you want to assign as
viewpoint character. If you click on the topmost entry (the blank one)
of the list, this will clear the viewpoint association.

> **Hint**
> 
> Select a parent node to set the viewpoint for multiple sections.


### Unisci al precedente

Joins two sections, if within the same chapter, of the same type, and
with the same viewpoint.

-   New title = title of the prevoius section & title of the selected
    section
-   The section contents are concatenated, separated by a paragraph
    separator.
-   Descriptions are concatenated, separated by a paragraph separator.
-   Goals are concatenated, separated by a paragraph separator.
-   Conflicts are concatenated, separated by a paragraph separator.
-   Outcomes are concatenated, separated by a paragraph separator.
-   Notes are concatenated, separated by a paragraph separator.
-   Character lists are merged.
-   Location lists are merged.
-   Item lists are merged.
-   Plot line assignments are merged.
-   Plot point associations are moved to the joined section, if any.
-   Section durations are added.

> **Caution**
> 
> Be aware, there is no "Undo" feature.

## Personaggi/Località/Oggetti context menu entries

### Aggiungi

Adds a new character/location/item.

-   The new element is placed after the selected one.
-   The new element has an auto-generated title. You can change it in
    the right pane.
-   The status of newly created characters is *minor*.

### Esporta manoscritto filtrato per POV

Exports a manuscript with the sections that have the selected character 
as viewpoint. If a manuscript already exists, confirmation 
is required before exporting.

> **Caution**
> 
> The exported document has the same file name as the complete manuscript.
> If you overwrite it before reimporting, changes to other sections may be
> lost.

### Esporta riassunti filtrati per POV

Exports the descriptions of the sections that have the selected character 
as viewpoint. If a synopsis already exists, confirmation is required 
before exporting.

> **Caution**
> 
> The exported document has the same file name as the complete synopsis.
> If you overwrite it before reimporting, changes to other section
> descriptions may be lost.

### Cancella

Deletes the selected character/location/item.

> **Caution**
> 
> Be aware, there is no "Undo" feature.

### Imposta stato

Sets the selected character's status. This can be *major* or *minor*.
Major characters are highlighted in the tree view.

> **Note**
> 
> The character status is only for visual distinction. It has no influence
> on the program functions. Nevertheless, you can use it to mark viewpoint
> characters or characters with their own plot lines.

> **Hint**
> 
> Select the *Personaggi* root node to set the status for all characters.


### ${Highlight sections with this viewpoint}

Highlights the sections that are narrated from the viewpoint
of the selected character.


### ${Highlight related sections}

Highlights the sections to which the selected character, location,
or item is related.

## Plot lines context menu entries

### Aggiungi Trama

Adds a new plot line

-   If a plot line is selected, the new item is placed after the
    selected one.
-   Otherwise, the new plot line is placed at the last position.
-   The new plot line has an auto-generated title. You can change it in
    the right pane.

### Aggiungi Snodo nella Trama

Adds a new Plot point

-   If a plot point is selected, the new plot point is placed after the
    selected one.
-   If a plot line is selected, the new plot point is placed at the last
    position.
-   Otherwise, no new plot point is generated.
-   The new plot point has an auto-generated title. You can change it in
    the right pane.

### Esporta manoscritto filtrato per trama

Exports a manuscript with the sections that belong to the selected 
plot line. If a manuscript already exists, confirmation is required 
before exporting.

> **Caution**
> 
> The exported document has the same file name as the complete manuscript.
> If you overwrite it before reimporting, changes to other sections may be
> lost.

### Esporta riassunti filtrati per trama

Exports the descriptions of the sections that belong to the selected 
plot line. If a synopsis already exists, confirmation is required 
before exporting.

> ** Caution**
> 
> The exported document has the same file name as the complete synopsis.
> If you overwrite it before reimporting, changes to other section
> descriptions may be lost.

### Modifica la sezione in Inutilizzata

Set all sections that are assigned to the selected plot line to
Non utilizzato. This excludes the entire plot line from the manuscript.

### Modifica la sezione in Normale

Set all sections that are assigned to the selected plot line to
Normale. This allows a plot line that has been excluded to be 
reintegrated into the manuscript.

### Cancella

Deletes the selected plot line/plot point.

> Caution
> 
> Be aware, there is no "Undo" feature. If you delete a plot line, all
> its plot points will be deleted, too.


### ${Highlight related sections}

Highlights the sections that are related to the selected plot line
or plot point.



## Project notes context menu entries

### Aggiungi Nota di Progetto

Adds a new project note.

-   If a project note is selected, the new project note is placed after
    the selected one.
-   Otherwise, the new project note is placed at the last position.
-   The new project note has an auto-generated title. You can change it
    in the right pane.

### Delete

Deletes the selected project note.

---

[English manual](https://peter88213.github.io/nvhelp-en/)


Copyright (c) 2025 by Peter Triesberger. All rights reserved.

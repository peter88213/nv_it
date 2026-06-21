[novelibre Pagina principale](https://github.com/peter88213/novelibre) > [Pagine in italiano](../../) > [Aiuto online](../) > [nv_writer](./) > Operation

---

# Operation

## Access Help

-   `F1` folds a help window above the editor window in or out.
-   `Alt`-`F1` opens this help page.

## Toggle the menu

-   `F3` folds the clickable menu bar below the editor window in or out.

## Change the editor window and font size

-   `Ctrl`-`+` increases the size.
-   `Ctrl`-`–` decreases the size.

---

## Switch between sections

-   `Ctrl`-`PgSu` loads the previous section, if any.
-   `Ctrl`-`PgGiù`, loads the next section, if any.
-   When loading another section, you may be asked for applying changes.

## Create a new section

-   `Ctrl`-`N` creates a new section.
    -   The new section is placed after the currently edited section.
    -   The new section is of the same type as the currently edited
        section.
    -   The editor loads the newly created section.

## Split a section

-   `Ctrl`-`L` splits the section at the cursor position.
    -   All the text from the cursor position is cut and pasted into a
        newly created section.
    -   The new section is placed after the currently edited section.
    -   The new section is appended to
        the currently edited section.
    -   The new section has the same status as the currently edited
        section.
    -   The new section is of the same type as the currently edited
        section.
    -   The new section has the same viewpoint character as the
        currently edited section.
    -   The editor loads the newly created section.

## Clone a section

-   `Ctrl`-`U` applies changes and creates an "unused" copy of the
    currently edited section in the background. This allows you to
    quickly and conveniently try out alternative text variations.

## Apply changes and save the project

-   `Ctrl`-`S` applies the changes made to the current section, and
    saves the whole project.

---

## Move the cursor and select text

-   Clicking the left mouse button positions the cursor just before the
    character underneath the mouse cursor, sets the input focus, and
    clears any selection.
-   Dragging with the left mouse button strokes out a selection between
    the cursor and the character under the mouse.
-   Double-clicking the left mouse button selects the word under the
    mouse and positions the cursor at the beginning of the word.
-   Dragging after a double click will stroke out a selection consisting
    of whole words.
-   Triple-clicking the left mouse button selects the line under the
    mouse and positions the cursor at the beginning of the line.
-   Dragging after a triple click will stroke out a selection consisting
    of whole lines.
-   The ends of the selection can be adjusted by dragging with the left
    mouse button while `Maiusc` is down; this will adjust the end of the
    selection that was nearest to the mouse cursor when the left button
    was pressed.
-   If the button is double-clicked before dragging then the selection
    will be adjusted in units of whole words; if it is triple-clicked
    then the selection will be adjusted in units of whole lines.
-   Clicking the left mouse button with `Ctrl` down will reposition the
    cursor without affecting the selection.
-   `Ctrl`-`A` and `Ctrl`-`/` select the whole text.
-   `Left` and `Right` move the cursor one character to the left or
    right and clear any selection in the text.
-   If `Left` or `Right` is typed with the `Maiusc` key down, then the
    cursor moves and the selection is extended to include the new
    character.
-   `Ctrl`-`Left` and `Ctrl`-`Right` move the cursor by words.
-   `Ctrl`-`Maiusc`-`Left` and `Ctrl`-`Maiusc`-`Right` move the cursor by
    words and also extend the selection.
-   `Up` and `Down` move the cursor one line up or down and clear any
    selection in the text.
-   If `Up` or `Down` is typed with `Maiusc` down, then the cursor moves
    and the selection is extended to include the new characters.
-   `PgSu` and `PgGiù` move the cursor forward or backwards by one
    screenful and clear any selection in the text.
-   If `Maiusc` is held down while `PgSu` or `PgGiù` is typed, then the
    selection is extended to include the new characters.
-   `Home` moves the cursor to the beginning of its line and clears any
    selection.
-   `Maiusc`-`Home` moves the cursor to the beginning of the line and
    also extends the selection to that point.
-   `Ctrl`-`Home` and `Ctrl`-`Up` move the cursor to the beginning of
    the text and clear any selection.
-   `Ctrl`-`Maiusc`-`Home` and `Ctrl`-`Maiusc`-`Up` move the cursor to the
    beginning of the text and also extend the selection to that point.
-   `End` moves the cursor to the end of the line and clears any
    selection.
-   `Maiusc`-`End` moves the cursor to the end of the line and extends
    the selection to that point.
-   `Ctrl`-`End` and `Ctrl`-`Down` move the cursor to the end of the
    text and clear any selection.
-   `Ctrl`-`Maiusc`-`End` and `Ctrl`-`Maiusc`-`Down` move the cursor to
    the end of the text and extend the selection to that point.

## Modify text

-   If any normal printing characters are typed, they are inserted at
    the point of the cursor.
-   `Del` deletes the selection, if any. Otherwise, it deletes the
    character to the right of the cursor.
-   `Backspace` deletes the selection, if any. Otherwise, it deletes the
    character to the left of the cursor.
-   `Ctrl`-`H` deletes the character to the left of the cursor.
-   `Ctrl`-`K` deletes from the cursor to the end of its line; if the
    cursor is already at the end of a line, then `Ctrl`-`K` deletes the
    newline character.
-   `Ctrl`-`D` deletes the character to the right of the cursor.
-   `Ctrl`-`T` reverses the order of the two characters to the left and
    right of the cursor.
-   `Ctrl`-`O` opens a new line by inserting a newline character in
    front of the cursor without moving the cursor.
-   `Ctrl`-`Maiusc`-`X` changes the case of the selected text to
    uppercase.
-   `Ctrl`-`Maiusc`-`Y` changes the case of the selected text to
    lowercase.
-   `Ctrl`-`Maiusc`-`C` capitalizes every word in the selection.
-   `Ctrl`-`Maiusc`-`S` toggles the case of each character in the
    selection.

## Undo/Redo

-   `Ctrl`-`Z` undoes the last editing. Multiple undo is possible.
-   `Ctrl`-`Y` redoes the last undo. Multiple redo is possible.

> **Important**
> 
> Only insert and delete operations are recorded as editing steps. Text
> formatting (see below) cannot be undone using this mechanism. Also, text
> formats are lost after redo operation.

## Convert into comment

-  `Ctrl`-`Alt`-`C` converts the selection into a comment.
   If the selection already contains a comment,
   it will be deleted and its content incorporated into the body text.

> **Note**
>
> The author of the novel is listed as the comment creator, if known.
> In contrast, comments created with *Writer* are always attributed 
> to the name listed in the OpenOffice/LibreOffice user properties.      

## Format text

-   `Ctrl`-`I` formats the selected text "Enfasi".
-   `Ctrl`-`B` formats the selected text "`Enfasi marcata`".
-   `Ctrl`-`M` removes "Enfasi" and "`Enfasi marcata`" formatting
    from the selection.

## Copy/cut/paste text

-   `Ctrl`-`C` copies the selection, to the clipboard.
-   `Ctrl`-`X` copies the selection to the clipboard and deletes the
    selection.
-   `Ctrl`-`V` inserts the contents of the clipboard at the position of
    the cursor.

---

## Word count

-   The section word count is displayed at the status bar at the top of
    the window.
-   By default, word count is updated manually by pressing the `F5` key.
-   The word count can be updated "live", i.e. just while entering
    text. This is enabled or disabled via the options dialog.

---

## End the distraction-free writing mode

-   `F11` exits the distraction-free writing mode.
-   Under Windows you can optionally exit with `Alt`-`F4`.
-   Otherwise you can optionally exit with `Ctrl`-`Q`.
-   When closing the editor window, you may be asked for applying
    changes.

## Interrupt the distraction-free writing mode (not recommended)

-   You can temporarily leave the distraction-free mode using your
    desktop's task switcher (e.g. via `Win`-`Tab` under Windows).

---

[English manual](https://peter88213.github.io/nvhelp-en/)


Copyright (c) by Peter Triesberger. All rights reserved.

    
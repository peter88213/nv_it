[Pagina principale](https://github.com/peter88213/novelibre) > [Index](../) > [Aiuto in linea](index.md) > Personaggio properties

---

# Personaggio properties

The Character properties view opens in the right pane when you select a
character in the tree.

![Screenshot](images/character_view01.png)

## Title and description

Title and description are displayed in an editable "index card".

The editing of the title can be completed by pressing the `Enter` key.
Changes to the description are applied when the mouse is clicked
anywhere outside the text input field.

## Nome completo

The character's title as shown on the index card is used as a short
name at several places. The full name can be entered separately. Editing
can be completed by pressing the `Enter` key.

## soprannome

This entry field is for alias names. Editing can be completed by
pressing the `Enter` key.

## Annotazioni

Tags are a very freely usable tool for labeling characters in the tree
view. Tags do not have to be defined elsewhere, but simply entered in
the input field separated by semicolons. Editing can be completed by
pressing the `Enter` key.

> **Caution**
> 
> If you want to use a tag more than once, make sure you use the same
> spelling in the different places.

> **Hint*
> 
> The [nv_zim plugin](https://github.com/peter88213/nv_zim/) can adopt
> keywords when creating a new wiki page for the character. This provides
> a powerful navigation aid.

## Personaggio principale

With the **Personaggio principale** checkbox you can change the character
status.

> **Note**
> 
> The character status is only for visual distinction. It has no influence
> on the program functions. Nevertheless, you can use it to mark viewpoint
> characters or characters with their own plot lines.

## Data di nascita and Data della morte

Format: *YYYY-MM-DD*, according to ISO 8601.

The editing of the birth and death dates can be completed by pressing
the `Enter` key.

## Campo 1

Expand or collapse this frame by clicking on the label.

![Screenshot](images/character_view02.png)

Changes are applied when the mouse is clicked anywhere outside the text
input field.

The default name is "Biografia". If this is not the right category for you,
you can change it in the book settings.

## Campo 2

Expand or collapse this frame by clicking on the label.

![Screenshot](images/character_view03.png)

Changes are applied when the mouse is clicked anywhere outside the text
input field.

The default name is "Obiettivi". If this is not the right category for
you, you can change it in the book settings.

## Collegamenti

Expand or collapse this frame by clicking on the label.

![Screenshot](images/world_view02.png)

This is a list for image and research document links.

Although *novelibre* holds some character/location/item data, it is not
the right application for extensive world building. For this, you may
want to use more powerful software, like [Zim Desktop
Wiki](https://zim-wiki.org/). In this case, *novelibre* allows you to
create links to the text files that will take you quickly to the right
places in the wiki.

Or you have collected some images that could inspire you when writing.
Then simply create links to these images to open them with your
system's standard image viewer.

> **Tip**
> 
> If you have collected several images for a character in a folder that
> your standard image viewer can browse through, a single link to any
> image file is sufficient.

The links are displayed in a list in the order they are entered.

### Aggiungi Link

When clicking on ![Aggiungi](images/add.png), a file selection dialog
opens. The selected file will be added to the link list.

> **Hint**
>
> By default, the dialog shows image files. For other file types,
> change the selector in the lower right corner.
>
> ![Screenshot](images/filePicker01.png)

### Rimuovi Link

When clicking on ![Rimuovi](images/remove.png) or pressing the `Canc`
key, the selected link is removed from the list.

### Aprire Link

When double-clicking on a link, or clicking on
![Vai a](images/goto.png), the link is opened with the standard
application for the link's file type.

> **Hint**
>
> If you want to open certain linked files with another application
> than the standard application, you can provide a *novelibre*
> "launcher" setting. For this, just create a text file named
> **launchers.ini** in the `.novx/config` directory (where all
> configuration files are stored). Here you can assign applications to
> the file extensions.
>
> Zim Desktop wiki pages are a special case. For this, the Zim program
> is assigned to the *.zim* extension.
>
> This example shows a setting that makes *novelibre* open text files
> with the *Zim Desktop Wiki* application instead of the standard text
> editor:
> 
> ```ini
> [SETTINGS]
> .zim = C:/Program Files (x86)/Zim Desktop Wiki/zim.exe 
> ```

## "Sticky note"

The yellow text area is for notes. Changes are applied when the mouse is
clicked anywhere outside the text input field.

When the "sticky note" of a plot point contains text, "N" is
displayed in the tree view as a reminder. If the branch of a plot line
with plot points containing notes is collapsed, the "N" is displayed
in the plot line row.

## Navigation buttons

-   **Precedente** lets you navigate to the previous character in the
    tree.
-   **Prossimo** lets you navigate to the next character in the tree.

---

[English manual](https://peter88213.github.io/nvhelp-en/)


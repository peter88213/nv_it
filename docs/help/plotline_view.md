[Pagina principale](https://github.com/peter88213/novelibre) > [Pagine italiane](../) > [Aiuto in linea](./) > Linea narrativa properties

---

# Linea narrativa properties

The Linea narrativa properties view opens in the right pane when you select a
plot line in the tree.

![novelibre screenshot](images/plotline_view01.png)

## Title and description

Title and description are displayed in an editable "index card".

The editing of the title can be completed by pressing the `Enter` key.
Changes to the description are applied when the mouse is clicked
anywhere outside the text input field.

## Nome abbreviato

Be sure to enter a short name to be displayed as a reference in the
tree. A single character like "A", "B", "C" is recommended.

The following example shows plot line short names as displayed in the
tree:

![novelibre screenshot](images/plotline_view02.png)

## Section assignments

The number of sections that belong to the selected plot line is shown
below the "Nome abbreviato" entry. The assignments can be made in the
section properties view. You can unlink all
sections from the selected plot line at once by clicking on the 
**Rimuovi l'assegnazione della sezione** button.

> Hint
> 
> A convenient way to manage and keep track of section assignments is
> offered by the
> [nv_matrix plugin](https://github.com/peter88213/nv_matrix/).

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

-   **Precedente** lets you navigate to the previous plot line in the
    tree.
-   **Prossimo** lets you navigate to the next plot linie in the tree.

---

[English manual](https://peter88213.github.io/nvhelp-en/)


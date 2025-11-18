[novelibre Pagina principale](https://github.com/peter88213/novelibre) > [Pagine italiane](../) > [Aiuto in linea](./) > Libro properties

---

# Libro properties

The Libro properties view opens in the right pane when you select
"Libro" in the tree, or when you click on the ![Mostra libro](images/viewBook.png) 
toolbar icon. It is the initial view after opening a *novelibre* project.

![novelibre screenshot](images/book_view01.png)

## Title, description, and author

Title and description are displayed in an editable "index card".

The editing of book title and author can be completed by pressing the
`Enter` key. Changes to the description are applied when the mouse is
clicked anywhere outside the text input field.

After exporting the book to an *ODT* document, title and description
appear in the document properties.

![Screenshot](images/book_view08.png)

These properties are visible, for example, when the mouse pointer is
over the document in the Windows Explorer.

![Screenshot](images/book_view09.png)

## Lingua del documento

Expand or collapse this frame by clicking on the label.

![novelibre screenshot](images/book_view02.png)

-   Language code acc. to ISO 639-1
-   Country code acc. to ISO 3166-2

This information controls the spelling checker for export documents.

![LibreOffice Writer screenshot](images/book_view10.png)

If not set, the System locale setting will be used as default.

> **Hint**
> 
> You can also set or change the document language with *Writer*, then it
> will be applied on import.
>
> ![LibreOffice Writer screenshot](images/book_view11.png)


## Numerazione automatica

Expand or collapse this frame by clicking on the label.

![novelibre screenshot](images/book_view03.png)

### Numera automaticamente i capitoli, Numera automaticamente le parti

If this checkbox is ticked, all chapters/parts are automatically
numbered each time the tree is refreshed. The chapter titles are
replaced with a `prefix-number-suffix` pattern (without the dashes).

> **Hint**
> 
> You can optionally exclude individual chapters/parts from
> auto-numbering in the Chapter/part properties.

Prefix and suffix entries can be completed by pressing the `Enter` key.

> **Note**
>
> Make sure to add a space character to separate the prefix or suffix from
> the chapter or part number.

### Usa numeri di capitolo romani

By default, arabic numbers, like "1", "2", "3" ... are used
for auto-numbering. If this checkbox is ticked, Roman numbers, like
"I", "II", "III", "IV" ... are used instead.

### Ricomincia numerazione all'inizio della parte

By default, the chapters are numbered consistently across the parts.
If this checkbox is ticked, the chapter numbering starts again with
"1" in each part.

## Nome del campo

Expand or collapse this frame by clicking on the label.

![novelibre screenshot](images/book_view04.png)

*novelibre* provides some ready-made fields for sections and characters
to store information that should be at hand when writing. You can name
these fields to fit into your individual story planning concept. Editing
the categories can be completed by pressing the `Enter` key.

### Non è una scena

When you set the Scene frame to **Non è una scena**, 
you see the three text boxes whose names you enter here.
These categories then apply to all sections that don't represent
scenes.

### Altra scena

When you set the Scene frame to
**Altro**, you see the three text boxes whose names you enter here.
These categories then apply to all sections that represent scenes
other than "Action" and "Reaction".

### Personaggio

Here you enter the names of the two character fields, 
you can open in the character properties view.

> **Hint**
> 
> You can reset a field name to its default value by clearing the input
> field and pressing the Enter key.

## Tempo narrativo

Expand or collapse this frame by clicking on the label.

![novelibre screenshot](images/book_view05.png)

To get an overview of the course of the story time, you can enter
date/time information for each section.
The date can be specific *(YYYY-MM-DD)* or unspecific (number of days,
e.g. from the beginning of the story).

### Data di riferimento

The reference date is optional. It can be used to convert relative
dates into absolute dates, or vice versa. The timeline software
plugins may use the reference date for creating events from sections
that have no date or an unspecific one.

Format: *YYYY-MM-DD*, according to ISO 8601.

> **Hint**
>
> Even if you don't need specific dates for your story, specifying a
> reference date might be helpful. Thus, a day of the week can be
> displayed along with the unspecific date,
> and ages can be calculated for related characters.

### Converto le date in giorni

This transforms specific section dates into days, related to the
reference date.

### Converto i giorni in date

This transforms unspecific section dates into specific ones, using
the reference date.

> **Note**
> 
> For large novels, the conversion may take some time, depending on your
> system. During the conversion time, the clicked button will display
> *"Attendere prego..."*.

> **Hint**
> 
> The commands above convert all dated sections at once. If you want to do
> the conversion for single sections, just go to the Section properties.

## Avanzamento della scrittura

Expand or collapse this frame by clicking on the label.

![novelibre screenshot](images/book_view06.png)

With *novelibre*, you can set a word count target and track your writing
progress.

> **Note**
> 
> Regardless of the entries made here, you can see the word count in the
> status bar at any time.

### Registrare i progressi di scrittura

By default, *novelibre* stores a log entry with the word counts for
each day on which you edit the project. You can prevent this by
unticking the **Registrare i progressi di scrittura** checkbox.

> **Hint**
> 
> For viewing the daily progress log, you may want to install the
> [nv_progress plugin](https://github.com/peter88213/nv_progress/).
 
### Parole da scrivere

Here you can enter a number (without decimal points or separators)
indicating your writing goal in words. The entry can be completed by
pressing the `Enter` key.

### Inizia conteggio

Here you can enter a number (without decimal points or separators)
indicating the word count you want to start from. The entry can be
completed by pressing the `Enter` key.

### Imposta l'attuale conteggio parole come inizio

Click this button to enter your current word count in the 
**Inizia conteggio** field.

### Parole scritte

Here the difference between your actual word count and the starting
count is displayed. The percentage refers to the words to write.

### Fase di lavorazione

This setting is for the tree viewer "Fase di lavorazione" coloring mode.

-   Sections with the same completion status as the selected work
    phase are black.
-   Sections that are ahead of the selected work phase are green.
-   Sections that are behind the selected work phase are magenta.

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


## Cover thumbnail

A cover thumbnail is displayed with the book properties if you provide a
PNG image file with the project name along with the *.novx* file. The
recommended image width is 100 to 200 pixels.

![Windows Explorer Screenshot](images/book_view12.png)

![novelibre screenshot](images/book_view07.jpg)

---

[English manual](https://peter88213.github.io/nvhelp-en/)


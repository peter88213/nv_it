novelibre [Pagina principale](https://github.com/peter88213/novelibre) > [Pagine italiane](../../) > [Aiuto in linea](../) > nv_tlview

---

# nv_tlview

**User guide**

This page refers to the latest
[nv_tlview](https://github.com/peter88213/nv_tlview/) release. You can
open it with **Aiuto > ${Timeline view Online help}** or with `F1`.

*nv_tlview* is a plugin providing a timeline view with sections that are
given a narrative date/day and time.

The plugin adds a **${Timeline view}** entry to the *novelibre* **Strumenti**
menu, and a **${Timeline view Online help}** entry to the **Aiuto** menu.
The Toolbar gets a ![Timeline](images/tlview.png) button.

![novelibre Screenshot](images/screen01.png)

## Operation

### Start the Timeline view

-   Open the Timeline view either from the main menu: 
    **Strumenti > ${Timeline view}**,
-   or via the ![Timeline](images/tlview.png) button in the toolbar.

### Mouse scrolling

-   Scroll the timeline horizontally with `Maiusc`-`Mousewheel`.
-   Scroll the timeline vertically with the mousewheel.
-   Scroll the timeline in any direction by right-clicking on the canvas
    and dragging the mouse.
-   Increase or reduce the time scale with `Ctrl`-`Mousewheel`.
-   Change the distance limits for stacking with
    `Maiusc`-`Ctrl`-`Mousewheel`.

### Selecting a section in the *novelibre* project tree

-   Select a section by double klicking on a timeline marker. This will
    bring the *novelibre* application window in the foreground.

### Shifting a section in time

-   Hold down the `Maiusc` button and click on the timeline marker, then
    drag it with the mouse. This will move the section forward or
    backward in time while keeping the duration.

### Shifting the section end

-   Hold down the `Ctrl` and `Maiusc` buttons and click on the timeline
    marker, then drag it with the mouse. This will increase or decrease
    the section's duration while keeping the start date/time.



> **Hint**
> 
> Shifting operations with the mouse can be aborted with the `Esc` key
> before releasing the mouse button. - Shifting operations with the mouse
> can be undone with ![undo](images/undo.png).


## Command reference

### "Vai a menu

#### ${First section}

Shift the timeline so that the earliest section is positioned near
the left edge of the window.

#### ${Last section}

Shift the timeline so that the latest section is positioned near the
right edge of the window.

#### ${Selected section}

Shift the timeline so that the section selected in the *novelibre*
project tree is positioned in the center of the window.

### "${Scale} menu

#### Ore

This sets the scale to one hour per line.

#### Giorni

This sets the scale to one day per line.

#### ${Years}

This sets the scale to one year per line.

#### ${Fit to window}

This sets the scale and moves the timeline, so that all sections
with valid or substituted date/time information fit into the window.

### "${Cascading} menu

The section marks are stacked on the timeline canvas, so that they would
not overlap or cover the title of previous sections. If the stacking
algorithm does not seem good enough to you, you can adjust its limits.

#### ${Tight}

Arrange consecutive sections behind each other, even if they are close together.

#### ${Relaxed}

Arrange consecutive sections in a stack, even if they are some distance apart.

#### ${Standard}

Reset the cascading to default.


> **Hint**
> 
> You can fine-tune the stacking limits with `Maiusc`-`Ctrl`-`Mousewheel`.


### "Opzioni menu

#### ${Use 00:00 for missing times}

-   If ticked, "00:00" is used as display time for sections without time information. This does not affect the section properties.
-   If unticked, sections without time information are not displayed.

### "Aiuto menu

#### Aiuto in linea

Open this help page in a web browser.

### Buttons in the footer toolbar

#### ![rewindLeft](images/rewindLeft.png) Go one page back

Shift the timeline to go about one screen width back in time. Same as the "back" mouse button (Windows).

#### ![arrowLeft](images/arrowLeft.png) Scroll back

Shift the timeline to go 1/5 screen width back in time. You can move it more precisely with the mouse wheel.

#### ![goToFirst](images/goToFirst.png) Go o the first section

Shift the timeline so that the earliest section is positioned near the left edge of the window.

#### ![goToSelected](images/goToSelected.png) Go to the selected section

Shift the timeline so that the section selected in the *novelibre* project tree is positioned in the center of the window.

#### ![goToLast](images/goToLast.png) Go to the last section

Shift the timeline so that the latest section is positioned near the right edge of the window.

#### ![arrowRight](images/arrowRight.png) Scroll forward

Shift the timeline to go 1/5 screen width forward in time. You can move it more precisely with the mouse wheel.

#### ![rewindRight](images/rewindRight.png) Go one page forward

Shift the timeline to go about one screen width forward in time.
Same as the "forward" mouse button (Windows).

#### ![arrowDown](images/arrowDown.png) Reduce the time scale

Reduce the time scale in major steps. Fine scaling is meant to be done with the mouse wheel.

#### ![fitToWindow](images/fitToWindow.png) Fit to window

This sets the scale and moves the timeline, so that all sections with valid or substituted date/time information fit into the window.

#### ![arrowUp](images/arrowUp.png) Increase the time scale

Increase the time scale in major steps. Fine scaling is meant to be done with the mouse wheel.

#### ![undo](images/undo.png) Undo the last change

This restores date/time/duration before the last mouse operation on a section.

    
> **Caution**
> 
> Interim changes to date/time/duration on the same section via the
> section properties in *novelibre* may get lost.

#### Close

Close the timeline viewer window. Same as `Ctrl`-`Q` (Linux) or `Alt`-`F4` (Windows).


---

[English manual](https://peter88213.github.io/nvhelp-en/)


Copyright (c) 2025 by Peter Triesberger. All rights reserved.

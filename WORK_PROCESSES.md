# How to Create These Notes, Anyway

I created these abominations. Here's how to use them for something vaguely approaching the good of mankind.

## Generating New HTML Notes

1.  Run the `createAllNotes.py` script with the following command: `python createAllNotes.py`.
2.  That's it! Any .txt notes currently in the folders you've specified for each class will have an HTML version generated, and can be viewed in any web browser.

## Adding a New Class's Notes

1.  Open `createAllNotes.py`
2.  At some point after the `notesToCreate` list has been declared but before the `convertNoteDirectory()` function is called, create a new `ClassNoteEntry` object with the following information, and append it to `notesToCreate`:

    ```python
    notesToCreate.append(ClassNoteEntry(
        # Full path (relative or absolute) from createAllNotes.py to the folder
        # where your .txt notes for this class are
        pathToNoteDirectory='../../classStuff/className/notes',

        # Full path from createAllNotes.py to the CSS
        # stylesheet for this class to use. This should be inside the 'css'
        # folder in this repo unless you have a good reason for it not to be.
        pathToStylesheet='css/classNameStyles.css',

        # Full path from createAllNotes.py to the folder where the HTML files
        # generated from your notes will be stored. This should be in a
        # subfolder of 'htmlNotes' named after your class.
        outputDirectory='htmlNotes/className',

        # The name you want this class to be displayed as on the note pages
        # themselves
        pageTitle='My Class Name'
    ))
    ```

3.  If you haven't already, create the `.css` stylesheet you specified last step with the following two rules (specifying the color gradient to use for that class's notes):

    ```css
    .className header:after {
        /* This gradient should be the same in both rules */
        background: linear-gradient(90deg,#ff573a, #0b2d8d);
    }

    ul.note-links-slider > li.active-note-page {
        background: linear-gradient(90deg,#ff573a, #0b2d8d);
    }
    ```

4.  Generate the HTML notes for the class.

5.  Add the stylesheet you just created to `index.html`.

    ```html
        <link rel="stylesheet" href="css/classNameStyles.css">
    ```

6.  Under the appropriate section, add a new card for this class to the `index.html` file. **Make sure to add the class's stylesheet class to the div, and a link to the 1st HTML notes file for the class.**

    ```html
    <div class="class-notes-card className">
        <a href="htmlNotes/className/0_firstDay_8_22_17.html">
        <header>
            <h3>CS #### - Class Name</h3>
            <h5 class="subtitle"><em>Some catchy tagline, huzzah!</em></h5>
        </header>
        </a>
    </div>
    ```

.. _forms_style_howtos:

===================================
How Tos - Fonts and colors of forms
===================================

Snooz gives every form the same look: the Inter font, and the colors of the Snooz theme (blue accent, links, selections, backgrounds). A form made in Qt Designer gets this look automatically. The form only chooses the sizes of its texts and which ones are bold, italic or underlined.

.. contents::
   :local:

Fonts in Qt Designer
==================================

Snooz loads the Inter font and shows every form in it, at the same size on Windows, macOS and Linux. The text of Snooz is 12 pt (16 px). In Qt Designer:

- Leave the **family** of the ``font`` property unset: Snooz shows every text in Inter, whatever the family.
- Choose the **size**, **bold**, **italic** and **underline** of a text in the ``font`` property of its widget, or in the rich text editor of a label or text box.
- Set them on the widget that shows the text (label, button, check box, text box, table...), not on the root widget of the form or on a page, a frame or a group box: Snooz does not pass their font reliably to the widgets inside.
- Do not write font rules in a style sheet (``font``, ``font-family``, ``font-size``...): a rule hides the fonts set in the ``font`` property of the widgets inside.
- Text pasted from another application brings its own font: paste it as plain text, or remove its font with the rich text editor.

Sizes for the headings and notes of a form:

=========================  =================================
Text                       Size in Qt Designer
=========================  =================================
Title of a page            18 pt, bold (24 px in Snooz)
Title of a section         15 pt, bold (20 px)
Title of a group or field  12 pt, bold (16 px)
Text, fields, buttons      no size: 12 pt (16 px) in Snooz
Note, hint                 10 pt (13 px)
=========================  =================================

.. note::
   Sizes in points are converted to pixels when the form is shown (12 pt = 16 px), so a text has the same size on every operating system.
   Qt Designer shows a text without a size in its own font (9 pt on Windows), smaller than Snooz: leave room for the text to grow.

Text styles in code
==================================

For a text created in Python code, use the text styles of Snooz (``commons/fonts.py`` of the toolbox) instead of ``setFont`` or a font rule in a style sheet:

.. code-block:: python

   from commons.fonts import set_text_style, text_label, text_style_font

   title = text_label("Recent files", "h2")    # a new label in the h2 style
   set_text_style(self.result_label, "small")    # an existing widget
   painter.setFont(text_style_font("body"))      # a text painted in code

=========  ===================================
Style      Text
=========  ===================================
``h1``     24 px, bold
``h2``     20 px, bold
``h3``     16 px, bold
``body``   16 px, the text of every widget
``small``  13 px
``mono``   14 px, monospaced (logs, code)
=========  ===================================

Colors and links
==================================

The colors of Snooz come from its theme. A form should not set colors:

- Do not set colors in a style sheet (``color``, ``background-color``) or in the palette of a widget.
- Write links with the rich text editor (or ``<a href="...">``) without changing their color: Snooz shows them in the link color of its theme.
- For a color painted in code, take it from the palette of the widget, for example ``widget.palette().color(QPalette.ColorRole.Highlight)`` for the accent or ``QPalette.ColorRole.Link`` for links.

Check the fonts of your forms
==================================

Snooz checks the fonts of the forms of your packages each time it starts from the source code (see :ref:`run_snooz`). Once its window is open, it checks the forms of the packages added in its settings, and prints the result in the terminal of VS Code. It reports the settings that Snooz does not show, or that hide the fonts of other widgets:

- a font family, in the ``font`` property of a widget or in a rich text;
- a font rule in a style sheet;
- a size on the root widget or on a container (page, frame, tab widget...).

When every form follows this guide, Snooz prints one line::

   Fonts of the forms of your packages: 296 form(s) checked, all follow the guideline.

Otherwise, each setting to fix is listed with its form and its widget, for example::

   Fonts of the forms of your packages: 296 form(s) checked, 1 to fix (2 setting(s)):
     C:/snooz_workspace/my-package/tools/MyTools/MyTool/MyStep/Ui_MyStep.ui
        - title_label: font family Arial
        - frame: font size 14pt on a QFrame

Fix them in Qt Designer, then update the Python file of the form (``Ui_MyStep.py``) as usual.

To check the forms without starting Snooz, open a terminal with the virtual environment **snooz_310_env** activated (see :ref:`installation`), go to the ``src/main/python`` folder of the toolbox, and type ``python check_form_fonts.py`` followed by the folder of your package. In the CEAMS package repository (snooz-package-ceams), you can also type ``python main_utils.py`` and select **7- Check the fonts of the forms**: it uses the toolbox placed next to the repository in the Snooz workspace.

.. note::
   With ``--strict``, the check ends with an error when a form has settings to fix: it can run before each commit (pre-commit hook) or as an automatic check of the repository.

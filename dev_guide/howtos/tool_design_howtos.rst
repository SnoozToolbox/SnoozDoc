.. _tool_design_howtos:

=====================================================
How Tos - Design of the pages of tools and modules
=====================================================

Every page of a tool (a step of the step-by-step interface) and every settings view of a module follows the same pattern, so users find the settings, their help and the warnings at the same place everywhere:

1. a **header**: the title of the page and one muted sentence saying what the step is for;
2. the **settings first**, in white **cards**: a bold title, the settings, then one small line of help;
3. **callouts** for what must not be missed: a limit to respect (amber) or something to do first (blue);
4. **About ...** at the end: how the method works, in muted text.

Follow these rules for every new tool, and when you redesign the pages of an existing tool. The tool **Analyze EEG Spectral Power** of the CEAMS package (``tools/CEAMSTools/PowerSpectralAnalysis``) is the reference: its introduction (``IntroStep``), ``FilterStep``, ``SelectionStep``, ``SpectralSettings`` and ``Outputfiles`` pages, and its sub-step ``HoursCyclesStep``.

The sizes of the texts are the ones of :ref:`forms_style_howtos`.

``python main_utils.py`` creates the forms in this layout: **2- Create a module** creates the settings view of the module, with one field per input; **4- Create a tool step** creates the page of a step, or the introduction page when it is the first custom step of the tool.

.. tip::
   The same rules are in ``ui_design_guideline.md``, at the root of the package repositories (snooz-package-ceams and snooz-package-template). To have a page designed by an AI agent, point the agent to this file.

.. contents::
   :local:

Where the look comes from
==================================

The forms only **mark** their widgets: a frame shape or a ``variant`` dynamic property. The colors, borders and backgrounds are in the style sheet of the Snooz toolbox (section TOOL PAGES of ``ui/themes/light/stylesheet.qss``, colors in the ``tokens.json`` of each theme, see :ref:`info_theme`), so the light and dark themes are both right without any work in the package.

- Never set a style sheet, a color or a font family in a form, and no colored HTML (such as a red "NOTE:"). Use the building blocks below.
- Qt Designer does not load the Snooz style sheet: cards and callouts look plain there. Check the look in Snooz, in the light and the dark theme.
- The callouts, the step numbers, the link buttons and the muted text boxes need Snooz Toolbox 1.2.0 or later (TOOL PAGES rules of its style sheet). An older Snooz shows them plain.

The building blocks
==================================

.. list-table::
   :header-rows: 1
   :widths: 18 52 30
   :class: wrap-cells

   * - Element
     - In Qt Designer
     - Shown as
   * - Page title
     - QLabel, ``font``: 18 pt, bold. Text: the name of the step (the name of the tool on the introduction)
     - 24 px, bold
   * - Subtitle
     - QLabel under the title, ``wordWrap``, dynamic property ``variant`` = ``help``. One sentence: what the step is for
     - 16 px, muted
   * - Heading
     - QLabel, ``font``: 15 pt, bold, above a card (introduction page: "What you will do", "Accepted files")
     - 20 px, bold
   * - Card
     - QFrame, ``frameShape`` StyledPanel, ``frameShadow`` Raised. Its layout: margins 10 (the style sheet adds 6), spacing 10
     - white rounded card
   * - Card title
     - QLabel, ``font``: bold, or the bold check box that turns the group on
     - 16 px, bold
   * - Muted line
     - QLabel, ``wordWrap``, ``variant`` = ``help``: a line under the card title (what the group is for, "Optional.")
     - 16 px, muted
   * - Unit
     - QLabel after the field, ``variant`` = ``help``: "Hz", "s"
     - 16 px, muted
   * - Help
     - QLabel, ``font``: 10 pt, ``wordWrap``, ``variant`` = ``help``. Under a check box or a radio button: ``indent`` 26 (aligned with its text)
     - 13 px, muted
   * - Line
     - QFrame, ``frameShape`` HLine, ``frameShadow`` Plain: between two options of a card, between two steps of the introduction
     - 1 px line
   * - Warning
     - QFrame, ``frameShape`` NoFrame, ``variant`` = ``warning``. Its layout: QHBoxLayout, margins 14, 10, 14, 10, holding one QLabel (rich text, ``wordWrap``): ``<b>Title</b><br/>text``
     - amber box, bar on the left
   * - Info
     - Same as the warning, with ``variant`` = ``info``
     - blue box, bar on the left
   * - About
     - QLabel bold (``About the filters``), then a QLabel ``wordWrap``, ``variant`` = ``help``, in a QVBoxLayout (spacing 6)
     - 16 px, muted
   * - Step number
     - QLabel, ``font``: 10 pt, ``variant`` = ``step_number``, minimum and maximum size 24 x 24, ``alignment`` centered
     - number in a blue circle
   * - Link button
     - QPushButton, ``flat``, ``variant`` = ``link``, ``focusPolicy`` TabFocus: shows a hidden part of the page ("› Methods and references")
     - blue text
   * - Illustration
     - A drawing of the code, in the colors of the theme (palette ``Text`` and ``Link``), painted on a QLabel without picture, in a card with a small caption (Detect Spindles with A7: ``SpindleDetectionDoc.py``). Snooz puts a picture (QLabel with a pixmap) in a white card, made for pictures on a white background
     - sharp, light and dark themes
   * - References
     - QVBoxLayout ``references_layout`` (margins 0, 6, 0, 0; spacing 8): a line ``references_line`` (QFrame HLine, Plain), then a QLabel ``references_label``, ``font``: 10 pt, ``wordWrap``, ``variant`` = ``help``, rich text, ``openExternalLinks`` true, one reference per line (``<br/>``). Under the text that cites them, see `Writing the texts`_
     - a line, then the references: 13 px, muted, blue links

**Adding the variant property in Qt Designer:** select the widget, click **+** at the top of the Property Editor, choose **String**, name it ``variant``, then type the value. Untick *translatable*: the value is not a text for the user.

Making a step page, step by step
==================================

1. **Create the form** with ``python main_utils.py``, **4- Create a tool step**: the form already has the layout below, the header (the label and the description of the step) and a first card. For an existing tool, copy the form of a reference page and rename its class. Give the widgets that are not inputs names that say what they are (``bandpass_card``, ``nyquist_warning``, ``about_filters_label``).
2. **Lay out the page.**

   - Top-level layout of the form: QVBoxLayout, margins 19, 12, 19, 12.
   - In it, a QHBoxLayout named ``content_row`` (margins 0) holding a QWidget named ``content_widget`` and a horizontal spacer. Set the ``layoutStretch`` of ``content_row`` to ``1,0``.
   - ``content_widget`` has a maximum width of **800 px** (lines stay readable on wide screens) and holds a QVBoxLayout ``content_layout`` with margins 0 and spacing **16**.
   - Under ``content_row``, a vertical spacer, so the page stays at the top.

   .. note::
      Do not put ``content_widget`` directly in the QVBoxLayout of the form. A QVBoxLayout computes the height of the wrapped texts for the whole width of the page, not for the maximum width of ``content_widget``: on a wide window, the texts that wrap are cut. The QHBoxLayout gives ``content_widget`` its real width.

3. **Write the header.** The page title and the subtitle, in a QVBoxLayout (spacing 6).
4. **Group the settings into cards.** One card per group of settings the user decides together (the FFT windows, the frequency bands, the method). Put the cards in the order the user decides.

   - Two short cards go side by side: a QHBoxLayout, spacing 16, ``layoutStretch`` ``1,1``. End each card with a vertical spacer, so their contents stay at the top.
   - A group that can be turned on or off starts with its check box, in bold, as the card title.
   - A card alone and short (two fields) takes half the width: put it in a QHBoxLayout (spacing 16) with a fixed horizontal spacer of 16 px and a horizontal spacer, ``layoutStretch`` ``1,0,1``. Qt adds no spacing next to a spacer: without the fixed spacer, the card is 8 px wider than the cards of a row below it.

5. **Lay out the settings in each card.**

   - Settings with a value: a QGridLayout, horizontal spacing 12, vertical spacing 10. Label in column 0, field in column 1, unit in column 2, a horizontal spacer in column 3. The label has no unit: the unit is after the field.
   - The minimum and maximum of the same value: one QGridLayout per card, with the columns label | "Min" | field | "Max" | field | unit.
   - Options (check boxes, radio buttons) with a help: the option, its help under it (``indent`` 26) in a QVBoxLayout (spacing 2), a line between two options. The radio buttons of one choice have the same parent, so they are exclusive.
   - One small help line at the end of the card when the settings need it ("IIR bandpass, order 6"). The details go in About.
   - A button with a tooltip keeps its own width. Stretched, its centered text runs under the help mark (?).

6. **Add the callouts.** A limit to respect (sampling rate, minimum duration) goes in an amber callout under the cards; something to do before setting the step goes in a blue callout under the header. The title says what it is about ("Highest cutoff frequency"), the text says what to do.
7. **Put the method last.** How the method works, the formulas and the examples go in **About ...** at the end of the page ("About the filters", "About the frequency resolution").
8. **Connect the signals** in the Signal/Slot Editor, as before.
9. **Generate the Python file** of the form with the version of Qt used by Snooz (6.8.2):

   .. code-block:: console

      pyside6-uic Ui_MyStep.ui -o Ui_MyStep.py

10. **Check the page in Snooz.** Open the tool and go through every step:

    - in the light and the dark theme (File > Settings > General Settings > Theme);
    - in a window about 1300 px wide, 1500 px wide and maximized;
    - no text is cut (look at the texts on two lines or more), no horizontal scroll bar appears.

The introduction page
==================================

The first page of a tool presents it. From top to bottom:

1. **Header:** the name of the tool, and one sentence: what the tool computes or does.
2. **Before you start** (blue callout), only when something must be done before the steps of the tool: **Common settings › Sleep Cycles**, in the left panel, or a file or option prepared in another tool (for example, the cohort report option of a detection tool). Take it from the original page. Never add one that repeats a step (What you will do, the step description): a tool with nothing to do first has no Before you start.
3. **What you will do** (heading and card): one row per step, in a QGridLayout (horizontal spacing 12, vertical spacing 10, ``columnStretch`` ``0,0,0,1``): the step number (column 0, item alignment top), the name of the step in bold (column 1), a fixed horizontal spacer of 16 px (column 2, first row only), what the user does in the step in a muted label (column 3). A line spanning the 4 columns between two steps. Optionally, a heading and a card after it give advice for the tool: what the user must know about the data ("Sleep stages", "Channels").
4. **Accepted files** (heading and card), if the tool reads PSG files: a QGridLayout (horizontal spacing 32, vertical spacing 6): the format in bold, then what it needs.
5. **Methods and references**, shown on demand. Name the links "Methods" when the tool cites nothing, and leave them out when there is no method to describe.

   - two link buttons in a QHBoxLayout with a spacer: ``methods_show_button`` ("› Methods and references") and ``methods_hide_button`` ("⌄ Methods and references", property ``visible`` false), then a help "The details of each setting are shown in its own step.";
   - a QWidget ``methods_widget`` (property ``visible`` false) holding the methods, then the references block (a line, then the references);
   - connections (Signal/Slot Editor): ``clicked()`` of ``methods_show_button`` to ``show()`` of ``methods_widget`` and ``methods_hide_button`` and to ``hide()`` of itself; ``clicked()`` of ``methods_hide_button`` to ``hide()`` of ``methods_widget`` and of itself and to ``show()`` of ``methods_show_button``.

The settings view of a module
==================================

The settings view of a module is shown in its window in the process designer, whose title band shows the name and the version of the module, and as a step of a tool when the step is defined by a ``module_id`` (the steps column shows the name of the step, which can differ from one tool to the next). So:

- **No page title:** start with the cards. A muted line above the first card only when the settings need context, written for every tool that uses the module.
- **The same layout, cards, fields, options, callouts and About** as the page of a step. The window of the process designer is about 700 px wide: check that the cards side by side still read well.
- **The generated form** has a card with one field per input (``<input>_label`` and ``<input>_lineedit``, used by ``<Module>SettingsView.py``). Replace the labels (the names of the inputs) by words ("Minimum duration", not ``min_duration``), put the unit after the field, and choose the right widget for each input (QDoubleSpinBox, QComboBox, QCheckBox...), changing the code of ``<Module>SettingsView.py`` with it (``setText``/``text`` become ``setValue``/``value``...).
- A module without settings the user can edit keeps an empty settings view (see :ref:`module_howtos`).

Pages shared by several tools
==================================

Some step forms are used by several tools: the step of another tool inherits the class of the step. For example, ``NonValidEventStep`` of Analyze EEG Spectral Power is used by the event steps of 9 tools. The settings views of the modules are shared the same way.

- **No page title:** each tool gives the step its own name.
- **Keep every widget name:** the steps that inherit the form use them (``setText``, ``setEnabled``).
- **A page of lists:** see below.
- **Check** the page in every tool that uses it. Raise the version of each of these tools when you redesign the pages of that tool.

A page of lists
==================================

A page of lists (files, events, channels, reports):

- **The lists take the whole page:** no ``content_widget`` of 800 px, the cards side by side fill the page.
- **Title:** a step of the tool keeps its header (the name of the step and a subtitle). A page shared by several tools and the settings view of a module have no title.
- **A card per list:** a bold title (its help in the tooltip), the list, then a row with a small help on the left (stretch 1) and the buttons on the right ("Choose files", "Clear all").
- **Helps in tooltips,** on the title of the list or on the control they describe, so the lists keep their room.
- **A message box** (a read-only text box filled by the code) goes under the lists, at full width, and the lists get a minimum height (240 px): the toolbox makes a read-only text box as high as its text, which would squeeze the lists.

Writing the texts
==================================

- **Short and simple**, in the user's words: what the setting does or what to do. Not "Check this option to...", not "The user may...": say what the option does ("Optionally, add...").
- **Keep the information:** when you reformulate an existing text, keep everything it says; only the wording changes. Do not drop an option or a condition to make a text shorter.
- **Page title:** the name of the step, as written in the json file of the tool (the steps column).
- **Subtitle:** what the step is for, in one sentence.
- **Callouts:** a title of a few words, then one sentence.
- **Names from the interface in quotation marks:** the name of a step, a section, a field, a check box, an option, a button, a list or a column, written as on the page: In "Events from selection", the changes apply to the selected recording. Not the technical identifiers of a file (group, start_sec), nor everyday words (the suffix, the PSG files).
- **Sentences:** short. No colon or semicolon in the middle of a sentence. A definition is a sentence of its own. Lists, cases and the columns of a file are bullet points (``• ...<br/>``) after a short sentence that ends with a period. A long About block has small bold subheadings (``<b>Reading the stages</b><br/>``).
- **Files:** name the kind of file (the PSG file, the sleep stage file, the accessory file). Never a bare "file" when the tool has several kinds of files.
- **One place for each text:** a callout or an About block is on one page, the step where it applies. An important warning (the orange callout) can stay on the introduction too.
- **Examples:** explain a setting with a worked example (a path before and after, a file name with its suffix), and check it against the code.
- **Introduction:** only what is needed to use the tool and understand how it works. File examples, long lists and column-by-column details go to the documentation of the tool, and the page points to it (the documentation of the tool, "Read more!" below).
- **Step description** (``description`` of the step in the json file of the tool, shown in the steps column, left of the pages): what the user does in the step, in one or two short sentences (30 words at most), with the meaning of the step's row in What you will do. The page holds the rest.

  - Plain text: no blank lines, lists, HTML layout or file formats (the accepted files are in the introduction, the details on the page).
  - No "Click", "i.e." or "your study"; no "To define..." (write "Define..."). Start with a capital letter, end with a period.
  - Rewrite the description of every step of the tool you redesign, the first step (the page of the tool) excepted: it keeps its link to Read more!.
  - A step description is a display text: a workspace keeps the one it was saved with.
- **Abbreviations:** write them in full ("power spectral analysis", not "PSA"), except the usual units and formats (Hz, EDF, FFT).
- **Tooltips:** put the tooltip of a setting on its label, so the help mark (?) is next to the name of the setting. No tooltip that only repeats the name of the widget ("Check to perform the analysis on N1." on the check box N1). When you remove a description from the page, keep the most accurate description in the tooltip.
- **References:** the same format everywhere, APA style: numbered in the order of the text ([1], [2]...); up to 20 authors, "&" before the last one; the journal and the volume in italics; a dash (–) between the pages; the DOI link at the end. They go in the references block, where a line separates them from the text that cites them. A text set by the code (a text box) never holds its references: put them in the references block of the form, and hide the block when the text has no reference. The text of a reference:

  .. code-block:: html

     [1] Feinberg, I., &amp; Floyd, T. C. (1979). Systematic trends across the night in human sleep cycles. <i>Psychophysiology</i>, <i>16</i>(3), 283–291. <a href="https://doi.org/10.1111/j.1469-8986.1979.tb02991.x">https://doi.org/10.1111/j.1469-8986.1979.tb02991.x</a>

Things not to do
==================================

- No style sheet, color, font family or HTML color in a form.
- No font size other than 18 pt (page title), 15 pt (heading), 12 pt (no size) and 10 pt (help).
- No QTextEdit for a fixed text: use a QLabel with ``wordWrap``. A QTextEdit has its own height and scroll bar, and cuts the text.
- No fixed minimum or maximum width on labels: let the layout size them. Keep a maximum width on short inputs (80 to 110 px for a number).
- No settings under a long text: the settings come first, the method last.

Redesigning an existing tool
==================================

1. **Before** changing anything, save workspaces of the original pages: one with the default settings, one with every setting changed. A workspace saved before the redesign must open in the redesigned tool and give the same results.
2. **Redesign** the pages. Keep every input widget: its object name, its class, its default value or state, its range, whether it is enabled, and its signal connections. Keep the name of every widget used in the code of the step (search ``self.<name>`` in the .py file of the step), labels included. Keep the tooltips.
   A text box whose text the code sets or saves stays a text box: frameless (``frameShape`` NoFrame), with ``variant`` = ``help`` for a muted text. A text box the code only enables or disables can become a muted QLabel with the same name. Keep the button groups of the form (``<buttongroups>``): its radio buttons refer to them.
3. **Check:** the workspaces saved the same way after the redesign must be identical to the ones saved before (only the versions and the step descriptions change), no tooltip is missing, no text is cut.
4. Raise the version of the tool (``tool_version`` in the json file of the tool and ``item_version`` of the tool in the json file of the package) and add a line to the Version History of its documentation page.

Checklist
==================================

- Header: page title (18 pt) and a muted subtitle.
- Settings first, in cards, in the order the user decides; short cards side by side.
- Units after the fields; one small help line per card or per option.
- Limits in amber callouts, things to do first in blue callouts, each with a title.
- How the method works last, in About.
- ``content_widget`` at most 800 px wide, in ``content_row`` (stretch ``1,0``), vertical spacer at the bottom.
- Introduction page: Before you start (only when something must be done first, never repeating a step), What you will do, advice for the tool (if needed), Accepted files, Methods and references on demand ("Methods" when nothing is cited).
- Steps column: each step description is one or two short sentences (30 words at most), what the user does, without blank lines, lists or file formats.
- Settings view of a module: no page title, the inputs as fields with words and units.
- Texts short, information kept, abbreviations in full, tooltips on the labels and never only repeating a name.
- References after a line, in APA style with their DOI link, 10 pt, muted.
- Page shared by several tools: no title, widget names kept, checked in every tool.
- Page of lists: the whole page, a card per list (help in the tooltip of its title, buttons on the right), message box under the lists; a step of the tool keeps its title.
- No style sheet, color, font family, other font size or QTextEdit for a fixed text.
- Python file generated with pyside6-uic 6.8.2.
- Checked in Snooz in the light and dark themes, at about 1300 px, 1500 px and maximized: no text cut.
- Existing tool: same saved workspaces before and after, button groups and tooltips kept, tool version raised.

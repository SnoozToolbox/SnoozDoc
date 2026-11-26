.. _EDFbrowser_Converter:

===========================================
Convert Annotations from EDFbrowser
===========================================

This tool converts EDFbrowser .txt annotation files to Snooz .tsv annotation files. 
In Snooz, annotations are grouped, a feature that does not exist in EDFbrowser. 
This tool allows you to add annotations to the 'stage' and 'art_snooz' groups.
Additionally, you can optionally add any annotation to any group.

.. warning::

    The converted file is written next to the annotation file, with the same name: a .tsv file with that name is replaced.

Steps
-----------------

**1 - Input Files**

Add the .txt annotation files to convert to Snooz .tsv annotation file.
	
Define the column index of each annotation feature

* Event group : none in EDFbrowser
* Event name (description label) : column 3 
* Event onset (starting point) : column 1
* Event duration : column 2
* Event channel : none because EDFbrowser includes it in the event name

**2 - Stage Annotation Selection**

Check all the annotation names that correspond to the sleep stages.  The event group "stage" will be added to those annotations for further analyses in Snooz.

**3- Artifact Annotation Selection**

Check all the annotation names that correspond to the artifacts.  The event group "art_snooz" will be added to those annotations for further analyses in Snooz.

**4- Event Group Definition**

Edit the annotation group as you wish.  The default group is EDFbrowser.

.. note::
    
    Enjoy the push button "Apply to all files" to convert files in batch.

    Look at the "Convert Annotations from EDFbrowser" home page and the step pages for more information.
     
.. warning::

    Make sure to rename the output file properly.
	In Snooz, the PSG files must have the same name as the annotation files.

	i.e. ``subject1.edf`` and ``subject1.tsv`` **is valid** 
    
        i.e. ``subject1.edf`` and ``subject1_annotation.tsv`` **is not valid**


Version History
-----------------

* v2.0.0 : Distributed with CEAMS package version 7.2.0 — Snooz beta 2.0.1
    - Initial release of the tool.

* v2.1.0 : Distributed with CEAMS package version 7.3.0 — Snooz beta 3.0.0
    - Added support for the new optional time elapsed column.

* v2.3.1 : Distributed with CEAMS package version 7.5.0 — Snooz Toolbox 1.1.0
    - Fixed the TSV Writer module to support an empty list of annotations.
    - Improved validation dialogs using TableDialog.
    - Updated the forms to the new look of Snooz Toolbox 1.1.0 (Inter font, light and dark themes).

* v2.3.2 : Distributed with CEAMS package version 7.6.0 — Snooz Toolbox 1.2.0
    - Redesigned the pages and the step descriptions of the tool, including the settings view of the Csv Reader Master module.
    - Fixed Select All in the selection steps: with no file selected, it wrote an error in the console.
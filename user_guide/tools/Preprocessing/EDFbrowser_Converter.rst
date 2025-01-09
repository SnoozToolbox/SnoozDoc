.. _EDFbrowser_Converter:

======================
Convert EDFbrowser
======================

Description
-----------------

This tool converts EDFbrowser .txt annotation files to Snooz .tsv annotation files. 
In Snooz, annotations are grouped, a feature that does not exist in EDFbrowser. 
This tool allows you to add annotations to the 'stage' and 'art_snooz' groups.
Additionally, you can optionally add any annotation to any group.

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

    Look at the "EDFbrowser Converter" home page and the step pages for more information.
     
.. warning::

    Make sure to rename the output file properly.
	In Snooz, the PSG files must have the same name as the annotation files.

	i.e. ``subject1.edf`` and ``subject1.tsv`` **is valid** 
    
        i.e. ``subject1.edf`` and ``subject1_annotation.tsv`` **is not valid**

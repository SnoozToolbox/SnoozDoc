.. _tools:

======
Tools
======

This section describes how to use tools within Snooz.

Launch tools from the menu
=============================

The tools installed within Snooz are divided into three categories. Each category has direct access from the menu bar of Snooz.

1. **Preprocessing**: Includes importers/converters/extractors and the artifact detection tool.
2. **Processing**: Includes sleep stages analyses, event detectors, and power spectral analysis.
3. **Postprocessing**: Includes secondary analyses such as performance evaluation of detectors, transposition of cohort reports, and slow wave events analysis.

A new user
-----------

If you are new to Snooz, we recommend beginning with the Preprocessing category.  
The Preprocessing category includes importers, converters, extractors, and the artifact detection tool.
The main goal of the user is to create a cohort compatible with Snooz, see :ref:`accepted_format` for more details.

Ready for the analysis  
-----------------------

Once your PSG files are compatible with Snooz, proceed to the Processing category.  
The Processing category includes sleep analyses, event detectors, and power spectral analysis.

Cohort analysis  
----------------

The Postprocessing category includes secondary analyses, such as performance evaluation of detectors,
transposition of cohort reports, and slow wave events analysis.

Viewer
-------

The only available Viewer is the Oximeter, which allows you to select bad sections to generate a valid Oxygen Saturation Report.
The Oximeter is an application that operates within Snooz.  (See :ref:`apps` for more details.)

.. _accepted_format:

Accepted file formats
==========================================================

**Polysomnography file format**

The only accepted format for polysomnography is the European Data Format (EDF). For more details, see `European Data Format <https://www.edfplus.info/specs/edf.html>`_.
Snooz can also read signals from the EDF+ format; however, annotations must be imported from the EDF+ file into a .tsv (Tab-Separated Value) format compatible with Snooz.
See :ref:`EDF_Annotations_Importer` for more details.

.. note::

   CEAMS users have access to two additional PSG file formats: Harmonie and NATUS.

**Annotations file format**

The columns of the annotations file are as follows:

1. **group** : The category of the annotation (annotations with different names can be grouped into the same category), e.g. artifact
2. **name**: The text label of the annotation, e.g., art_snooz
3. **start_sec**: The onset of the annotation in seconds, e.g., 300
4. **duration_sec** : The duration of the annotation in second, e.g., 30
5. **channels** : The list of channels on which the annotation occurs, e.g., ['LOC', 'ROC']

To have an example of the Snooz annotations file see `Snooz_accessory_file.tsv <https://f004.backblazeb2.com/file/snooz-release/doc/Snooz_accessory_file.tsv>`_

Many converters have been implemented in Snooz. 
I recommend exploring the preprocessing category to see if your annotation files can be converted into Snooz accessory files.

Navigate in the step-by-step interface
==========================================================

Here is an example of an empty tool to show you around.

.. image:: ./ToolA_example_edited_small.png
   :width: 700
   :alt: Alternative text    

**1.** Launch the tool from the menu bar of Snooz.  

**2.** The Snooz left panel allows you to navigate across views.  
   
   .. note::

      * Home : The Snooz Home page with the recents files list.
      * Tool : The step-by-step interface for the current tool.
      * Process : The pipeline with the interconnected modules.
  

**3.** The steps panel and the "Previous" and "Next" buttons allow you to navigate through each step of the tool.  

   .. note::

      * The introduction step is the home page of the tool. It describes how to use it. 
      * The number of steps is specific to each tool.
      * Each step describes what the user must define as settings.  

**4.** The user can save the workspace (.json file) at any moment. The workspace includes all the settings defined by the user in the current tool.   
   
**5.** Press the green push button to run the tool.  
   
   .. warning::  
      
      The user will be informed if a required setting for the run has not been defined by the user.


Load workspace
=============================

* To open a previously saved workspace, navigate to the menu **File** -> **Load Workspace**.

* Select the .json file via the browse window and press "Open".

   .. warning::  
      
      The .json file includes the API version of Snooz (``package_api_version": "1.0.0"``) and all the package dependencies, if any.  Make sure to use a valid workspace for the version of Snooz installed. 


Tools Categories
=============================

.. toctree::
   :maxdepth: 2

   Preprocessing/Preprocessing
   Processing/Processing
   Postprocessing/Postprocessing
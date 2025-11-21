.. _Import_Annotations_from_Text:

==============================
Import Annotations from Text 
==============================

Description
-----------------

Tool to import annotations from a text file (.csv, .tsv, .txt) into the accessory .tsv file used by Snooz.

Steps
-----------------

**1 - Input PSG Files**

PSG files are mandatory, and the only supported format is .edf. The annotation file to be imported must be saved in the same location as the PSG file.

.. warning::
    The annotation file must **not** have the same filename as the PSG file, otherwise Snooz will attempt to load it as a Snooz accessory file.
    To prevent processing errors, please specify a **prefix** and/or **suffix** for the annotation file.
    
Select the PSG files for which you want to import additional annotations. You can select multiple files at once.

**2 - Link PSG and Text file**

Specify how the PSG filename links to the annotation filename using a prefix and suffix. 
Define the file extension of the annotation file—TSV, TXT, and CSV formats are supported.
The annotation file to be imported must be saved in the same location as the PSG file.

**3 - Text File Format**
	
Specify the format of the annotation text file.

**Item separator** - Character used to separate columns in the text file :
 - ``\t`` for tab
 - ``,`` for comma
 - ``;`` for semicolon

**Number of rows to skip** (reserved for the header).

.. warning::
    Do not include blank rows in the count. Do not include the row containing the column titles.

**Time format** - Define the format used for the annotation onset and duration (onset and duration may use different formats). 
The value must represent the elapsed time from the start of the recording:

    - Number of samples (e.g., 15000) the sampling rate must also be specified.
    - Time in seconds (e.g., 300.5).
    - Time in hours, minutes, and seconds (e.g., 00:05:00).

.. note::
    | For time formats using % codes, please refer to the Python strftime directives.
    | For the complete definition see : https://strftime.org/
    
    Examples of string format code for time :
        - %H:%M:%S for 14:30:45
        - %H.%M.%S for 14.30.45
        - %H:%M:%S.%f for 14:30:45.123456
        - %I:%M:%S %p for 02:30:45 PM

File encoding : 
    - UTF-8
    - LATIN-1
    - UTF-16
    - UTF-32
    - ISO-8859
    - ASCII
    - ANSI

**Columns Mapping** - Match the relevant columns from your annotation file to the corresponding Snooz columns listed below :

    - Group : The category of the annotation (annotations with different names can be grouped into the same category), e.g. spindle
    - Name: The text label of the annotation, e.g., spindle_a7
    - Onset : The onset of the annotation
    - Duration : The duration of the annotation
    - Channels : The list of channels on which the annotation occurs, e.g., [C3-A2]

**Output**

Annotations will be appended to the Snooz accessory .tsv file for each corresponding PSG file (named after the PSG file).
Any previously saved annotations in the file with the same group, name, and channels as the new annotations will be deleted before appending the new data.
	
The columns of the Snooz accessory file are as follows:
   1. group : The category of the annotation (annotations with different names can be grouped into the same category), e.g. spindle
   2. name: The text label of the annotation, e.g., spindle_a7
   3. start_sec: The onset of the annotation in seconds, e.g., 300
   4. duration_sec : The duration of the annotation in second, e.g., 0.9
   5. channels : The list of channels on which the annotation occurs, e.g., [C3-A2]

.. _info_PSG_accessory:

=======================================
Snooz PSG File
=======================================

For an introduction to the accepted file format, see :ref:`accepted_format`.

How to read the PSG file?
============================================

Developpers can read PSG file via ``PSGReader`` module from the CEAMSModules package.
The ``PSGReader`` module currently supports three PSG file formats, although only CEAMS users have access to the **NATUS** and **Stellate** formats.
Using the ``PSGReader`` module allows developers to interact with different PSG formats (e.g., .edf, .sig or .eeg) and accessory files (e.g., .tsv, .sts, or .ent) 
with a unified set of methods, providing an abstraction layer for easier integration through the ``PSGReaderManager``.
To be read correctly by tools in the CEAMSTools package, the accessory file must have the same name as the PSG file and be located in the same folder as the PSG file.

PSG Reader Manager
--------------------------

The **NATUS** and **Stellate** formats are proprietary, defined as platform-specific compiled code extensions.  
The **EDF** , however, is open-access and implemented in Python source code. For consistency across formats, method definitions for the **EDF** file format, 
along with other PSG formats, are located in the resources folder within the Snooz architecture repository. 

EdfReader
-----------------

Snooz is configured to load the appropriate compiled code extensions automatically based on the user's operating system.

Snooz architecture repository: ``scinodes_poc``

- Bitbucket Address : https://bitbucket.org/ceamscarsm/scinodes_poc/
- To clone : git@bitbucket.org:ceamscarsm/scinodes_poc.git

**Resources Folder path for the Edf reader**

- Windows : scinodes_poc/src/main/resources/windows/extension/PSGReader
- macOS : scinodes_poc/src/main/resources/mac/extension/PSGReader
- Linux : scinodes_poc/src/main/resources/linux/extension/PSGReader

.. note::

    Developers who wish to add support for additional PSG file formats can add their classes to the appropriate resources folder.

How to read the Snooz accessory .tsv file?
============================================

The recommanded strategy is to use the methods in the ``PSGReaderManager`` class; you can explore the ``PSGReader`` and ``PSGWriter`` modules from the ``CEAMSModules`` package.

You may also access the .tsv file directly and explore examples of how to do this in the ``EventReader``, ``CVSReaderMaster`` and ``TsvWriter`` modules from the ``CEAMSModules`` package.


PSG Reader
--------------------------

Developers may access the annotations using the ``get_events`` method from the class ``PSGReaderManager``, also included in the ``PSGReader`` folder.

The ``PSGReader`` folder includes a ``commons.py`` file that lists the expected labels, such as annotation group or name.

Sleep stages
--------------
Sleep stages are represented by numbers in Snooz:

.. list-table:: 
   :widths: 10 10
   :header-rows: 1

   * - Stage
     - Snooz value
   * - W
     - 0
   * - N1
     - 1
   * - N2
     - 2
   * - N3
     - 3
   * - N4
     - 4
   * - R
     - 5
   * - movement
     - 6
   * - tech
     - 7
   * - unscored
     - 8
   * - undefined
     - 9

TSV reader
--------------------------

Developers may also read the .tsv file directly if the signals are not required.
To read the .tsv file directly, developers can use the ``read_csv`` method from the pandas library. 

pandas.read_csv input parameters:

  - **sep** : ``'\t'``
  - **header** : ``0``
  - **encoding** : ``'utf_8'``

Channel transformation
--------------------------

Be aware that the Snooz accessory file allows annotations to be channel-specific. 
The channels column is defined as a list of channels, and this list can also be empty, indicating that the annotation is not channel-specific.
However, annotations are regenerated in the ``PSGReaderManager`` to ensure that there is a maximum of one channel per annotation, and the format becomes a string instead of a list.
This means that an annotation defined on two channels will be generated as two separate annotations, each corresponding to one channel within Snooz.  
The modules in the CEAMSModules package expect a string for channels in the annnotations, except for the modules responsible for accessing the accessory files, such as ``PSGReader``, ``PSGWriter``, ``EventReader``, ``CVSReaderMaster`` and ``TsvWriter``.
For the modules ``PSGReader`` and ``PSGWriter``, the transformation is managed by the ``PSGReaderManager`` class.
For the modules ``EventReader``, ``CVSReaderMaster`` and ``TsvWriter``, the transformation is handled via the file ``manage_events.py``, included in the ``EventReader`` folder.

If your goal is only to read the .tsv file, modify it, and write it back, there is no need to transform the annotations to be specific to a single channel.

EDFbrowser compatibility
--------------------------

See :ref:`EDFbrowser_compatibility` for instructions on importing Snooz annotations into EDFbrowser.
 
EDFbrowser supports channel-specific annotations, but for this to work, the annotation label (the column name in the Snooz annotation .tsv file) must include the label followed by @@ and then the channel label.

To maintain compatibility with EDFbrowser, we have added the channel label as a suffix to the annotation name using @@. 
This duplication of the channel label from the channels column is not required by tools in the CEAMSTools package and is only necessary for compatibility with EDFbrowser.

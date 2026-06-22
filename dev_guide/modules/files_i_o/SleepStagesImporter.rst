.. _module_sleepstagesimporter:

Sleep Stages Importer
=====================

**Module name:** ``SleepStagesImporter``

**Package:** CEAMSModules 7.4.0

**Version:** 2.1.0

Overview
--------

Class to import sleep stages from a textfile into the sleep_stages dataframe.

Inputs
------

.. list-table::
   :widths: 25 20 15 50
   :header-rows: 1
   :align: left
   :class: left-align-caption wrap-table

   * - Input
     - Format
     - Default
     - Description
   * - ``filename``
     - string
     - —
     - The name of the current PSG file.
   * - ``sleep_stages``
     - Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
     - —
     - Original sleep stages list from the PSG file.
   * - ``stages_files``
     - list
     - —
     - List of path and filename of files with sleep stages to read
   * - ``file_params``
     - dict
     - —
     - | Parameters of the files to read
       | sep : separator of the textfile
       | n_rows_hdr : number of rows to skip in the header
       | encoding : encoding of the textfile (i.e. utf-8)
       | column_stages : column of the textfile containing the sleep stages
       | stages_sec : duration of the sleep stage in seconds in the textfile to read
       | prefix_filename : prefix to insert before the filename to create the stage filename
       | suffix_filename : suffix to append after the filename to create the stage filename
       | case_sensitive : True if the filename\prefix_filename\suffix_filename are case sensitive
       | rename_values : dictionary of values to rename
       | '0' : 'Original awake label'
       | '1' : 'Original N1 label'
       | '2' : 'Original N2 label'
       | '3' : 'Original N3 label'
       | '5' : 'Original REM label'
       | '6' : 'Original movement label'
       | '7' : 'Original tech label'
       | '9' : 'Original unscored label'

Outputs
-------

.. list-table::
   :widths: 25 20 65
   :header-rows: 1
   :align: left
   :class: left-align-caption wrap-table

   * - Output
     - Format
     - Description
   * - ``sleep_stages``
     - TPandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
     - Updated sleep stages list from the textfile.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Sleep Stages Importer** under the **Files I/O** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

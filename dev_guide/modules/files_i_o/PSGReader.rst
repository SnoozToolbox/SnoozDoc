.. _module_psgreader:

PSGReader
=========

**Module name:** ``PSGReader``

**Package:** CEAMSModules 7.4.0

**Version:** 2.5.0

Overview
--------

PSGReader reads a PSG file.

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
   * - ``files``
     - — EDF, STS, Natus
     - — None
     - Each file contains a montage and a list of channel to process.
   * - ``alias``
     - —
     - — None
     - Channels alias to use for this process

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
   * - ``filename``
     - string
     - The name of the current PSG file.
   * - ``signals``
     - List of SignalModel
     - | List of signal with dictionary of channels with SignalModel with
       | properties :
       | name: The name of the channel
       | samples: The samples of the signal
       | alias: The alias of the channel
       | sample_rate: The sample rate of the signal
       | start_time: The start time of the recording
       | montage_index: The index of the montage used for this signal
       | is_modified: Value caracterizing if the signal as been modify
       | from the original
   * - ``events``
     - Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
     - Events list.
   * - ``sleep_stages``
     - Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
     - Sleep stages list.
   * - ``subject_info``
     - dict
     - | filename : Recording filename without path and extension.
       | id1 : Identification 1
       | id2 : Identification 2
       | first_name : first name of the subject recorded
       | last_name : last name of the subject recorded

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **PSGReader** under the **Files I/O** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

.. _module_csvreadermaster:

Csv Reader Master
=================

**Module name:** ``CsvReaderMaster``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

Read events from a CSV file. All index starts at 1.

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
     - List of string
     - —
     - The files to read
   * - ``file_separator``
     - string
     - \t
     - The file separator as '\t' or ','.
   * - ``group_col_i``
     - integer
     - 1
     - The column index of the group
   * - ``name_col_i``
     - integer
     - 2
     - The column index of the event names
   * - ``onset_col_i``
     - integer
     - 3
     - The column index of the onset of the events
   * - ``duration_col_i``
     - integer
     - 4
     - The column index of the duration of the events
   * - ``channels_col_i``
     - integer
     - 5
     - The column index of the channel of the events
   * - ``sample_rate``
     - —
     - 256
     - See module settings for configuration details.
   * - ``input_as_time``
     - Bool
     - 1
     - | If 1, the content of the column are in time (s)
       | if 0, the content are in samples
   * - ``event_center``
     - Bool
     - 0
     - | If 1, the content of the onset is the event center
       | if 0, the content of the onset is the event onset
   * - ``fixed_dur``
     - float
     - —
     - Valide only when duration_col_i==0. The fixed duration of all the events.
   * - ``personnalized_header``
     - bool
     - 0
     - | True to output the header of the event passed in parameters. False to
       | ouput a default header (columns=['group','name','start_sec','duration_sec','channels'])

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
   * - ``events``
     - Pandas DataFrame
     - | List of events (columns=['group','name','start_sec','duration_sec','channels'])
       | OR list of events with personalized columns
   * - ``filename``
     - String
     - Last filename read (or current filename)

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Csv Reader Master** under the **Files I/O** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

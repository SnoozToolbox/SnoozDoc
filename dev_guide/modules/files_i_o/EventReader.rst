.. _module_eventreader:

Event Reader
============

**Module name:** ``EventReader``

**Package:** CEAMSModules 7.4.0

**Version:** 3.0.0

Overview
--------

Read events from a Tsv file

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
     - The filename to read.
   * - ``delimiter``
     - string
     - —
     - Delimiter of the columns.
   * - ``nrows_header``
     - integer
     - 1
     - The number of rows for the header.
   * - ``encoding``
     - string
     - utf_8
     - The file format encoding, default utf_8.
   * - ``group_col_i``
     - integer
     - 1
     - The column index of the group
   * - ``group_def``
     - string
     - —
     - Group event definition if group_col_i=0
   * - ``name_col_i``
     - integer
     - 2
     - The column index of the event names
   * - ``name_def``
     - string
     - —
     - Name event definition if name_col_i=0.
   * - ``onset_col_i``
     - integer
     - 3
     - The column index of the onset of the events (always in elapsed time)
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
   * - ``input_as_onset``
     - string
     - seconds
     - | The specific input for the onset (start_sec) in the annotation file
       | If "seconds", the content are in time (s)
       | if "samples", the content are in samples
       | or any valid datetime string format, see https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
       | ex) "%H:%M:%S%f" for "14:30:45"
       | "%H%M%S%f" for "14:30:45.123456"
   * - ``input_as_dur``
     - string
     - seconds
     - | The specific input for the duration in the annotation file
       | If "seconds", the content are in time (s)
       | if "samples", the content are in samples
       | or any valid datetime string format, see https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
       | ex) "%H:%M:%S%f" for "14:30:45"
       | "%H%M%S%f" for "14:30:45.123456"
   * - ``event_center``
     - Bool
     - 0
     - | If 1, the content of the onset is the event center
       | if 0, the content of the onset is the event onset
   * - ``dur_disable``
     - Bool
     - 0
     - | If 1, the duration is disabled
       | if 0, the content of duration is valid
   * - ``fixed_dur``
     - float
     - —
     - Valide only when dur_disable=1. The fixed duration_col_i of all the events.
   * - ``personalized_header``
     - string of int
     - 0
     - | '1' to read directly the input filename via read_csv and output the pandas datadrame of the file.
       | '0' to convert the filename into snooz dataframe columns=['group','name','start_sec','duration_sec','channels']

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
     - List of events
   * - ``filename``
     - string
     - The input filename is return.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Event Reader** under the **Files I/O** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

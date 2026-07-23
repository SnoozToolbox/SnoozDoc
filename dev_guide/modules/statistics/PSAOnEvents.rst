.. _module_psaonevents:

PSA on Events
=============

**Module name:** ``PSAOnEvents``

**Package:** CEAMSModules 7.5.0

**Version:** 3.0.0

Overview
--------

Compile the PSA run on selected events. The compilation is for a cohort.

Inputs
------

.. list-table::
   :widths: 27 19 15 50
   :header-rows: 1
   :align: left
   :class: left-align-caption wrap-table

   * - Input
     - Format
     - Default
     - Description
   * - ``subject_info``
     - dict
     - —
     - | filename : Recording filename without path and extension.
       | id1 : Identification 1
       | id2 : Identification 2
       | first_name : first name of the subject recorded
       | last_name : last name of the subject recorded
       | ...

   * - ``PSD``
     - list of dicts
     - —
     - | psd : power (µV^2)
       | freq_bins : frequency bins (Hz)
       | win_len : windows length (s)
       | win_step : windows step (s)
       | sample_rate : sampling rate of the original signal (Hz)
       | chan_label : channel label
   * - ``events``
     - pandas dataframe ['group','name','start_sec','duration_sec','channels']
     - —
     - List of events.
   * - ``PSA_event_group``
     - String of dict
     - —
     - A key for each filename and the value is the events group, each group is separated by a comma.
   * - ``PSA_event_name``
     - String of dict
     - —
     - A key for each filename and the value is the events name, each name is separated by a comma.
   * - ``mini_bandwidth``
     - float
     - —
     - The bandwidth of each mini band division (Hz)
   * - ``first_freq``
     - float
     - —
     - The minimum (first) frequency analyzed.
   * - ``artifact_group``
     - String
     - —
     - Event group to ignore, each group is separated by a comma.
   * - ``artifact_name``
     - String
     - —
     - Event name to ignore, each name is separated by a comma.
   * - ``PSA_out_filename``
     - String
     - —
     - Path and filename to write the output.
   * - ``match_event_channels``
     - bool
     - True
     - | True (default): compile each event only on its annotated channel.
       | False: use the event intervals for every analyzed PSD channel.

Outputs
-------

This module has no outputs.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **PSA on Events** under the **Statistics** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

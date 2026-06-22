.. _module_a4preciseevents:

A4Precise Events
================

**Module name:** ``A4PreciseEvents``

**Package:** CEAMSModules 7.4.0

**Version:** 2.0.0

Overview
--------

Precise the A4 spindle events.

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
   * - ``signals``
     - a list of SignalModel
     - —
     - | signal.samples : The actual signal data as numpy list
       | signal.sample_rate : sampling rate of the signal (used to STFT)
       | signal.channel : current channel label
   * - ``events``
     - Pandas DataFrame
     - —
     - | DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])
       | A4 Events detected with a windows length and windows step = 0.25 sec
   * - ``threshold_events``
     - list of float
     - —
     - A threshold value for each event nammed "event_name" from this current detector
   * - ``win_len_sec``
     - Float
     - 0.25
     - The window length in seconds used to compute the RMS value.
   * - ``len_adjust_sec``
     - Float
     - 0.5
     - The window length in seconds to evaluate before and after each event in order to precise the event.
   * - ``min_len_sec``
     - float
     - 0
     - The accepted minimum length in sec (any spindle shorter are discarded)
   * - ``max_len_sec``
     - float
     - 5
     - The accepted maximum length in sec (any spindle longer are discarded)
   * - ``event_group``
     - string
     - —
     - | The event group to limit the length and precise the onset and duration.
       | All the events are selected when event_group is empty.
   * - ``event_name``
     - string
     - —
     - | The event name to limit the length and precise the onset and duration.
       | All the events are selected when event_name is empty.

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
     - | DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])
       | New events with precise onset and duration.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **A4Precise Events** under the **Detectors** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

.. _module_eventsubdivision:

Event Subdivision
=================

**Module name:** ``EventSubdivision``

**Package:** CEAMSModules 7.5.0

**Version:** 1.0.0

Overview
--------

Creates a new pandas DataFrame of events with subwindow of every input event named events_names.

Inputs
------

.. list-table::
   :widths: 17 18 12 53
   :header-rows: 1
   :align: left
   :class: left-align-caption wrap-table

   * - Input
     - Format
     - Default
     - Description
   * - ``events``
     - Pandas DataFrame
     - — 
     - df of events with fields:
        group: Group of events this event is part of (String)
        name: Name of the event (String)
        start_sec: Starting time of the event in sec (Float)
        duration_sec: Duration of the event in sec (Float)
        channels: Channel where the event occures (String)
   * - ``events_names``
     - String
     - —
     - String of the desired events to take in account. Separated by a comma. ex)'stage_2' or ex)'stage_1,stage2,stage3'
       comma. ex)'stage_2' or ex)'stage_1,stage2,stage3'
   * - ``window_sec``
     - Integer
     - —
     - Duration of new subwindow in second. Must be a dividers of previous events.
   * - ``n_window``
     - Integer [Optionnal]
     - —
     - Number of windows in one window.
   * - ``filename``
     - String
     - —
     - The filename of the input recording.

Outputs
-------

.. list-table::
   :widths: 15 20 65
   :header-rows: 1
   :align: left
   :class: left-align-caption wrap-table

   * - Output
     - Format
     - Description
   * - ``new_events``
     - pandas DataFrame
     - df of events with fields:
        group: Group of events this event is part of (String)
        name: Name of the event (String)
        start_sec: Starting time of the event in sec (Float)
        duration_sec: Duration of the event in sec (Float)
        channels: Channel where the event occures (String)

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Event Subdivision** under the **Events Utilities** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

.. _module_signalsfromevents:

Signals From Events
===================

**Module name:** ``SignalsFromEvents``

**Package:** CEAMSModules 7.4.0

**Version:** 3.0.0

Overview
--------

Manage a list of SignalModel from specific events during a recording.

The goal is to extract signals from events (segments : sleep stages or clean segments for analysis). Could also be spindles.

Create a new list of SignalModel based on the events (create = True), otherwise select items from the list of SignalModel based on the events (create = False).

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
     - | Each item of the list is a SignalModel object as described below:
       | signal.samples : The actual signal data as numpy list
       | signal.sample_rate : the sampling rate of the signal
       | signal.channel : current channel label
       | signal.start_time : The start time of the signal in sec
       | signal.end_time : The end time of the signal in sec
       | (for more info : look into common/SignalModel)
   * - ``events``
     - pandas DataFrame
     - —
     - | df of events with field
       | 'group': Group of events this event is part of (String)
       | 'name': Name of the event (String)
       | 'start_sec': Starting time of the event in sec (Float)
       | 'duration_sec': Duration of the event in sec (Float)
       | 'channels' : Channel where the event occures (String)
       | (For now events are expected to be on all channels)
   * - ``events_groups``
     - String
     - —
     - | String of the desired event groups to take in account. Separated by a
       | comma. ex)'group_1' or ex)'group_1,group2,group3'
   * - ``events_names``
     - String
     - —
     - | String of the desired events to take in account. Separated by a
       | comma. ex)'stage_2' or ex)'stage_1,stage2,stage3'
   * - ``create``
     - bool
     - True
     - | True to create a new list of SignalModel based on the events.
       | False to select items from the list of SignalModel based on the events.

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
   * - ``signals_from_events``
     - a list of SignalModel
     - | Each item is a SignalModel based on one item from events.
       | (For now events are expected to be on all channels)
   * - ``epochs_to_process``
     - pandas DataFrame
     - | df of events with field
       | 'group': Group of events this event is part of (String)
       | 'name': Name of the event (String)
       | 'start_sec': Starting time of the event in sec (Float)
       | 'duration_sec': Duration of the event in sec (Float)
       | 'channels' : Channel where the event occures (String)

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Signals From Events** under the **Events Utilities** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

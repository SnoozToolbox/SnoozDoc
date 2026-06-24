.. _module_sleepstageevents:

Sleep Stage Events
==================

**Module name:** ``SleepStageEvents``

**Package:** CEAMSModules 7.5.0

**Version:** 2.1.0

Overview
--------

Create a list of event from specific sleep stages during a recording.

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
   * - ``epoch_len``
     - double
     - —
     - The epoch length in second (only required for sleep_stages as array)
   * - ``sleep_stages``
     - array or pandas DataFrame
     - —
     - | A sleep stage per epoch (an array of stages from 0-9). Valid values are :
       | 0 = Wake
       | 1 = Stage 1
       | 2 = Stage 2
       | 3 = Stage 3
       | 4 = Stage 4
       | 5 = REM
       | 6 = Movement time
       | 7 = Technical time
       | 9 = undetermined
       | pandas DataFrame of events with field
       | 'group': Group of events this event is part of (String)
       | 'name': Name of the event (String)
       | 'start_sec': Starting time of the event in sec (Float)
       | 'duration_sec': Duration of the event in sec (Float)
       | 'channels' : Channel where the event occures (String)
   * - ``stages``
     - string
     - —
     - | A string of each sleep stage separeted by a comma with the same
       | valid values as sleep_stages. Example : '1,4,5,7'
   * - ``merge_events``
     - String
     - 0
     - 1 to merge selected continuous events, 0 to let them in epochs.
   * - ``new_event_name``
     - string (optional)
     - —
     - To rename selected event. The original name is kept if let blank.
   * - ``exclude_nremp``
     - —
     - 0
     - See module settings for configuration details.
   * - ``exclude_remp``
     - —
     - 0
     - See module settings for configuration details.
   * - ``in_cycle``
     - String
     - 0
     - | '1' to keep only events inluded in the sleep cycles.
       | '0' do not use sleep cycles information.

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
   * - ``sleep_stage_events``
     - pandas DataFrame
     - List of events from specific stages

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Sleep Stage Events** under the **Events Utilities** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

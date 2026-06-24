.. _module_oxygendesatdetector:

Oxygen Desaturation Detector
============================

**Module name:** ``OxygenDesatDetector``

**Package:** CEAMSModules 7.5.0

**Version:** 2.5.0

Overview
--------

A Class to analyze the oxygen channel, detect oxygen desaturations and export oxygen saturation report. To copy the previous software, the oxygen saturation channel is downsampled to 1 Hz.

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
   * - ``artifact_group``
     - String
     - —
     - The group label of the invalid section annotation for the oxy chan analysis.
   * - ``artifact_name``
     - String
     - —
     - The name label of the invalid section annotation for the oxy chan analysis.
   * - ``arousal_group``
     - String
     - —
     - | The group label of the arousal annotations for temporal link analysis.
       | (Obsolete, the feature was removed 2024-01-30, not robust)
   * - ``arousal_name``
     - String
     - —
     - | The name label of the arousal annotations for temporal link analysis.
       | (Obsolete, the feature was removed 2024-01-30, not robust)
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
       | (within Snooz channels is a string of a single channel or [] for all channels)
   * - ``stages_cycles``
     - Pandas Dataframe ['group','name','start_sec','duration_sec','channels']
     - —
     - | Events defined as (columns=['group', 'name','start_sec','duration_sec','channels'])
       | The sleep stage group has to be commons.sleep_stage_group "stage" and
       | the sleep cycle group has to be commons.sleep_cycle_group "cycle".
   * - ``subject_info``
     - dict
     - —
     - | filename : Recording filename without path and extension.
       | id1 : Identification 1
       | id2 : Identification 2
       | first_name : first name of the subject recorded
       | last_name : last name of the subject recorded
       | sex :
       | ...
   * - ``parameters_oxy``
     - dict
     - {'desaturation_drop_percent': 3, 'max_slope_drop_sec': 120, 'min_hold_drop_sec': 10}
     - | 'desaturation_drop_percent' : 'Drop level (%) for the oxygen desaturation "3 or 4"',
       | 'max_slope_drop_sec' : 'The maximum duration (s) during which the oxygen level is dropping "120 or 20"',
       | 'min_hold_drop_sec' : 'Minimum duration (s) during which the oxygen level drop is maintained "10 or 5"',
   * - ``parameters_cycle``
     - Dict
     - —
     - | Options used to define the cycles
       | "{
       | 'defined_option':'Minimum Criteria'
       | 'Include_SOREMP' : '1'
       | 'Include_last_incompl' : '1'
       | 'Include_all_incompl: : '1'
       | 'dur_ends_REMP' = '15'
       | 'NREM_min_len_first':'0'
       | 'NREM_min_len_mid_last':'15'
       | 'NREM_min_len_val_last':'0'
       | 'REM_min_len_first':'0'
       | 'REM_min_len_mid':'0'
       | 'REM_min_len_last':'0'
       | 'mv_end_REMP':'0'
       | 'sleep_stages':'N1, N2, N3, N4, R'
       | 'details': '<p>Adjust options based on minimum criteria.</p>
       | }"
   * - ``report_constants``
     - dict
     - {}
     - Constants used in the report (N_HOURS, N_CYCLES)
   * - ``cohort_filename``
     - String
     - —
     - Path and filename to save the oxygen saturation report for the cohort.
   * - ``picture_dir``
     - String
     - —
     - | Directory path to save the oxygen saturation graph picture.
       | One graph per recording (1 picture per discontinuity).

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
   * - ``desat_events``
     - pandas DataFrame
     - | df of events with field
       | 'group': Group of events this event is part of (String)
       | 'name': Name of the event (String)
       | 'start_sec': Starting time of the event in sec (Float)
       | 'duration_sec': Duration of the event in sec (Float)
       | 'channels' : Channel where the event occures (String)
       | (within Snooz channels is a string of a single channel or [] for all channels)

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Oxygen Desaturation Detector** under the **Detectors** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

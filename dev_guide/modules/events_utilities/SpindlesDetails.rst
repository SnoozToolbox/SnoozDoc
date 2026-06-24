.. _module_spindlesdetails:

Spindles Details
================

**Module name:** ``SpindlesDetails``

**Package:** CEAMSModules 7.5.0

**Version:** 2.2.0

Overview
--------

To compute events characteristics such as duration, amplitude, frequency and so on.

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
   * - ``recording_path``
     - string
     - —
     - The recording path.
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
   * - ``spindle_events``
     - Pandas DataFrame
     - —
     - | Spindle events defined as (columns=['group', 'name','start_sec','duration_sec','channels'])
       | The group has to be commons.sleep_spindle_group (spindle)
   * - ``stages_cycles``
     - Pandas DataFrame
     - —
     - | Spindle events defined as (columns=['group', 'name','start_sec','duration_sec','channels'])
       | The sleep stage group has to be commons.sleep_stage_group (stage) and
       | the sleep cycle group has to be commons.sleep_cycle_group (cycle)
   * - ``artifact_events``
     - Pandas DataFrame
     - —
     - | Artifact events defined as (columns=['group', 'name','start_sec','duration_sec','channels'])
       | Artifacts that disable the spindle detection.
   * - ``sleep_cycle_param``
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
   * - ``spindle_gen_param``
     - Dict
     - —
     - | Options used to detect spindles
       | "{
       | 'min_duration': 0.5
       | 'max_duration': 2.5
       | 'sleep_stage_sel' : [2,3]
       | 'in_cycle: : 1
       | 'exclude_nremp' : 0
       | 'exclude_remp' : 1
       | }
   * - ``spindle_sel_param``
     - Dict
     - —
     - | Options specific to the det selected
       | "{
       | -> Martin a4
       | 'spindle_name' : a4
       | 'threshold' : 0.95
       | 'threshold_per_cycle' : 1
       | 'precision_on' : 1
       | -> Lacourse A7
       | 'spindle_name' : a7
       | 'thresh_abs_sigma_pow_uv2' : 1.25
       | 'thresh_rel_sigma_pow_z' : 1.6
       | 'thresh_sigma_cov_z' : 1.3
       | 'thresh_sigma_cor_perc' : 69
       | -> SUMO
       | 'spindle_name' : sumo
       | }"
   * - ``report_constants``
     - dict
     - {'N_HOURS': 9, 'N_CYCLES': 6}
     - Constants used in the report (N_HOURS, N_CYCLES)
   * - ``cohort_filename``
     - String
     - —
     - Path and filename to save the spindle characteristics for the cohort.
   * - ``export_spindles``
     - bool
     - False
     - True : generate a file per subject of the characteristics of each spindle.

Outputs
-------

This module has no outputs.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Spindles Details** under the **Events Utilities** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

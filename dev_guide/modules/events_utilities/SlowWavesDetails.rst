.. _module_slowwavesdetails:

Slow Waves Details
==================

**Module name:** ``SlowWavesDetails``

**Package:** CEAMSModules 7.4.0

**Version:** 2.2.0

Overview
--------

To average slow wave events characteristics such as duration, amplitude, frequency and so on per stage and sleep cycle.

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
   * - ``sw_events_details``
     - Pandas DataFrame
     - —
     - Slow wave events defined as (columns=['group', 'name', 'start_sec','pkpk_amp_uV','neg_amp_uV','neg_sec','pos_sec','Pap_raw','Neg_raw','mfr','trans_freq_Hz', 'channels'])
   * - ``artifact_events``
     - Pandas DataFrame
     - —
     - | Artifact events defined as (columns=['group', 'name','start_sec','duration_sec','channels'])
       | Artifacts are forced to zeros for the detection (with a tukey window)
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
   * - ``stages_cycles``
     - Pandas DataFrame
     - —
     - | Events defined as (columns=['group', 'name','start_sec','duration_sec','channels'])
       | The sleep stage group has to be commons.sleep_stage_group "stage" and
       | the sleep cycle group has to be commons.sleep_cycle_group "cycle".
   * - ``slow_wave_det_param``
     - Dict
     - —
     - | stage_sel : Sleep stages selection to detect slow waves in.
       | detect_excl_remp : Flag to exclude rem period from the spindle detection.
       | sw_event_name : String label of the event name
       | filt_low_hz : Low frequency bandpass filter (Hz)
       | filt_high_hz : High frequency bandpass filter (Hz)
       | min_amp_pk-pk_uV : minimum peak-to-peak amplitude (uV)
       | min_neg_amp_uV : minimum negative amplitude (uV)
       | min_dur_neg_ms : minimum duration of negative part of the slow wave (ms)
       | max_dur_neg_ms : maximum duration of negative part of the slow wave (ms)
       | min_dur_pos_ms : minimum duration of positive part of the slow wave (ms)
       | max_dur_pos_ms : maximum duration of positive part of the slow wave (ms)
   * - ``report_constants``
     - dict
     - {}
     - Constants used in the report (N_HOURS, N_CYCLES)
   * - ``cohort_filename``
     - string
     - —
     - Path and filename to save the slow wave characteristics for the cohort.
   * - ``export_slow_wave``
     - bool or string
     - False
     - True : generate a file per subject of the characteristics of each slow wave.

Outputs
-------

This module has no outputs.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Slow Waves Details** under the **Events Utilities** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

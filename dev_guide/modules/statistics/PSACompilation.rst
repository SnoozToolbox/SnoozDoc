.. _module_psacompilation:

PSA Compilation
===============

**Module name:** ``PSACompilation``

**Package:** CEAMSModules 7.5.0

**Version:** 2.2.0

Overview
--------

Class to analyse and report the PSD output. Average the PSD per channel, stage, cycle, hour... Append all subjects in the same output file.

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
     - Pandas Dataframe ['group','name','start_sec','duration_sec','channels']
     - —
     - List of events.
   * - ``sleep_stages``
     - Pandas Dataframe ['group','name','start_sec','duration_sec','channels']
     - —
     - List of sleep stages that match the PSD input. Sleep stages selected to analyse the spectral power.
   * - ``mini_bandwidth``
     - float
     - 0.5
     - The bandwidth of eah mini band division (Hz)
   * - ``first_freq``
     - float
     - 0
     - The minimum (first) frequency analyzed.
   * - ``last_freq``
     - float
     - 64
     - | The maximum (last) frequency analysed.
       | ! Warning : the last frequency is limited to fs/2
   * - ``dist_total``
     - bool
     - 1
     - True to write the total spectral activity.
   * - ``dist_hour``
     - bool
     - 1
     - True to write the spectral activity per hour.
   * - ``dist_cycle``
     - bool
     - 1
     - True to write the spectral activity per cycle.
   * - ``parameters_cycle``
     - String (dict converted into a string)
     - —
     - | "{
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
   * - ``artefact_group``
     - String
     - —
     - Event group to ignore, each group is separated by a comma.
   * - ``artefact_name``
     - String
     - —
     - Event name to ignore, each name is separated by a comma.
   * - ``cycle_labelled``
     - pandas DataFrame
     - —
     - | List of NREM and REM periods (columns=['group','name','start_sec','duration_sec','channels'])
       | where the group is the recording filename.
   * - ``report_constants``
     - dict
     - {}
     - Constants used in the report (N_HOURS, N_CYCLES)
   * - ``filename``
     - string
     - —
     - Path and filename to write the output.

Outputs
-------

This module has no outputs.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **PSA Compilation** under the **Statistics** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

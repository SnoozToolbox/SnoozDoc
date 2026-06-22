.. _module_sleepcyclesdelimiter:

Sleep Cycles Delimiter
======================

**Module name:** ``SleepCyclesDelimiter``

**Package:** CEAMSModules 7.4.0

**Version:** 2.4.0

Overview
--------

Compute the sleep cycles. Creates and appends events with group: "cycles" and name: "cycle number" ex.1.

Cycle definition: The cycle starts with a nrem period. The nrem period ends with a rem stage. The rem period ends when there is 15 mins without a rem stage. The end of the rem period is updated to the last rem stage or the start of the following nrem period.

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
   * - ``events_in``
     - pandas DataFrame
     - —
     - | List of events, including sleep stages (columns=['group','name','start_sec','duration_sec','channels']).
   * - ``parameters``
     - dict
     - None
     - | Dictionary of options to define the cycles.
       | {'defined_option': 'Minimum Criteria'
       | 'Include_SOREMP' : '1'
       | 'Include_last_incompl' : '1'
       | 'Include_all_incompl' : '1'
       | 'dur_ends_REMP' : '15'
       | 'NREM_min_len_first': '0'
       | 'NREM_min_len_mid_last': '15'
       | 'NREM_min_len_val_last': '0'
       | 'REM_min_len_first': '0'
       | 'REM_min_len_mid': '0'
       | 'REM_min_len_last': '0'
       | 'mv_end_REMP': '0'
       | 'sleep_stages': 'N1, N2, N3, R'
       | 'details': 'Adjust options based on minimum criteria.'}
   * - ``label``
     - string
     - None
     - Label to identify the current recording

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
   * - ``events_out``
     - pandas DataFrame
     - List of events (columns=['group','name','start_sec','duration_sec','channels'])
   * - ``parameters_cycle``
     - Dict
     - | Options used to define the cycles
       | {'defined_option':'Minimum Criteria'
       | 'defined_option':'Minimum Criteria'
       | 'Include_SOREMP' : '1'
       | 'Include_last_incompl' : '1'
       | 'Include_all_incompl: : '1'
       | 'dur_ends_REMP' : '15'
       | 'NREM_min_len_first':'0'
       | 'NREM_min_len_mid_last':'15'
       | 'NREM_min_len_val_last':'0'
       | 'REM_min_len_first':'0'
       | 'REM_min_len_mid':'0'
       | 'REM_min_len_last':'0'
       | 'mv_end_REMP':'0'
       | 'sleep_stages':'N1, N2, N3, R'
       | 'details': 'Adjust options based on minimum criteria.'}
   * - ``sleep_cycles_epoch``
     - list
     - | The list of sleep cycle in epoch (one cycle per row).
       | Epoch start and end are inclusive and start to 0.
       | [((NREM start, NREM stop),(REM start, REM stop))\
       | ((NREM start, NREM stop),(REM start, REM stop))\
       | ...]
   * - ``REM_period_epoch``
     - list
     - | The list of REM period in epoch (one cycle per row).
       | Epoch start and end are inclusive and start to 0.
       | [(REM start, REM stop))\
       | ((REM start, REM stop))\
       | ...]
   * - ``cycle_labelled``
     - pandas DataFrame
     - | List of NREM and REM periods (columns=['group','name','start_sec','duration_sec','channels'])
       | where the group is the input label.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Sleep Cycles Delimiter** under the **Hypnogram Analysis** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

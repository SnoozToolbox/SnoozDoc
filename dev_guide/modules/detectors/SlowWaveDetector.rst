.. _module_slowwavedetector:

Slow Wave Detector
==================

**Module name:** ``SlowWaveDetector``

**Package:** CEAMSModules 7.4.0

**Version:** 2.3.0

Overview
--------

This plugin detects slow wave events based on multiple criterias such as Carrier's, sex and / or age of subject. The plugin also keeps in memory the caracteristics of the slow wave, including the transition frequency of the wave in order to eventually classify the slow waves collected. To assure best results, the detector keeps only 30 s or + epochs. If epochs aren't the same size, the detector reformats the signal and keeps only 30 s segments.

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
     - | signal.samples : the actual signal data as numpy list
       | signal.sample_rate : sampling rate of the signal
       | signal.channel : current channel label
   * - ``event_group``
     - String, event group.
     - ssw_carrier
     - String, event group.
   * - ``event_name``
     - String, event label.
     - —
     - String, event label.
   * - ``f_min``
     - float, minimal wave frequency
     - 0.16
     - float, minimal wave frequency
   * - ``f_max``
     - float, maximal wave frequency
     - 4
     - float, maximal wave frequency
   * - ``th_PaP``
     - float, peak-to-peak minimal amplitude
     - 75
     - float, peak-to-peak minimal amplitude
   * - ``th_Neg``
     - float, negative minimal amplitude
     - 40
     - float, negative minimal amplitude
   * - ``min_tNe``
     - int, minimal duration of negative part of the slow wave
     - 125
     - int, minimal duration of negative part of the slow wave
   * - ``max_tNe``
     - int, maximal duration of negative part of the slow wave
     - 1500
     - int, maximal duration of negative part of the slow wave
   * - ``min_tPo``
     - int, minimal duration of positive part of the slow wave
     - 0
     - int, minimal duration of positive part of the slow wave
   * - ``max_tPo``
     - int, maximal duration of positive part of the slow wave
     - 1000
     - int, maximal duration of positive part of the slow wave
   * - ``age_criterion``
     - String, '1' or '0'
     - 0
     - | '1' to modify criterias according to age
       | '0' to keep criterias as they are
   * - ``years``
     - int, 0 to 122
     - 0
     - int, 0 to 122
   * - ``months``
     - int, 0 to 11
     - 0
     - int, 0 to 11
   * - ``sex_criterion``
     - String, '1' or '0'
     - 0
     - | '1' to modify criterias according to sex
       | '0' to keep criterias as they are
   * - ``sex``
     - String, 'Female' or 'Male'
     - Female
     - String, 'Female' or 'Male'

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
       | containing a slow wave event
   * - ``events_details``
     - Pandas DataFrame
     - | DataFrame events (columns=['start_sec', 'duration_sec', 'n_t','pkpk_amp_uV','neg_amp_uV', 'neg_sec', 'pos_sec', 'Pap_raw', 'Neg_raw', 'mfr', 'trans_freq_Hz', 'slope_0_min', 'slope_min_max', 'slope_max_0', 'channels','name'])
       | containing data of each detected slow wave for further analysis

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Slow Wave Detector** under the **Detectors** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

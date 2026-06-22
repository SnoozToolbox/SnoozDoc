.. _module_amplitudedetector:

Amplitude Detector
==================

**Module name:** ``AmplitudeDetector``

**Package:** CEAMSModules 7.4.0

**Version:** 2.0.0

Overview
--------

This plugin detects events based on the absolute signal amplitude. The plugin is flexible, an event can be detected when activity goes above or below the threshold. The threshold can be fixed or adaptive based on a baseline window around the event. The adaptive threshold can be x times the baseline median value or x times the standard deviation of the baseline. When a z-score is used as threshold (x BSL STD), the absolute signal amplitude can be log10 transformed to make them more normally distributed.

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
   * - ``event_group``
     - string, event group.
     - —
     - string, event group.
   * - ``event_name``
     - string, event label.
     - —
     - string, event label.
   * - ``pad_sec``
     - string
     - 0.5
     - | The padding event (length in second) to add to the beginning and
       | the end of the originally detected event.
   * - ``threshold_val``
     - string or a list of float
     - —
     - | String : the value to threshold to detect events.
       | list : the value to threshold for each signal included in signals.
   * - ``threshold_unit``
     - string
     - fixed
     - The threshold unit (fixed, x BSL median, x BSL STD or x BSL STD(log10)).
   * - ``threshold_behavior``
     - string
     - Above
     - | Above : Event is detected when activity goes above the threshold.
       | Below : Event is detected when activity goes below the threshold.
   * - ``baseline_win_len``
     - string
     - —
     - (optional) The baseline window length in seconds
   * - ``art_events``
     - Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
     - —
     - (optional) Artefact events previously detected
   * - ``channel_dbg``
     - string
     - None
     - Channel label to save and exit detection info.

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
     - DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])
   * - ``det_activity``
     - list of ndarray of n_windows
     - | An array per item of the list signals.
       | An array is the absolute signal amplitude or the std amplitude value relative to the baseline.
   * - ``bsl_activity``
     - list of ndarray of n_windows
     - | An array per item of the list signals.
       | (Optional) Median\STD amplitude of the baseline window.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Amplitude Detector** under the **Detectors** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

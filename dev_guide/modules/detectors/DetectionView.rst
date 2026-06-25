.. _module_detectionview:

Detection View
==============

**Module name:** ``DetectionView``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

This plugin organizes detection information and saves it into the cache in order to plot it. Helpfil to degub detector.

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
   * - ``time_elapsed``
     - string "HH:MM:S.S"
     - 00:00:00
     - Time elapsed since the beginning of the recording to show.
   * - ``win_len_show``
     - double
     - 30
     - Window length in sec to show.
   * - ``signals``
     - a list of SignalModel
     - —
     - | signal.samples : The actual signal data as numpy list
       | signal.sample_rate : the original sampling rate of the signal
       | signal.channel : current channel label
   * - ``event_name``
     - string
     - —
     - Event label selected for display
   * - ``channel``
     - string
     - —
     - Channel label selected for display
   * - ``win_step_sec``
     - float
     - —
     - Window step in sec (each time the fft is applied)
   * - ``events``
     - Pandas DataFrame
     - —
     - DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])
   * - ``win_activity``
     - list of ndarray of n_windows
     - —
     - | Each item correspond to an item of signals for the selected channel to display
       | Spectral power in the frequency bins from low_freq to high_freq.
   * - ``threshold``
     - list of double
     - —
     - | Each item correspond to an item of signals for the selected channel to display
       | The threshold to detect events.
   * - ``threshold_unit``
     - string
     - fixed
     - The threshold unit (fixed, x BSL median or x BSL STD).
   * - ``filename``
     - string
     - —
     - Python filename to save data to display an additional detection window.
   * - ``win_bsl``
     - list of ndarray of n_windows (or [2 x n_windows])
     - —
     - | Each item correspond to an item of signals for the selected channel to display
       | median_use==True : Median spectral power of the baseline window
       | median_use==False : Mean and standard deviation of the baseline
       | spectral power (row1: mean, row2: std).

Outputs
-------

This module has no outputs.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Detection View** under the **Detectors** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

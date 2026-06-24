.. _module_windowstosamples:

Windows To Samples
==================

**Module name:** ``WindowsToSamples``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

To convert information based on windows (i.e. RMS energy) into a time series (i.e. RMS values synchronized - aligned with the eeg signal). If the step window used to compute the information is longer than 1/sampling rate the window value is replicated along windows step length to match the sampling rate of the signal in input.

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
   * - ``signals_windows``
     - list of SignalModel
     - —
     - | signal_windows.samples : The actual windows data as array.
       | signal.sample_rate : the original sampling rate of the signal
       | signal.channel : current channel label
   * - ``win_step_sec``
     - Float
     - —
     - The window step length in seconds used to compute the information signals_windows.

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
   * - ``samples_values``
     - dict of SignalModel, the key is the label of the channel.
     - samples_values[channel_label].samples : The actual samples values as array

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Windows To Samples** under the **Events Utilities** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

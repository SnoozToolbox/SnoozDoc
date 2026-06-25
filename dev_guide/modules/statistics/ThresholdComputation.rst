.. _module_thresholdcomputation:

Threshold Computation
=====================

**Module name:** ``ThresholdComputation``

**Package:** CEAMSModules 7.4.0

**Version:** 2.1.0

Overview
--------

To compute the value to threshold (i.e. µV) from a signals (i.e. EEG time series) based on a threshold definition (i.e. 4) and a metric or a unit (i.e. standard deviation).

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
     - dict of SignalModel, the key is the label of the channel.
     - —
     - signals[channel_label].samples : The actual signal data as numpy list
   * - ``cycle_events``
     - pandas DataFrame
     - —
     - | Events (columns=['group','name','start_sec','duration_sec','channels'])
       | Sleep cycles are defined with the 'group' cycle and the 'name' nremp or remp
   * - ``threshold_definition``
     - float
     - —
     - threshold definition to compute the value from the signals
   * - ``threshold_metric``
     - String
     - standard deviation
     - | Metric (unit) used for thresholding.
       | "percentile", "standard deviation", "variance" or "median"
   * - ``threshold_scope``
     - String
     - 0
     - | '0' to compute a threshold per item of signals
       | '1' to compute a threshold per sleep cycle and channel
       | '2' to compute a threshold per channel (through all signals).

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
   * - ``threshold_value``
     - list of float
     - | The value to threshold for each signal included in signals.
       | (Can vary for each item of signals depending of the threshold_scope.)

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Threshold Computation** under the **Statistics** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

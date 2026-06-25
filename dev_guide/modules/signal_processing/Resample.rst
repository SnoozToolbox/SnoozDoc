.. _module_resample:

Resample
========

**Module name:** ``Resample``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

This class resamples a signal.

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
       | signal.sample_rate : the original sampling rate of the signal
       | signal.channel : current channel label
   * - ``sample_rate``
     - float
     - —
     - The wanted sampling rate
   * - ``upsample``
     - str (bool)
     - True
     - | Flag to allow upsampling.
       | If False, the resampled data is never upsampled, the original sampling rate is kept.

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
   * - ``signals``
     - a list of SignalModel
     - | signal.samples : The actual signal data as numpy list
       | signal.sample_rate : the new sampling rate of the signal
       | signal.channel : current channel label

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Resample** under the **Signal Processing** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

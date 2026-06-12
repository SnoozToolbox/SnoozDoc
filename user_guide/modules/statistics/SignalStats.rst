.. _module_signalstats:

Signal Stats
============

**Module name:** ``SignalStats``

**Package:** CEAMSModules 7.4.0

**Version:** 2.0.0

Overview
--------

Compute the mean and standard deviation of the input signals per epoch, per channel. 

.. note:: For each epoch (each item in the `SignalModel` list), the module calculates the mean and standard deviation. The module accepts NaN values in the signals and will ignore them in the calculations.

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
     - List of SignalModel
     - —
     - | List of signal with dictionary of channels with SignalModel with properties :
       | name: The name of the channel
       | samples: The samples of the signal
       | alias: The alias of the channel
       | sample_rate: The sample rate of the signal
       | start_time: The start time of the recording
       | montage_index: The index of the montage used for this signal
       | is_modified: Value characterizing if the signal has been modified from the original

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
   * - ``stats``
     - dict
     - | A dictionary containing statistical properties of the signals.
       | - 'mean': List of mean values computed from the input signals.
       | - 'std': List of standard deviation values computed from the input signals.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Signal Stats** under the **Statistics** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

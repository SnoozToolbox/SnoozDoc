.. _module_epochsignal:

Epoch Signal
============

**Module name:** ``EpochSignal``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

No description available.

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
     - list
     - None
     - list of SignalModel
   * - ``events``
     - pandas.DataFrame
     - None
     - The events to use to segment the signals into epochs.
   * - ``epoch_length_sec``
     - float or str
     - None
     - The length of the epochs in seconds.
   * - ``overlap_sec``
     - float or str
     - None
     - The overlap between epochs in seconds.
   * - ``droplast``
     - bool or str
     - None
     - Whether to discard the last segment if it is not of the same length as the other segments.

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
   * - ``epochs``
     - list of EpochModel
     - The epochs of the signals. (One per channel)
   * - ``events``
     - pandas.DataFrame
     - The events used to segment the signals into epochs. (One row per epoch)

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Epoch Signal** under the **Signal Processing** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

.. _module_wpliconnectivity:

Wpli Connectivity
=================

**Module name:** ``WpliConnectivity``

**Package:** CEAMSModules 7.5.0

**Version:** 2.1.0

Overview
--------

This node computes corrected Weighted Phase Lag Index (wPLI) connectivity from EEG epochs.

Workflow
^^^^^^^^

#. Stack input epochs into a 3D array with shape (num_epochs, num_channels, num_samples).
#. Remove artifact windows by dropping any epoch that contains NaNs (across all channels/samples).
#. For each remaining epoch, compute wPLI between all channel pairs using the analytic (Hilbert) signal.
#. Build a null distribution via time-shift (lag) surrogates and apply a Wilcoxon test: keep (real wPLI − median(surrogates)) if p < p_value and real > median; otherwise set 0.
#. Return the per-epoch corrected wPLI and the average across epochs, along with channel names.

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
   * - ``epochs``
     - list[EpochModel]
     - —
     - Each EpochModel has .samples (2D array W×T: epochs × samples), .sample_rate, .channel.
   * - ``events``
     - pandas.DataFrame
     - —
     - Present for interface consistency; not used by the computation here.
   * - ``num_surr``
     - int
     - 20
     - Number of time-shift surrogates for correction.
   * - ``p_value``
     - float
     - 0.05
     - Significance threshold for the Wilcoxon signed-rank test.

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
   * - ``wpli_results``
     - dict
     - | {
       | "final_wpli": (num_epochs_kept, C, C) array of corrected wPLI per epoch,
       | "average_wpli": (C, C) array = mean over kept epochs,
       | "channel_names": list[str] of channel labels
       | }

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Wpli Connectivity** under the **Connectivity Analysis** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

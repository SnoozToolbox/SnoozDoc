.. _module_dpliconnectivity:

Dpli Connectivity
=================

**Module name:** ``DpliConnectivity``

**Package:** CEAMSModules 7.4.0

**Version:** 2.1.0

Overview
--------

This node computes corrected Directed Phase Lag Index (dPLI) connectivity from EEG epochs.

Workflow
^^^^^^^^

#. Stack input epochs into a 3D array with shape (num_epochs, num_channels, num_samples).
#. Treat non-finite values (NaN/Inf) as artifacts; convert to NaN so they can be dropped.
#. Remove artifact windows by dropping any epoch that contains NaN or zeros (across any channel/sample).
#. For each remaining epoch, compute dPLI between all channel pairs using Hilbert phase.
#. Build a null distribution via per-channel time-shift surrogates and apply a Wilcoxon test: apply the “gap + 0.5” correction logic when p < p_value; otherwise leave at 0.5 baseline.
#. Return the per-epoch corrected dPLI and the average across epochs, along with channel names.

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
   * - ``dpli_results``
     - dict
     - | {
       | "final_dpli": (num_epochs_kept, C, C) array of corrected dPLI per epoch,
       | "average_dpli": (C, C) array = mean over kept epochs,
       | "channel_names": list[str] of channel labels
       | }

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Dpli Connectivity** under the **Connectivity Analysis** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

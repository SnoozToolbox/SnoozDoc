.. _module_rescalesignal:

Rescale Signal
==============

**Module name:** ``RescaleSignal``

**Package:** CEAMSModules 7.5.0

**Version:** 2.1.0

Overview
--------

Create a list of dictionnaries with the channels (each of them are SignalModel) from specific epochs during a recording. Each signal is rescale according to a specific approach.

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
     - List
     - —
     - | List of signal with dictionary of channels with SignalModel with
       | properties :
       | name: The name of the channel
       | samples: The samples of the signal
       | alias: The alias of the channel
       | sample_rate: The sample rate of the signal
       | start_time: The start time of the recording
       | montage_index: The index of the montage used for this signal
       | is_modified: Value caracterizing if the signal as been modify
       | from the original
   * - ``scaling_approach``
     - String
     - —
     - | String of the desired scaling approach to rescale signals.
       | parameters : Dict
       | Dictionnary of all the parameters associated with the scaling
       | approach.
   * - ``parameters``
     - —
     - —
     - See module settings for configuration details.

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
   * - ``signals_rescale``
     - List
     - | List of Dict containing channel with SignalModel where the signal
       | have been rescale.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Rescale Signal** under the **Signal Processing** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

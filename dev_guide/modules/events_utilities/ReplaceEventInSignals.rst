.. _module_replaceeventinsignals:

Replace Event In Signals
========================

**Module name:** ``ReplaceEventInSignals``

**Package:** CEAMSModules 7.5.0

**Version:** 2.1.0

Overview
--------

Insert samples from event dataframe inside a signals.

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
     - | List of SignalModel with properties :
       | name: The name of the channel
       | samples: The samples of the signal
       | alias: The alias of the channel
       | sample_rate: The sample rate of the signal
       | start_time: The start time of the recording
       | montage_index: The index of the montage used for this signal
       | is_modified: Value caracterizing if the signal as been modify
       | from the original
   * - ``signals_events``
     - List
     - —
     - | List of signals from events with dictionary of channels.
       | These channels are SignalModel with properties :
       | name: The name of the channel
       | samples: The samples of the signal
       | alias: The alias of the channel
       | sample_rate: The sample rate of the signal
       | start_time: The start time of the recording
       | montage_index: The index of the montage used for this signal
       | is_modified: Value caracterizing if the signal as been modify
       | from the original

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
   * - ``new_signals``
     - signals : List
     - | List of SignalModel with properties :
       | name: The name of the channel
       | samples: The samples of the signal
       | alias: The alias of the channel
       | sample_rate: The sample rate of the signal
       | start_time: The start time of the recording
       | montage_index: The index of the montage used for this signal
       | is_modified: Value caracterizing if the signal as been modify
       | from the original

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Replace Event In Signals** under the **Events Utilities** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

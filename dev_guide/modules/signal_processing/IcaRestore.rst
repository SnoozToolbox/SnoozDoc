.. _module_icarestore:

Ica Restore
===========

**Module name:** ``IcaRestore``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

Reconstruct Signal from ICA components.

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
     - | List of signals put in IcaComponents with dictionary of channels.
       | These channels are SignalModel with properties :
       | name: The name of the channel
       | samples: The samples of the signal
       | alias: The alias of the channel
       | sample_rate: The sample rate of the signal
       | start_time: The start time of the recording
       | montage_index: The index of the montage used for this signal
       | is_modified: Value caracterizing if the signal as been modify
       | from the original
   * - ``components``
     - List
     - —
     - | List of componants with dictionary of channels. These channels are
       | SignalModel with properties :
       | name: The name of the channel
       | samples: The samples of the signal
       | alias: The alias of the channel
       | sample_rate: The sample rate of the signal
       | start_time: The start time of the recording
       | montage_index: The index of the montage used for this signal
       | is_modified: Value caracterizing if the signal as been modify
       | from the original
   * - ``epochs_to_process``
     - pandas DataFrame
     - —
     - | df of epochs with field
       | 'group': Group of events this event is part of (String)
       | 'name': Name of the event (String)
       | 'start_sec': Starting time of the event in sec (Float)
       | 'duration_sec': Duration of the event in sec (Float)
       | 'channels' : Channel where the event occures (String)

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
   * - ``signals_reconstruct``
     - List
     - | List of componants with dictionary of channels. These channels are
       | SignalModel with properties :
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
2. In the Module Library, find **Ica Restore** under the **Signal Processing** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

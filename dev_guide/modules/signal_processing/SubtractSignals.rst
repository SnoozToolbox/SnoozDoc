.. _module_subtractsignals:

Subtract Signals
================

**Module name:** ``SubtractSignals``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

Subtract signals from a specific channel from the signals of a list of channels.

This module can be used to reformat a montage.

.. note:: For example, to reformat C3-CLE to C3-A2, the input channel is [C3-CLE], and the channel to subtract is [A2-CLE]. To rename properly the channel, the new channel name can be provided.

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
     - | List of SignalModel and their informations
       | Properties:
       | samples:np.array
       | List of samples
       | start_time:float
       | Start time in seconds of the signal in relation to the beginning
       | of the recording.
       | end_time:float
       | End time in seconds of the signal in relation to the beginning
       | of the recording.
       | duration:float
       | Duration in seconds of the signal.
       | sample_rate:float
       | Sampling rate of the signal
       | channel:str
       | Name of the channel
       | alias:str
       | Channel alias.
       | meta:dict
       | Optional information about this signal
       | is_modified:bool
       | Has the signal been modified or not.
   * - ``channel``
     - String or List of strings (usually the output of Alias Signals)
     - —
     - A string with the name of the initial channels. Can be multiple split with ";"
   * - ``channel_to_sub``
     - String or a list of strings
     - —
     - A string with the name of the channel to Subtract
   * - ``new_channel_name``
     - String (let empty to use the default channel name)
     - —
     - | To rename the new Subtracted channel.
       | Valid only when a single channel is Subtracted.

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
     - List
     - | List of SignalModel and their informations
       | Properties:
       | samples:np.array
       | List of samples
       | start_time:float
       | Start time in seconds of the signal in relation to the beginning
       | of the recording.
       | end_time:float
       | End time in seconds of the signal in relation to the beginning
       | of the recording.
       | duration:float
       | Duration in seconds of the signal.
       | sample_rate:float
       | Sampling rate of the signal
       | channel:str
       | Name of the channel
       | alias:str
       | Channel alias.
       | meta:dict
       | Optional information about this signal
       | is_modified:bool
       | Has the signal been modified or not.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Subtract Signals** under the **Signal Processing** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

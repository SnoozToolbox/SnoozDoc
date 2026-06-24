.. _module_mutualinfo:

Mutual Info
===========

**Module name:** ``MutualInfo``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

Find the mutual information between two lists of signals.

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
   * - ``signals1``
     - List of SignalModel
     - —
     - | List of signal with dictionary of channels with SignalModel with
       | properties :
       | name: The name of the channel
       | samples: The samples of the signal
       | alias: The alias of the channel
       | sample_rate: The sample rate of the signal
       | start_time: The start time of the recording
       | montage_index: The index of the montage used for this signal
       | is_modified: Value characterizing if the signal has been modified from the original
   * - ``signals2``
     - List of SignalModel
     - —
     - | List of signal with dictionary of channels with SignalModel with
       | properties :
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
   * - ``mutual_info``
     - List of SignalModel
     - List of mutual info score for each window in each index of the list

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Mutual Info** under the **Statistics** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

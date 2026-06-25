.. _module_spindledetectorsumo:

Spindle Detector Sumo
=====================

**Module name:** ``SpindleDetectorSumo``

**Package:** CEAMSModules 7.4.0

**Version:** 3.0.0

Overview
--------

Class to detect spindles based on the SUMO deep learning algorithm

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
   * - ``event_group``
     - String
     - —
     - List of Event group to filter separated by comma (discard too long, short)
   * - ``event_name``
     - String
     - —
     - List of Event name to filter separated by comma (discard too long, short)

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
   * - ``events``
     - Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
     - Events list for spindle detections.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Spindle Detector Sumo** under the **Detectors** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

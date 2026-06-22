.. _module_connectivitydetails:

Connectivity Details
====================

**Module name:** ``ConnectivityDetails``

**Package:** CEAMSModules 7.4.0

**Version:** 2.0.0

Overview
--------

Node for saving connectivity results (matrix, heatmap, and head plot) to disk. Works for wPLI and dPLI results. Head plot is created only if ≥4 channels match a montage.

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
   * - ``recording_path``
     - string
     - None
     - The path to the recording file.
   * - ``subject_info``
     - dict
     - None
     - Information about the subject.
   * - ``con_dict``
     - dict
     - None
     - The connectivity dictionary.
   * - ``output_path``
     - string
     - None
     - The path to the output directory.

Outputs
-------

This module has no outputs.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Connectivity Details** under the **Events Utilities** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

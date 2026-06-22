.. _module_jsonpatheditormaster:

Json Path Editor Master
=======================

**Module name:** ``JsonPathEditorMaster``

**Package:** CEAMSModules 7.4.0

**Version:** 2.0.0

Overview
--------

This module is designed to edit JSON files by replacing paths within the JSON structure. It takes a list of JSON files, a mapping of old paths to new paths, and saves the modified JSON files to a specified directory.

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
   * - ``files``
     - input json files
     - —
     - input json files
   * - ``path_mapping``
     - a dictionary mapping old paths to new paths
     - —
     - a dictionary mapping old paths to new paths
   * - ``newfilespath``
     - the directory where the modified JSON files will be saved
     - —
     - the directory where the modified JSON files will be saved
   * - ``suffix``
     - a suffix to be added to the modified JSON file names
     - —
     - a suffix to be added to the modified JSON file names

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
   * - ``newfiles``
     - the modified JSON files saved in the specified directory (It is not used in the current implementation)
     - the modified JSON files saved in the specified directory (It is not used in the current implementation)

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Json Path Editor Master** under the **Files I/O** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

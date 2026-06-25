.. _module_renamefilelist:

Rename File List
================

**Module name:** ``RenameFileList``

**Package:** CEAMSModules 7.4.0

**Version:** 2.1.0

Overview
--------

Renames files based on intput parameters such as prefix, suffix, pattern to remove, number of characters to keep.

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
   * - ``file_list``
     - List of strings
     - —
     - List of file names to potentially rename
   * - ``prefix``
     - string
     - —
     - String added at the beginnig of the file name
   * - ``suffix``
     - String
     - —
     - String added to the end of the file name
   * - ``n_char_to_keep``
     - int
     - -1
     - Number of characters to keep
   * - ``pattern_to_rem``
     - string
     - —
     - Pattern to remove from the original file name
   * - ``ext_selection``
     - string
     - —
     - Extension to select the file to rename
   * - ``keep_original_file``
     - int
     - 1
     - 1 to keep the original file name, else to rename

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
   * - ``ren_file_list``
     - List of strings
     - List of renamed file names

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Rename File List** under the **Files I/O** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

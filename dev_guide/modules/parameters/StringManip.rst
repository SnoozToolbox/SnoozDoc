.. _module_stringmanip:

String Manip
============

**Module name:** ``StringManip``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

String manipulaiton.

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
   * - ``input``
     - String
     - —
     - Input string to manipulate
   * - ``prefix``
     - String
     - —
     - String added at the beginnig of the input string.
   * - ``suffix``
     - String
     - —
     - String added to the end of the input string.
   * - ``filename_rm``
     - String of int
     - 0
     - '1' to remove the filename after the path from the input string.
   * - ``path_rm``
     - String of int
     - 1
     - | '1' to remove the path from the input string.
       | Remove any chars before the last \ (including the last \).
   * - ``file_ext_rm``
     - String of int
     - 1
     - '1' to remove the file ext (ex .edf) from the input string.

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
   * - ``output``
     - String
     - Output string manipulated

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **String Manip** under the **Parameters** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

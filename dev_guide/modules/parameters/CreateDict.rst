.. _module_createdict:

Create Dictionary
=================

**Module name:** ``CreateDict``

**Package:** CEAMSModules 7.4.0

**Version:** 2.0.0

Overview
--------

Transforms key-value inputs into a dictionary output while preserving the original value. The dictionary is stringified for compatibility with downstream Flowpipe nodes.

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
   * - ``Key``
     - str
     - —
     - The key to be used in the output dictionary
   * - ``Value``
     - Any
     - —
     - The value to associate with the key in the dictionary

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
   * - ``Dict``
     - str
     - String representation of the generated dictionary (for Flowpipe compatibility)
   * - ``Value``
     - Any
     - The original input value (passed through)

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Create Dictionary** under the **Parameters** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

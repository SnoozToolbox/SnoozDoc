.. _module_createtuple:

Create Tuple
============

**Module name:** ``CreateTuple``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

This module creates a tuple from two input values. It is used to combine two values into a single tuple for further processing.

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
   * - ``Idx0``
     - first value to be included in the tuple
     - —
     - first value to be included in the tuple
   * - ``Idx1``
     - second value to be included in the tuple
     - —
     - second value to be included in the tuple

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
   * - ``Tuple``
     - a tuple containing the two input values
     - a tuple containing the two input values

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Create Tuple** under the **Parameters** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

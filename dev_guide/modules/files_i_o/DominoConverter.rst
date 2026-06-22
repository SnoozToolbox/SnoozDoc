.. _module_dominoconverter:

Domino Converter
================

**Module name:** ``DominoConverter``

**Package:** CEAMSModules 7.4.0

**Version:** 2.1.0

Overview
--------

To convert DOMINO accessory files (ASCII) in one Snooz accessory tsv file.

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
   * - ``folders``
     - String of list of string
     - —
     - List of folders to run through to convert all the supported ASCII files included.
   * - ``log_filename``
     - String
     - —
     - Path and filename to save the log warning message of the conversion.

Outputs
-------

This module has no outputs.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Domino Converter** under the **Files I/O** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

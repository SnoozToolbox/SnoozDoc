.. _module_tsvvalidatormaster:

TSV Validator Master
====================

**Module name:** ``TSVValidatorMaster``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

This module validates TSV files by checking their encoding and structure. It checks if the files are UTF-8 encoded and if they contain the expected columns and data types.

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
     - input TSV files
     - —
     - A list of TSV files to be validated.
   * - ``log_path``
     - the directory where the validation logs will be saved
     - —
     - the directory where the validation logs will be saved

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
   * - ``output_logs``
     - the validation logs in a text file saved in the specified directory
     - the validation logs in a text file saved in the specified directory

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **TSV Validator Master** under the **Files I/O** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

.. _module_tsvwriter:

Tsv Writer
==========

**Module name:** ``TsvWriter``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

Saves events to a CSV file.

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
   * - ``filename``
     - string
     - —
     - The filename to save to
   * - ``events``
     - pandas DataFrame
     - —
     - The list of events to save
   * - ``EDF_annot``
     - bool
     - 1
     - Flag to generate the event_name with @@channel_label.
   * - ``time_elapsed``
     - String of bool
     - 0
     - Flag to add a column with the time elapsed (HH:MM:SS)
   * - ``append_data``
     - String of bool
     - 0
     - Flag to append data to file instead of rewriting
   * - ``add_index``
     - —
     - 0
     - See module settings for configuration details.

Outputs
-------

This module has no outputs.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Tsv Writer** under the **Files I/O** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

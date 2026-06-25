.. _module_aliassignals:

Alias Signals
=============

**Module name:** ``AliasSignals``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

This plugin extract only the signals with a specific Alias.

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
     - A list of SignalModel
     - —
     - The original list of signals to filter;
   * - ``alias``
     - String
     - —
     - The alias of the signals to extract

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
   * - ``signals``
     - A list of SignalModel
     - Signals using the alias defined in the input
   * - ``channels_name``
     - A list of string
     - The list of channels linked to the input alias

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Alias Signals** under the **Parameters** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

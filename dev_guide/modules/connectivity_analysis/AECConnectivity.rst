.. _module_aecconnectivity:

AEC Connectivity
================

**Module name:** ``AECConnectivity``

**Package:** CEAMSModules 7.5.0

**Version:** 0.0.0

Overview
--------

TODO: Add a short description of this module.

Inputs
------

.. list-table::
   :widths: 15 20 12 53
   :header-rows: 1
   :align: left
   :class: left-align-caption wrap-table

   * - Input
     - Format
     - Default
     - Description
   * - ``epochs``
     - —
     - —
     - TODO
   * - ``events``
     - —
     - —
     - TODO

Outputs
-------

.. list-table::
   :widths: 15 20 65
   :header-rows: 1
   :align: left
   :class: left-align-caption wrap-table

   * - Output
     - Format
     - Description
   * - ``aec_results``
     - —
     - TODO

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **AEC Connectivity** under the **Connectivity Analysis** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

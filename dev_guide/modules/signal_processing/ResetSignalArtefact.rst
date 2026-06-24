.. _module_resetsignalartefact:

Reset Signal Artefact
=====================

**Module name:** ``ResetSignalArtefact``

**Package:** CEAMSModules 7.5.0

**Version:** 2.1.0

Overview
--------

To reset the signal that occurs during an artefact.

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
     - a list of SignalModel
     - —
     - | signal.samples : The actual signal data as numpy list
       | signal.sample_rate : the original sampling rate of the signal
       | signal.channel : current channel label
   * - ``events``
     - Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
     - —
     - Events to select based on the sleep stages.
   * - ``artefact_group``
     - String
     - —
     - Event group to reset signal, each group is separated by a comma, as a pattern occurrence.
   * - ``artefact_name``
     - String
     - —
     - Event name to reset signal, each name is separated by a comma, as a pattern occurrence.
   * - ``signal_values``
     - String
     - 0
     - | Signal values during artefact.
       | 0 : replace the artefacted signal values with zeros (with turkey mindow)
       | NaN : replace the artefacted signal values with NaNs

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
     - a list of SignalModel
     - | signal.samples : The actual signal data as numpy list
       | signal.sample_rate : the original sampling rate of the signal
       | signal.channel : current channel label

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Reset Signal Artefact** under the **Signal Processing** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

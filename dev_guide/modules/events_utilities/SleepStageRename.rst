.. _module_sleepstagerename:

Sleep Stage Rename
==================

**Module name:** ``SleepStageRename``

**Package:** CEAMSModules 7.4.0

**Version:** 2.0.0

Overview
--------

Rename sleep stage annotation.

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
   * - ``events_in``
     - pandas DataFrame
     - —
     - List of events to rename (columns=['group','name','start_sec','duration_sec','channels']).
   * - ``group_lut``
     - string (dict converted into a string)
     - {'stage':'stage'}
     - Dict where the key is the original group and the value is the new group.
   * - ``original_name``
     - string (dict converted into a string)
     - {'wake': 'wake', 'N1': 'N1', 'N2': 'N2', 'N3': 'N3', 'N4': 'N4', 'R': 'R', 'movement': 'movement', 'tech': 'tech', 'unscored': 'unscored'}
     - | Dict where the values are the original annotation names.
       | The keys are specified into plugin/PSGReader/commons.py
       | ex) sleep_stages_name = {
       | "wake": "Eveil",
       | "N1": "Stade1",
       | "N2": "Stade2",
       | ...
   * - ``new_name``
     - string (dict converted into a string)
     - {'wake': 'wake', 'N1': 'N1', 'N2': 'N2', 'N3': 'N3', 'N4': 'N4', 'R': 'R', 'movement': 'movement', 'tech': 'tech', 'unscored': 'unscored'}
     - | Dict where the values are the new annotation names.
       | The keys are specified into plugin/PSGReader/commons.py
       | ex) sleep_stages_name = {
       | "wake": "0",
       | "N1": "1",
       | "N2": "2",
       | ...

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
   * - ``events_out``
     - pandas DataFrame
     - List of events (columns=['group','name','start_sec','duration_sec','channels'])

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Sleep Stage Rename** under the **Events Utilities** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

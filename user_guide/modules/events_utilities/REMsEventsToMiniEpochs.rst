.. _module_remseventstominiepochs:

REMs to mini-epochs
===================

**Module name:** ``REMsEventsToMiniEpochs``

**Package:** CEAMSModules 7.4.0

**Version:** 0.0.0

Overview
--------

Class to generate a list of mini-epochs identified as a MOR_DET or NO_DET based on the list of REM detections.

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
     - The name of the current PSG file.
   * - ``REMs_events``
     - Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
     - —
     - List of detections from REMDetectorShotGroup
   * - ``epochs_to_proceed``
     - Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
     - —
     - | List of mini-epochs to identify as a MOR_DET or NO_DET.
   * - ``parameters``
     - dict
     - None
     - | Dictionary of group and name of the mini-epoch.
       | 'mini_epoch_group': 'DET_MOR'
       | 'mini_epoch_name_Phasic': 'Snooz_MOR_Phasic'
       | 'mini_epoch_name_Tonic': 'Snooz_MOR_Tonic'

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
   * - ``mini_epochs_events``
     - Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
     - List of mini-epochs identified as a MOR_DET or NO_DET.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **REMs to mini-epochs** under the **Events Utilities** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

.. _module_remseventstominiepochs:

REMs to mini-epochs
===================

**Module name:** ``REMsEventsToMiniEpochs``

**Package:** CEAMSModules 7.5.0

**Version:** 0.0.0

Overview
--------

Creates a list of mini-epochs identified as a EOG_Phasic or EOG_Tonic based on the list of REM detections.

Inputs
------

.. list-table::
   :widths: 22 20 12 48
   :header-rows: 1
   :align: left
   :class: left-align-caption wrap-table

   * - Input
     - Format
     - Default
     - Description
   * - ``filename``
     - String
     - —
     - The name of the current PSG file.
   * - ``REMs_events``
     - Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
     - —
     - df of detected REMevents with fields:
        group: Group of events this event is part of (String)
        name: Name of the event (String)
        start_sec: Starting time of the event in sec (Float)
        duration_sec: Duration of the event in sec (Float)
        channels: Channel where the event occures (String)
   * - ``epochs_to_proceed``
     - Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
     - —
     - List of mini-epochs to identify as a EOG_Phasic or EOG_Tonic.
   * - ``parameters``
     - dictionary
     - —
     - Dictionary of group and name of the mini-epochs:
            'mini_epoch_group': 'REMs'
            'mini_epoch_name_Phasic': 'EOG_Phasic'
            'mini_epoch_name_Tonic': 'EOG_Tonic'

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
   * - ``mini_epochs_events``
     - Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
     - List of mini-epochs identified as a EOG_Phasic or EOG_Tonic.

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

.. _module_discardevents:

Discard Events
==============

**Module name:** ``DiscardEvents``

**Package:** CEAMSModules 7.5.0

**Version:** 2.1.0

Overview
--------

To discard too long, too short or events that occur during artefacts.

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
   * - ``events``
     - Pandas DataFrame
     - —
     - DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])
   * - ``event_group``
     - String
     - —
     - Event group to filter (discard too long, short).
   * - ``event_name``
     - String
     - —
     - Event name to filter (discard too long, short).
   * - ``min_len_sec``
     - float
     - 0
     - Mimimum length accepted, shorter events are discared.
   * - ``max_len_sec``
     - float
     - 30
     - Maximum length accepted, longer events are discared.
   * - ``artefact_free``
     - bool
     - 0
     - | '1' : discard events that occur during an artefact.
       | '0' : keep all events
   * - ``artefact_group``
     - String
     - —
     - | Events to considered as artefact.
       | The user can define a single group (and let the name blank) or a single name (and let the group blank).
       | If group and name are defined, they must be defined in pairs.
       | Each group should be separated by a comma. The group works as a pattern matching.
   * - ``artefact_name``
     - String
     - —
     - | Events to considered as artefact.
       | Each name should be separated by a comma. The name works as a pattern matching.

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
   * - ``events``
     - Pandas DataFrame
     - DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Discard Events** under the **Events Utilities** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

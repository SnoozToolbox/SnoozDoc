.. _module_removechannelartefact:

Remove Channel Artefact
=======================

**Module name:** ``RemoveChannelArtefact``

**Package:** CEAMSModules 7.5.0

**Version:** 2.0.0

Overview
--------

Remove full-channel artefacts from signals and events.

This module accepts one or multiple artefact group/name pairs to identify channel-level artefacts. It removes any SignalModel whose channel matches these artefacts (after warning if the artefact does not span the full signal) and drops the corresponding events from the DataFrame.

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
     - list of SignalModel
     - —
     - | List of SignalModel objects, each with attributes:
       | .samples (numpy array),
       | .sample_rate (Hz),
       | .channel (str),
       | .start_time (s),
       | .end_time (s) and .duration (s).
   * - ``events``
     - pandas.DataFrame
     - —
     - DataFrame of events with columns ['group','name','start_sec','duration_sec','channels'].
   * - ``artefact_group``
     - str
     - —
     - Comma-separated artefact event groups (e.g. 'art_inspector').
   * - ``artefact_name``
     - str
     - —
     - | Comma-separated artefact event names (e.g. 'non_brain,art_channel').
       | If only one group is given but multiple names, that group is applied to all names.

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
   * - ``clean_signals``
     - list of SignalModel
     - Signals with any full-channel artefacts removed.
   * - ``clean_events``
     - pandas.DataFrame
     - Events DataFrame with specified artefact rows removed.

Usage in a process
------------------

1. Open **Dev Tools -> New process** in Snooz.
2. In the Module Library, find **Remove Channel Artefact** under the **Signal Processing** category.
3. Drag the module onto the process canvas.
4. Connect the required inputs from upstream modules (or set values in the **Settings** tab).
5. Connect outputs to downstream modules as needed.
6. Double-click the module to configure parameters in the **Settings** tab.
7. Run the process and inspect results in the **Results** tab.

.. note::

   For general guidance on building processes with modules, see :doc:`/dev_guide/explore_ex`.

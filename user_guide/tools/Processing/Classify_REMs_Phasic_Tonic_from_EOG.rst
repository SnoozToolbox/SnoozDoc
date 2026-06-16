.. _Classify_REMs_Phasic_Tonic_from_EOG:

==============================================
Classify REMs into Phasic/Tonic States from EOG
==============================================

This tool classifies REM sleep into phasic and tonic mini-epochs based on previously detected Rapid Eye Movement events stored in the annotation file using EOG signal.
It is designed to help users separate REM activity into the two most commonly used REM subtypes for downstream analysis.

The classification is based on the already detected REM events and the settings can be adjusted through user-defined settings.

The classified mini-epochs will be added to the original accessory file (.tsv, .STS or .ent).

The event information is:

   * **group** : the group of the event.
   * **name** : the name of the event.
   * **start_sec** : the onset of the event in seconds (time elapsed from the lights off).
   * **duration_sec** : the duration of the event in seconds.
   * **channels** : the list of channels on which the event occurs.

Steps
-----------------


**1 - Input Files**

Start by opening your PSG files (.edf, .sts or .eeg).

- **European Data Format (EDF)** :

  The corresponding .tsv file is required with .edf. Both files must be saved in the same directory and share the exact same filename.

- **Stellate format (up to version 6.2)** :

  The corresponding .sig file is required with the .sts. Both files must be saved in the same directory and share the exact same filename.

- **NATUS format (version 9.1)** :

  (*CEAMS users only*) The entire NATUS subject folder is required.

For more details on accepted formats, see :ref:`accepted_format`.

**2 - REMs events Selection**

Select the annotated REMs events.


**3 - Mini-epoch definition Settings**

Define the parameters used to separate phasic and tonic REM activity.

- Group for the mini-epochs
- Name for the phasic and tonic mini-epochs
- Stage name (5 for REM sleep in Snooz)
- Window length (in seconds) for the mini-epochs
- Number of windows


**4 - Output Files**

The classified mini-epochs are added to the original accessory file (.tsv, .STS or .ent) with the same filename as the input PSG file and saved in the same directory.


Version History
-----------------

* v0.0.0 : Distributed with CEAMS package version 7.4.0 — Snooz beta 3.1.0
    - Initial release of the tool.
* v0.1.0 : Distributed with CEAMS package version 7.4.0 — Snooz beta 3.1.0
    - Add error handling workflow for PSG loading from workspaces and display failed files in the UI.

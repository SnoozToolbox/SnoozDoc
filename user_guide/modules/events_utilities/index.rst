.. _modules_events_utilities:

Events Utilities
================

This section documents the **Events Utilities** modules from the CEAMSModules package.
Use these modules to build custom Snooz processes.

Modules
-------

.. toctree::
   :maxdepth: 1

   ConnectivityDetails
   DefineEventGroup
   DiscardEvents
   DropRenameEvents
   EventCombine
   EventCompare
   EventCreator
   EventSubdivision
   EventsSplitter
   ExtendEvents
   FilterEvents
   PerformanceByEvent
   PSAPicsGenerator
   REMsDetails
   REMsEventsToMiniEpochs
   ReplaceEventInSignals
   ScoringCompleteness
   SignalsFromEvents
   SleepStageEvents
   SleepStageRename
   SlowWavePicsGenerator
   SlowWavesDetails
   SpindlesDetails
   WindowsToSamples

Quick reference
---------------

.. list-table::
   :widths: 30 15 55
   :header-rows: 1
   :align: left
   :class: left-align-caption wrap-table

   * - Module
     - Version
     - Description
   * - :ref:`Connectivity Details <module_connectivitydetails>`
     - 2.0.0
     - Saving connectivity results  to disk.
   * - :ref:`Define Event Group <module_defineeventgroup>`
     - 2.0.0
     - Defines groups to events.
   * - :ref:`Discard Events <module_discardevents>`
     - 2.1.0
     - Discards too long, too short or events that occur during artefacts.
   * - :ref:`Drop/Rename Events <module_droprenameevents>`
     - 2.0.0
     - Drops events and/or rename events group and/or name.
   * - :ref:`Event Combine <module_eventcombine>`
     - 2.0.0
     - Combines two lists of events, with or without selection.
   * - :ref:`Event Compare <module_eventcompare>`
     - 2.0.0
     - Compares two sets of events .
   * - :ref:`Event Creator <module_eventcreator>`
     - 2.0.0
     - Creates a pandas Dataframe of events.
   * - :ref:`Event Subdivision <module_eventsubdivision>`
     - 0.0.0
     - Creates a new pandas DataFrame of events with subwindow of every input events named events_names.
   * - :ref:`Events Splitter <module_eventssplitter>`
     - 2.0.0
     - Used to split too long events.
   * - :ref:`Extend Events <module_extendevents>`
     - 2.0.0
     - Extend or shrink events by a percentage of their duration, applied to each side.
   * - :ref:`Filter Events <module_filterevents>`
     - 2.0.0
     - Selects  events from specific sleep stages.
   * - :ref:`Performance By Event <module_performancebyevent>`
     - 2.0.0
     - Compares two sets of events .
   * - :ref:`PSA Pics Generator <module_psapicsgenerator>`
     - 2.0.1
     - Used to generate figures of Power Spectral Analysis (PSA) data from PSA report files.
   * - :ref:`REMs Details <module_remsdetails>`
     - 2.2.0
     - Averages REMs events characteristics such as duration, amplitude and density per stage and sleep cycle.
   * - :ref:`REMs to mini-epochs <module_remseventstominiepochs>`
     - 0.0.0
     - Used to generate a list of mini-epochs identified as a Phasic or Tonic based on the list of detected REMs.
   * - :ref:`Replace Event In Signals <module_replaceeventinsignals>`
     - 2.1.0
     - Inserts samples from event dataframe inside a signals.
   * - :ref:`Scoring Completeness <module_scoringcompleteness>`
     - 2.0.0
     - Evaluates if the scoring (events) is unique, complete and specific to the sleep staging.
   * - :ref:`Signals From Events <module_signalsfromevents>`
     - 3.0.0
     - Manages a list of SignalModel from specific events during a recording.
   * - :ref:`Sleep Stage Events <module_sleepstageevents>`
     - 2.1.0
     - Creates a list of event from specific sleep stages during a recording.
   * - :ref:`Sleep Stage Rename <module_sleepstagerename>`
     - 2.0.0
     - Renames sleep stage annotation.
   * - :ref:`Slow Wave Pics Generator <module_slowwavepicsgenerator>`
     - 3.0.0
     - Used to generate pictures of slow wave events.
   * - :ref:`Slow Waves Details <module_slowwavesdetails>`
     - 2.2.0
     - Averages slow wave events characteristics such as duration, amplitude, frequency and so on per stage and sleep cycle.
   * - :ref:`Spindles Details <module_spindlesdetails>`
     - 2.2.0
     - Computes spindles events characteristics such as duration, amplitude, frequency and so on.
   * - :ref:`Windows To Samples <module_windowstosamples>`
     - 2.0.0
     - Converts information based on windows (i.e. RMS energy) into a time series.

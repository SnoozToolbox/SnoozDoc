.. _modules:

Modules
=======

This guide documents all the necessary information needed to use the modules in the **CEAMSModules** package.
Modules are the building blocks of Snooz processes. Each module performs
a specific operation on signals, events, files, or parameters.

Modules are grouped by category as they appear in the Snooz Module Library.
Select a category below to browse module documentation.

How to use modules
------------------

1. In Snooz, go to **Dev Tools -> New process**.
2. Open the **Module Library** and enable the **CEAMSModules** package if needed.
3. Drag modules from a category onto the process canvas.
4. Connect module inputs and outputs to define your analysis pipeline.
5. Configure each module via its **Settings** tab and run the process.

For a hands-on introduction to processes and modules, see :doc:`/dev_guide/explore_ex`.

Categories
----------

.. toctree::
   :maxdepth: 2
   :caption: Module categories:

   connectivity_analysis/index
   detectors/index
   events_analysis/index
   events_utilities/index
   files_i_o/index
   hypnogram_analysis/index
   parameters/index
   signal_processing/index
   statistics/index

All modules
-----------

.. list-table::
   :widths: 10 24 18 12 38
   :header-rows: 1
   :align: left
   :class: left-align-caption wrap-table

   * - Item
     - Module
     - Category
     - Version
     - Description
   * - 1
     - :ref:`Dpli Connectivity <module_dpliconnectivity>`
     - Connectivity Analysis
     - 2.1.0
     - Computes per-epoch, surrogate-corrected Directed Phase Lag Index (dPLI) matrices from EEG epochs.
   * - 2
     - :ref:`Wpli Connectivity <module_wpliconnectivity>`
     - Connectivity Analysis
     - 2.1.0
     - Computes per-epoch, surrogate-corrected Weighted Phase Lag Index (wPLI) matrices from EEG epochs.
   * - 3
     - :ref:`A4Precise Events <module_a4preciseevents>`
     - Detectors
     - 2.0.0
     - Refines onset and duration of events detected by the a4 spindle detector.
   * - 4
     - :ref:`Amplitude Detector <module_amplitudedetector>`
     - Detectors
     - 2.0.0
     - Detects events based on the absolute signal amplitude.
   * - 5
     - :ref:`Amplitude Var Detector <module_amplitudevardetector>`
     - Detectors
     - 2.0.0
     - Detects events based on maximum amplitude variation in a narrow time windows.
   * - 6
     - :ref:`Detection View <module_detectionview>`
     - Detectors
     - 2.0.0
     - Organizes detection information and saves it into the cache in order to plot it.
   * - 7
     - :ref:`Oxygen Desaturation Detector <module_oxygendesatdetector>`
     - Detectors
     - 2.5.0
     - Analyzes the oxygen channel, detect oxygen desaturations and export oxygen saturation report.
   * - 8
     - :ref:`REMs Detection Yasa <module_remsdetectionyasa>`
     - Detectors
     - 3.1.0
     - Detects Rapid Eye Movements (REMs) in EOG sleep recordings using YASA REM detection algorithm.
   * - 9
     - :ref:`Slow Wave Detector <module_slowwavedetector>`
     - Detectors
     - 2.3.0
     - Detects slow wave events based on the Carrier method.
   * - 10
     - :ref:`Spectral Detector <module_spectraldetector>`
     - Detectors
     - 2.2.0
     - Detects events based on the spectrum.
   * - 11
     - :ref:`Spindle Detector A7 <module_spindledetectora7>`
     - Detectors
     - 3.0.0
     - Detects spindles based on the a7 algorithm.
   * - 12
     - :ref:`Spindle Detector Sumo <module_spindledetectorsumo>`
     - Detectors
     - 3.0.0
     - Detects spindles based on the SUMO deep learning algorithm.
   * - 13
     - :ref:`Event Sleep Report <module_eventsleepreport>`
     - Events Analysis
     - 2.0.0
     - Generates event sleep report.
   * - 14
     - :ref:`Event Temporal Link <module_eventtemporallink>`
     - Events Analysis
     - 2.0.0
     - Generates temporal links listed in the input temporal_links.
   * - 15
     - :ref:`Connectivity Details <module_connectivitydetails>`
     - Events Utilities
     - 2.0.0
     - Saving connectivity results  to disk.
   * - 16
     - :ref:`Define Event Group <module_defineeventgroup>`
     - Events Utilities
     - 2.0.0
     - Defines groups to events.
   * - 17
     - :ref:`Discard Events <module_discardevents>`
     - Events Utilities
     - 2.1.0
     - Discards too long, too short or events that occur during artefacts.
   * - 18
     - :ref:`Drop/Rename Events <module_droprenameevents>`
     - Events Utilities
     - 2.0.0
     - Drops events and/or rename events group and/or name.
   * - 19
     - :ref:`Event Combine <module_eventcombine>`
     - Events Utilities
     - 2.1.0
     - Combines two lists of events, with or without selection.
   * - 20
     - :ref:`Event Compare <module_eventcompare>`
     - Events Utilities
     - 2.0.0
     - Compares two sets of events .
   * - 21
     - :ref:`Event Creator <module_eventcreator>`
     - Events Utilities
     - 2.0.0
     - Creates a pandas Dataframe of events.
   * - 22
     - :ref:`Events Splitter <module_eventssplitter>`
     - Events Utilities
     - 2.0.0
     - Used to split too long events.
   * - 23
     - :ref:`Extend Events <module_extendevents>`
     - Events Utilities
     - 2.0.0
     - Extend or shrink events by a percentage of their duration, applied to each side.
   * - 24
     - :ref:`Filter Events <module_filterevents>`
     - Events Utilities
     - 2.0.0
     - Selects  events from specific sleep stages.
   * - 25
     - :ref:`Performance By Event <module_performancebyevent>`
     - Events Utilities
     - 2.0.0
     - Compares two sets of events .
   * - 26
     - :ref:`PSA Pics Generator <module_psapicsgenerator>`
     - Events Utilities
     - 2.0.1
     - Used to generate figures of Power Spectral Analysis (PSA) data from PSA report files.
   * - 27
     - :ref:`REMs Details <module_remsdetails>`
     - Events Utilities
     - 2.2.0
     - Averages REMs events characteristics such as duration, amplitude and density per stage and sleep cycle.
   * - 28
     - :ref:`Replace Event In Signals <module_replaceeventinsignals>`
     - Events Utilities
     - 2.1.0
     - Inserts samples from event dataframe inside a signals.
   * - 29
     - :ref:`Scoring Completeness <module_scoringcompleteness>`
     - Events Utilities
     - 2.0.0
     - Evaluates if the scoring (events) is unique, complete and specific to the sleep staging.
   * - 30
     - :ref:`Signals From Events <module_signalsfromevents>`
     - Events Utilities
     - 3.1.0
     - Manages a list of SignalModel from specific events during a recording.
   * - 31
     - :ref:`Sleep Stage Events <module_sleepstageevents>`
     - Events Utilities
     - 2.1.0
     - Creates a list of event from specific sleep stages during a recording.
   * - 32
     - :ref:`Sleep Stage Rename <module_sleepstagerename>`
     - Events Utilities
     - 2.0.0
     - Renames sleep stage annotation.
   * - 33
     - :ref:`Slow Wave Pics Generator <module_slowwavepicsgenerator>`
     - Events Utilities
     - 3.1.0
     - Used to generate pictures of slow wave events.
   * - 34
     - :ref:`Slow Waves Details <module_slowwavesdetails>`
     - Events Utilities
     - 2.3.0
     - Averages slow wave events characteristics such as duration, amplitude, frequency and so on per stage and sleep cycle.
   * - 35
     - :ref:`Spindles Details <module_spindlesdetails>`
     - Events Utilities
     - 2.2.0
     - Computes spindles events characteristics such as duration, amplitude, frequency and so on.
   * - 36
     - :ref:`Windows To Samples <module_windowstosamples>`
     - Events Utilities
     - 2.0.0
     - Converts information based on windows (i.e. RMS energy) into a time series.
   * - 37
     - :ref:`Csv Reader Master <module_csvreadermaster>`
     - Files I/O
     - 2.0.0
     - Reads events from a CSV file.
   * - 38
     - :ref:`Detections Cohort Review <module_detectionscohortreview>`
     - Files I/O
     - 2.1.0
     - Reads the spindle/sw output files and generates the "Detected events cohort report" file clean or transposed.
   * - 39
     - :ref:`Domino Converter <module_dominoconverter>`
     - Files I/O
     - 2.1.0
     - Converts DOMINO accessory files (ASCII) in one Snooz accessory tsv file.
   * - 40
     - :ref:`EDF Annotations Reader <module_edfannotationsreader>`
     - Files I/O
     - 2.0.0
     - Used to read the EDF Annotations signal and create a pandas dataframe with the events.
   * - 41
     - :ref:`Edf Xml Reader <module_edfxmlreader>`
     - Files I/O
     - 2.0.0
     - Reads events from a EDF.XML file.
   * - 42
     - :ref:`Edf Xml Reader Master <module_edfxmlreadermaster>`
     - Files I/O
     - 2.0.0
     - Reads events from a EDF.XML files or .XML files.
   * - 43
     - :ref:`Edf Xml Writer <module_edfxmlwriter>`
     - Files I/O
     - 2.0.0
     - Creates an XML file based on compumedic format.
   * - 44
     - :ref:`Event Reader <module_eventreader>`
     - Files I/O
     - 3.0.0
     - Reads events from a Tsv file.
   * - 45
     - :ref:`Json Path Editor Master <module_jsonpatheditormaster>`
     - Files I/O
     - 2.0.0
     - Edits JSON files by replacing paths within the JSON structure.
   * - 46
     - :ref:`PSA Cohort Review <module_psacohortreview>`
     - Files I/O
     - 2.5.0
     - Reads the PSA output file and generates the PSA file clean or transposed.
   * - 47
     - :ref:`PSGReader <module_psgreader>`
     - Files I/O
     - 2.5.0
     - Reads a PSG file.
   * - 48
     - :ref:`PSGWriter <module_psgwriter>`
     - Files I/O
     - 2.3.0
     - Writes a PSG file.
   * - 49
     - :ref:`Rename File List <module_renamefilelist>`
     - Files I/O
     - 2.1.0
     - Renames files based on input parameters such as prefix.
   * - 50
     - :ref:`Sleep Stages Importer <module_sleepstagesimporter>`
     - Files I/O
     - 2.1.0
     - Imports sleep stages from a textfile into the sleep_stages dataframe.
   * - 51
     - :ref:`TSV Validator Master <module_tsvvalidatormaster>`
     - Files I/O
     - 2.0.0
     - Validates TSV files by checking their encoding and structure.
   * - 52
     - :ref:`Tsv Writer <module_tsvwriter>`
     - Files I/O
     - 2.0.0
     - Saves events to a CSV file.
   * - 53
     - :ref:`Hypnogram <module_hypnogram>`
     - Hypnogram Analysis
     - 2.1.0
     - Displays in the results view an hypnogram and its sleep cycles.
   * - 54
     - :ref:`Sleep Bouts <module_sleepbouts>`
     - Hypnogram Analysis
     - 2.0.0
     - Supports sleep bouts operations within a Snooz process.
   * - 55
     - :ref:`Sleep Cycles Delimiter <module_sleepcyclesdelimiter>`
     - Hypnogram Analysis
     - 2.4.0
     - Compute the sleep cycles.
   * - 56
     - :ref:`Sleep Report <module_sleepreport>`
     - Hypnogram Analysis
     - 2.1.0
     - Generates a sleep report in CSV file.
   * - 57
     - :ref:`Alias Signals <module_aliassignals>`
     - Parameters
     - 2.0.0
     - Extract only the signals with a specific Alias.
   * - 58
     - :ref:`Constant <module_constant>`
     - Parameters
     - 2.0.0
     - Passes a value to the next node.
   * - 59
     - :ref:`Create Dictionary <module_createdict>`
     - Parameters
     - 2.0.0
     - Transforms key-value inputs into a dictionary output while preserving the original value.
   * - 60
     - :ref:`Create List of Group Name <module_createlistofgroupname>`
     - Parameters
     - 2.0.0
     - Creates a list of tuples that has two values of group and name.
   * - 61
     - :ref:`Create Tuple <module_createtuple>`
     - Parameters
     - 2.0.0
     - Creates a tuple from two input values.
   * - 62
     - :ref:`Dictionary <module_dictionary>`
     - Parameters
     - 2.0.0
     - Returns a value based on a key received in input.
   * - 63
     - :ref:`String Manip <module_stringmanip>`
     - Parameters
     - 2.0.0
     - Allows string manipulaiton.
   * - 64
     - :ref:`Epoch Signal <module_epochsignal>`
     - Signal Processing
     - 2.0.0
     - Segments EEG signals into overlapping or non-overlapping epochs of fixed duration.
   * - 65
     - :ref:`Filter Signal <module_filtersignal>`
     - Signal Processing
     - 2.1.0
     - Applies a FIR/IIR filter to EEG signals.
   * - 66
     - :ref:`Ica Components <module_icacomponents>`
     - Signal Processing
     - 2.0.0
     - Find components of a signal with idependant component analysis.
   * - 67
     - :ref:`Ica Restore <module_icarestore>`
     - Signal Processing
     - 2.0.0
     - Reconstructs signal from ICA components.
   * - 68
     - :ref:`Invert Signals <module_invertsignals>`
     - Signal Processing
     - 2.0.0
     - Inverts signals.
   * - 69
     - :ref:`IRASA YASA <module_irasayasa>`
     - Signal Processing
     - 0.0.0
     - Spectral power decomposition using IRASA algorithm.
   * - 70
     - :ref:`Moving RMS <module_movingrms>`
     - Signal Processing
     - 2.0.0
     - Computes RMS value on a moving window.
   * - 71
     - :ref:`PSA Compilation FOOOF <module_psacompilationfooof>`
     - Signal Processing
     - 0.0.0
     - Analyses and reports the PSD output designed specifically for FOOOF analysis.
   * - 72
     - :ref:`Remove Channel Artefact <module_removechannelartefact>`
     - Signal Processing
     - 2.0.0
     - Removes full-channel artefacts from signals and events.
   * - 73
     - :ref:`Resample <module_resample>`
     - Signal Processing
     - 2.0.0
     - Resamples a signal.
   * - 74
     - :ref:`Rescale Signal <module_rescalesignal>`
     - Signal Processing
     - 2.1.0
     - Creates a list of dictionaries with the channels from specific epochs during a recording.
   * - 75
     - :ref:`Reset Signal Artefact <module_resetsignalartefact>`
     - Signal Processing
     - 2.1.0
     - Resets the signal that occurs during an artefact.
   * - 76
     - :ref:`Score Sleep Stages YASA <module_yasasleepstaging>`
     - Signal Processing
     - 2.0.0
     - Automatic sleep stage classification using YASA's machine learning model.
   * - 77
     - :ref:`Stft <module_stft>`
     - Signal Processing
     - 2.1.0
     - Computes the STFT on the signal split into sliding windows.
   * - 78
     - :ref:`Subtract Signals <module_subtractsignals>`
     - Signal Processing
     - 2.0.0
     - Subtracts signals from a specific channel from the signals of a list of channels.
   * - 79
     - :ref:`Trim Signal <module_trimsignal>`
     - Signal Processing
     - 2.0.0
     - Trims continuous/discontinuous signal segments and their associated events to a time window defined by.
   * - 80
     - :ref:`Mutual Info <module_mutualinfo>`
     - Statistics
     - 2.0.0
     - Finds the mutual information between two lists of signals.
   * - 81
     - :ref:`PSA Compilation <module_psacompilation>`
     - Statistics
     - 2.2.0
     - Analyses and reports the PSD output.
   * - 82
     - :ref:`PSA on Events <module_psaonevents>`
     - Statistics
     - 2.1.0
     - Compiles the PSA run on selected events.
   * - 83
     - :ref:`Signal Stats <module_signalstats>`
     - Statistics
     - 2.0.0
     - Computes the mean and standard deviation of the input signals per epoch, per channel.
   * - 84
     - :ref:`Sleep Staging Export Results <module_sleepstagingexportresults>`
     - Statistics
     - 2.0.0
     - Processes and visualizes sleep staging results.
   * - 85
     - :ref:`Slow Wave Classifier <module_slowwaveclassifier>`
     - Statistics
     - 2.0.0
     - Classifies slow wave events based on a gaussian mixture.
   * - 86
     - :ref:`Threshold Computation <module_thresholdcomputation>`
     - Statistics
     - 2.1.0
     - Computes the value to threshold (i.e. µV) from a signals (i.e. EEG time series)

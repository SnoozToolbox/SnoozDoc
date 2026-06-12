.. _modules_detectors:

Detectors
=========

This section documents the **Detectors** modules from the CEAMSModules package.
Use these modules to build custom Snooz processes.

Modules
-------

.. toctree::
   :maxdepth: 1

   A4PreciseEvents
   AmplitudeDetector
   AmplitudeVarDetector
   DetectionView
   OxygenDesatDetector
   REMsDetectionYasa
   SlowWaveDetector
   SpectralDetector
   SpindleDetectorA7
   SpindleDetectorSumo

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
   * - :ref:`A4Precise Events <module_a4preciseevents>`
     - 2.0.0
     - Refines onset and duration of events detected by the a4 spindle detector.
   * - :ref:`Amplitude Detector <module_amplitudedetector>`
     - 2.0.0
     - Detects events based on the absolute signal amplitude.
   * - :ref:`Amplitude Var Detector <module_amplitudevardetector>`
     - 2.0.0
     - Detects events based on maximum amplitude variation in a narrow time windows.
   * - :ref:`Detection View <module_detectionview>`
     - 2.0.0
     - Organizes detection information and saves it into the cache in order to plot it.
   * - :ref:`Oxygen Desaturation Detector <module_oxygendesatdetector>`
     - 2.4.0
     - Analyzes the oxygen channel, detect oxygen desaturations and export oxygen saturation report.
   * - :ref:`REMs Detection Yasa <module_remsdetectionyasa>`
     - 3.1.0
     - Detects Rapid Eye Movements (REMs) in EOG sleep recordings using YASA REM detection algorithm.
   * - :ref:`Slow Wave Detector <module_slowwavedetector>`
     - 2.2.0
     - Detects slow wave events based on the Carrier method.
   * - :ref:`Spectral Detector <module_spectraldetector>`
     - 2.1.0
     - Detects events based on the spectrum.
   * - :ref:`Spindle Detector A7 <module_spindledetectora7>`
     - 3.0.0
     - Detects spindles based on the a7 algorithm.
   * - :ref:`Spindle Detector Sumo <module_spindledetectorsumo>`
     - 3.0.0
     - Detects spindles based on the SUMO deep learning algorithm.

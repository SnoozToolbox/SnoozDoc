.. _DominoScreen_Converter:

============================
Convert DOMINO
============================

Description
-----------------

To convert the DOMINO ASCII accessory files (without sleep stages) to the Snooz accessory .tsv file.

Supported Formats
-------------------

* Sleep profile  

    .. code-block:: rst

        Signal ID: SchlafProfil
        Start Time: 08/03/2016 0:14:00
        Unit: 
        Signal Type: Discret
        Events list: N4,N3,N2,N1,REM,Wake,Movement
        Rate: 30 s

        00:14:00,000; Wake
        00:14:30,000; Wake
        00:15:00,000; Wake
  
* Annotations from the expert  
  
    .. code-block:: rst

        Signal ID: FlowD
        Start Time: 08/03/2016 0:14:00
        Unit: s
        Signal Type: Impuls

        00:22:48,246-00:23:00,246; 12;Hypopnea
        00:40:04,219-00:40:19,219; 15;Obstructive Apnea
        00:54:16,219-00:55:26,219; 70;Obstructive Apnea
        01:36:57,630-01:37:16,870; 19;Flow Limitation

**Examples of supported accessory files**

* Cardiac Events
* Classification Arousals
* Classification PTT
* Classification Systolic
* Effort DC Events
* Effort Int Events
* Flow Events
* Phase Angle Events
* PLM Events
* Sleep profile
* Snore Events
* Spindle  K
* SpO2 Events


Unsupported format
-------------------

* Recorded or computed values 

    .. code-block:: rst

        Signal ID: SchlafFFT
        Start Time: 17/11/2010 23:57:00
        Unit: Hz
        Signal Type: Analog
        
        23:57:00,000; 11
        23:57:01,000; 11
        23:57:02,000; 12
        23:57:03,000; 14

**Examples of unsupported accessory files**

* Systolic PTT
* Act
* Alpha+Beta FFT
* Average Frequency Value
* BF
* Delta FFT
* Diastolic
* Diastolic PTT
* Generic
* Heart Rate
* HRV HF
* HRV LF
* Integral EMG
* Light
* MAP
* Markers
* Obstruction
* Phase Angle
* Position
* PTT Raw
* Sigma FFT
* Sleep Profile Reliability
* SpO2
* SVB
* Systolic


.. note::

    Look at the "Input Folders" step of the "DOMINOScreen Converter" tool to know how to organize the files in order to convert them to the Snooz accessory .tsv file.

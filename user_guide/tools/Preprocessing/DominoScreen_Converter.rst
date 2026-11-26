.. _DominoScreen_Converter:

==============================================
Convert Annotations from DOMINOScreen
==============================================

To convert the DOMINO ASCII accessory files (export ANALYSIS DATA - WITHOUT SLEEP PROFILE) to one Snooz accessory .tsv file per recording folder, named after the EDF file of the folder. The sleep profile gives the sleep stages (group stage).

.. warning::

    The .tsv file named after the EDF file, in each folder, is replaced by the converted file.

Supported Formats
-------------------

* Sleep profile  

    .. code-block:: rst

        Signal ID: SchlafProfil\profil
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

        Signal ID: FlowD\flow
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


How the files are converted
-----------------------------

A DOMINO file has a header, a blank line, then one row per event. The columns of a row are separated by semicolons (``;``). Snooz counts the columns of the first row to know the format of the file, then writes each row as an event with the five columns of the Snooz annotation file.

The times become seconds from the ``Start Time`` of the header. The date is not read. A time earlier than the ``Start Time`` is taken as the next day. For example, with the ``Start Time`` 23:57:00, the time 00:10:00 gives 780 s.

**Sleep profile (2 columns, the time and the stage)**

* ``group`` is ``stage``, because the ``Signal ID`` ends with ``\profil``.
* ``name`` is the number of the stage in Snooz (0 Wake, 1 N1, 2 N2, 3 N3, 4 N4, 5 REM, 6 Movement).
* ``start_sec`` is the time of the row minus the ``Start Time``, in seconds.
* ``duration_sec`` is the ``Rate`` (in s or ms).
* ``channels`` is empty.

Another DOMINO file with 2 columns and a ``Rate`` is converted the same way. Its group is the end of the ``Signal ID`` and its names are kept.

The sleep profile example above gives these events.

.. list-table::
   :header-rows: 1

   * - group
     - name
     - start_sec
     - duration_sec
     - channels
   * - stage
     - 0
     - 0
     - 30
     - []
   * - stage
     - 0
     - 30
     - 30
     - []
   * - stage
     - 0
     - 60
     - 30
     - []

**Annotations from the expert (3 columns, the start and end times, the duration and the name)**

* ``group`` is the end of the ``Signal ID``, after the last backslash (``flow`` in the example).
* ``name`` is the 3rd column.
* ``start_sec`` is the start time of the row minus the ``Start Time``, in seconds.
* ``duration_sec`` is the end time minus the start time. The duration in the 2nd column is not read.
* ``channels`` is empty.

The annotations example above gives these events. In the last row, the duration is 19.24 s, from the times, while the 2nd column says 19.

.. list-table::
   :header-rows: 1

   * - group
     - name
     - start_sec
     - duration_sec
     - channels
   * - flow
     - Hypopnea
     - 528.246
     - 12
     - []
   * - flow
     - Obstructive Apnea
     - 1564.219
     - 15
     - []
   * - flow
     - Obstructive Apnea
     - 2416.219
     - 70
     - []
   * - flow
     - Flow Limitation
     - 4977.63
     - 19.24
     - []


Unsupported format
-------------------

Snooz skips a DOMINO file in these cases, and the log file gives the reason.

* It has 2 columns, without a ``Signal ID``, a ``Start Time`` or a ``Rate``.
* It has 3 columns, without a ``Signal ID``, a ``Start Time`` or a ``Unit``.
* It has another number of columns, or no row.
* Its header is not followed by a blank line.

The recorded or computed values are skipped. Their files have a value at each time instead of events, and no ``Rate``, as in this example.

* Recorded or computed values 

    .. code-block:: rst

        Signal ID: SchlafFFT\AFV
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

    Look at the "Input Folders" step of the "Convert Annotations from DOMINOScreen" tool to know how to organize the files in order to convert them to the Snooz accessory .tsv file.


Version History
-----------------

* v2.0.0 : Distributed with CEAMS package version 7.2.0 — Snooz beta 2.0.1
    - Initial release of the tool.

* v2.2.0 : Distributed with CEAMS package version 7.3.0 — Snooz beta 3.0.0
    - UI improvements for consistent tool and input file descriptions.

* v2.2.1 : Distributed with CEAMS package version 7.5.0 — Snooz Toolbox 1.1.0
    - Updated the forms to the new look of Snooz Toolbox 1.1.0 (Inter font, light and dark themes).

* v2.2.2 : Distributed with CEAMS package version 7.6.0 — Snooz Toolbox 1.2.0
    - Redesigned the pages and the step descriptions of the tool, including the settings view of the Domino Converter module.
    - Corrected the introduction: the sleep profile is converted to sleep stages, and the .tsv file of each folder is replaced.
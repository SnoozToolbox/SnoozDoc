.. _Oxygen_saturation_report:

=========================
Report Oxygen Saturation
=========================

A tool to analyze oxygen saturation, detect oxygen desaturations, and export the :ref:`Oxygen_saturation_report_csv`.

Sleep staging is essential because oxygen saturation is particularly relevant during the sleep period (SP).
The SP is defined as the duration (in minutes) from the first epoch scored as sleep (N1, N2, N3, R) to the final awakening, including the last epoch scored as sleep.

The desaturation detector is inspired by ABOSA v1.2.2 [1], a freely available automatic oxygen saturation analysis software.
TODO for more information on the desaturation detection algorithm.

.. warning::

    The detector includes basic automatic artifact detection (limited to obvious artifacts). 
    Manual annotation of subtle artifacts is recommended prior to analysis. 
    The :ref:`Oximeter` viewer can be used to mark the invalid section. 

Steps
-----------------

| **Common settings** 
| Define the sleep cycles criteria for your study. 
| For more information, see :ref:`Sleep_Cycles_definition`.

**1 - Input Files**

Start by opening your PSG files (.edf, .sts or .eeg). 

- **European Data Format (EDF)** : 
  
  The corresponding .tsv file is required with .edf. Both files must be saved in the same directory and share the exact same filename.

- **Stellate format (up to version 6.2)** : 
  
  The corresponding .sig file is required with the .sts. Both files must be saved in the same directory and share the exact same filename.

- **NATUS format (version 9.1)** : 
  
  (*CEAMS users only*) The entire NATUS subject folder is required.

For more details on accepted formats, see :ref:`accepted_format`.

**2 - Invalid sections**

The user must select any annotations to be excluded from the oxygen saturation analysis.

**3 - Detection Settings**

The user must define the oxygen desaturation criteria, including:
- the oxygen drop threshold (%)
- the minimum desaturation duration (s)
- the maximum desaturation duration (s)

**4 - Output Files**

**Cohort Saturation Report**

The Oxygen Saturation Report for the cohort contains two main categories of metrics:

1. **Oxygen saturation variables** : minimum, maximum, and average oxygen saturation per recording, computed for:

- the full sleep period
- sleep halves and thirds
- individual sleep cycles
- sleep stages

2. **Oxygen desaturation variables** : including:

- oxygen desaturation index (ODI, events per sleep hour)
- severity (sum of areas under desaturation events, in percent·sec, over the sleep period)
- percentage of sleep time spent in desaturation
- average and median desaturation characteristics (duration, area, slope, drop)

All variables are computed for the total sleep period. 
Each recording is saved as one line in the cohort report, with new recordings appended to the existing file. 
The user specifies the file location to save the Cohort Oxygen Saturation Report.

**Optional outputs**

The detected desaturation events can be saved in the accessory file associated with the recording, for review.

The user can select an output directory to save the following outputs for each recording :

- A desaturation characteristics report, including:

   - start time (s)
   - duration (s)
   - slope (%/s)
   - depth (%)
   - area (%*s)

- The oxygen saturation graph, including invalid sections.

.. warning::

    For discontinuous recordings, the oxygen saturation graph is generated for each continuous recording session separately.

Report
---------

.. toctree::
   Oxygen_saturation_report/Oxygen_saturation_report_csv

References
----------
1. Karhu, T., Leppänen, T., Töyräs, J., Oksenberg, A., Myllymaa, S., & Nikkonen, S. (2022). ABOSA – Freely available automatic blood oxygen saturation signal analysis software : Structure and validation. Computer Methods and Programs in Biomedicine, 226, 107120. https://doi.org/10.1016/j.cmpb.2022.107120\n

Version History
-----------------

* v2.1.0 : Distributed with CEAMS package version 7.2.0 — Snooz beta 2.0.1
    - Initial release of the tool.

* v2.4.0 : Distributed with CEAMS package version 7.3.0 — Snooz beta 3.0.0
    - The desaturation detector is now inspired by ABOSA [1].
    - The desaturation severity has been added to the report.
   
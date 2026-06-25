.. _PSA_per_stage_info_csv:

===================================================
Spectral Power Report per Stages Definition
===================================================

The list of the variables included in the EEG spectral report per sleep stages. 

The reported spectral power is obtained by summing the spectral power over all frequency bins contained in the band defined by freq_low_Hz and freq_high_Hz.

**This results in units of µV²**, representing the signal variance within the selected frequency band.

Each frequency bin is included in exactly one band definition to ensure non-overlapping band power estimates when adjacent frequency bands are used.

.. note::

   To download the original info.tsv file : `snooz_beta_2_1_0_PSA_per_stages_info.tsv <https://f004.backblazeb2.com/file/snooz-release/doc/snooz_beta_2_1_0_PSA_per_stages_info.tsv>`_

.. csv-table:: EEG spectral power report per stages
   :file: snooz_beta_2_1_0_PSA_per_stages_info.tsv
   :delim: tab
   :align: left
   :class: left-align-caption wrap-table


.. _Connectivity_Analysis:

=======================
Connectivity Analysis
=======================

Description
-----------------------

The **Connectivity Analysis** module computes both functional and directional brain connectivity using two established EEG measures:

- **wPLI (Weighted Phase Lag Index)**: estimates non-zero-lag phase synchronization, minimizing volume conduction artifacts.
- **dPLI (Directed Phase Lag Index)**: estimates the direction of phase-lead/lag between pairs of EEG channels.

This tool automatically applies statistical correction using surrogate data testing and Wilcoxon signed-rank tests to retain only significant connections. It requires at least two clean brain channels and two valid epochs to run.

.. note::
   For optimal results, it is strongly recommended to preprocess your data using the **EEGInspector** app in Snooz. This allows you to mark and exclude:
   - Non-brain channels (e.g., EOG, EMG, ECG)
   - Noisy/bad channels
   - Noisy epochs

----

Steps
-----------------

**1 - Input Files**

   Start by opening your PSG files (.edf, .eeg or .sts).

   * The .tsv file is also needed for the EDF format.
   * The .sig file is also needed for Stellate format.
   * The whole NATUS subject folder is also needed for the .eeg format.

**2 - Events Exclusion**

   Use previously saved artifact annotations (e.g., from EEGInspector, Snooz artifact detection tool) to exclude noisy data from connectivity calculations.

.. important::

   Connectivity cannot be performed on:
   - Fewer than 2 channels
   - Fewer than 2 valid epochs

**3 - Filtering**

- **Frequency Band Selection**:  
  Choose a predefined band (Delta, Theta, Alpha, Beta, Full) or define a custom band to match your research question.

- **Recording Scope**:  
  Specify which annotated segments to use for connectivity (e.g., N2, REM, or unscored).  
  For sleep studies, select the appropriate stage. Otherwise, use unscored segments.

**4 - Connectivity Configuration**

- **Connectivity Type**:  
  Choose between wPLI or dPLI.

- **Epoch Parameters**:
  - Epoch length (seconds)
  - Epoch overlap (seconds)
  - Number of surrogates (for statistical testing)
  - P-value threshold (to retain only significant connections)

  Statistical testing ensures connections are not due to chance and provides more reliable connectivity estimates.

**5 - Output Files**

All files are saved in the selected Output folder, or next to the input file if "Save in the same folder" is checked.

Output files include:

- **Connectivity Matrix** (TSV)
  - File: ``<Filename>_{wpli|dpli}_convalue.tsv``

- **Connectivity Heatmap** (PNG)
  - File: ``<Filename>_{wpli|dpli}_conheatmap.png``
  - Visual matrix of the TSV data.

- **Head Connectivity Plot** (PNG, optional)
  - File: ``<Filename>_{wpli|dpli}_contopomap.png``
  - Saved only if a montage with ≥ 4 EEG channels is found.

Connectivity value ranges

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Measure
     - Range and interpretation
   * - wPLI
     - 0 to 1 (0 = no phase coupling; 1 = strong coupling)
   * - dPLI
     - 0 to 1 (0.5 = neutral; > 0.5 = leads; < 0.5 = lags)

Head connectivity plot elements

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Element
     - Description
   * - Nodes
     - EEG channels (connected = filled black; unconnected = white)
   * - Edges
     - wPLI: single color (darker means stronger); dPLI: gradient red -> purple -> blue (red = leader, blue = lagger)
   * - Styling
     - Edge thickness and opacity scale with connection strength


**Montage Handling**

- Montage is automatically selected from MNE built-ins.
- For HydroCel 128/129, face/neck sensors are removed to clean up the layout.

----

Display Thresholds
----------------------

Default thresholds for plotting:

**wPLI:**

- neutral_min = 0.05 (ignore below)
- moderate_min = 0.10 (thin & faint)
- strong_min = 0.20 (thick & dark)
- max_val = 0.40 (for opacity scaling)

**dPLI (bias = dPLI − 0.5):**

- neutral_abs = 0.01 (ignore below)
- moderate_abs = 0.02 (thin & faint)
- strong_abs = 0.08 (thick & dark)
- max_abs = 0.25 (for opacity scaling)

.. note::

   An auto-density option (e.g., "keep top 15% of connections") is implemented but currently disabled. It may be available in future versions.

----

References
-----------------

[1] Stam, C. J., & van Straaten, E. C. W. (2012). Go with the flow: Use of a directed phase lag index (dPLI) to characterize patterns of phase relations in a large-scale model of brain dynamics. NeuroImage, 62(3), 1415–1428. https://doi.org/10.1016/j.neuroimage.2012.05.050

[2] Vinck, M., Oostenveld, R., van Wingerden, M., Battaglia, F., & Pennartz, C. M. (2011). An improved index of phase-synchronization for electrophysiological data in the presence of volume-conduction, noise and sample-size bias. NeuroImage, 55(4), 1548–1565. https://doi.org/10.1016/j.neuroimage.2011.01.055

[3] Duclos, C., Maschke, C., Mahdid, Y., Nadin, D., Rokos, A., Arbour, C., Badawy, M., Létourneau, J., Owen, A. M., Plourde, G., & Blain-Moraes, S. (2023). Brain responses to propofol in advance of recovery from coma and disorders of consciousness: A preliminary study. American Journal of Respiratory and Critical Care Medicine, 207(5), 602–613. https://doi.org/10.1164/rccm.202105-1223OC

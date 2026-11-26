.. _ValidateSnoozTSVFile:

===============================
Validate Snooz TSV File
===============================

Description
-----------

The ``ValidateSnoozTSVFile`` tool is part of the CEAMS Toolbox and is used to validate the content and structure of TSV files. 
It checks the UTF-8 encoding of input files, verifies the column headers, inspects individual rows for correct data types and missing values,
and validates sleep stage annotations. Logs of all validation results are generated for review.

The tool is designed to process multiple files iteratively and produce a separate log for each file.


Key Features
------------

- Ensures the file is UTF-8 encoded.
- Validates presence and order of required TSV columns.
- Checks for missing values or empty fields.
- Verifies data types per column (`str`, `int`, `float`).
- Checks for presence of sleep staging annotations (`group == "stage"`).
- Detects unrecognized or discouraged sleep stage labels (e.g., `4`).
- Outputs structured logs for each file in the specified directory.



Inputs
------

**files** : ``List[str]``  
    A list of TSV files to be validated.

**log_path** : ``str``  
    Path to the directory where validation log files will be saved.


Outputs
-------

**output_logs** : ``<filename>_validation_log.txt``  
    A text file containing the validation results for each input file.
    The log includes information about encoding, column headers, data types, missing values, and sleep stage annotations.


Expected Column Format
----------------------

Each TSV file is expected to have the following five columns, in order:

- ``group`` (str) — category of the annotation (e.g., ``stage``)
- ``name`` (str or int) — label or identifier of the annotation
- ``start_sec`` (float or int) — annotation start time in seconds
- ``duration_sec`` (float or int) — annotation duration in seconds
- ``channels`` (str) — channels to which the annotation applies

A sixth column, ``time elapsed (HH:MM:SS)``, is accepted after them.


Validation Logic
----------------

1. **Encoding Check**: Confirms the file is UTF-8 encoded.
2. **Header Check**: Verifies that the header matches the expected columns exactly.
3. **Row-by-Row Validation**:
   - Ensures each line has the correct number of tab-separated columns.
   - Validates that required fields are present and non-empty.
   - Confirms the correct data types for each field.
4. **Sleep Stage Validation**:
   - Detects if the file includes a `group` labeled ``stage``.
   - Validates stage labels using the predefined dictionary of acceptable values, which is compatible with PSGReader.
   - Detects use of discouraged stage values like ``4``.


Errors and Logs
---------------

If issues are detected during validation, they are logged in the corresponding ``_validation_log.txt`` file in the `log_path` directory.
Each error includes the row number and a description of the problem.


Version History
-----------------

* v0.0.0 : Distributed with CEAMS package version 7.2.0 — Snooz beta 2.0.1
    - Initial release of the tool.
* v2.0.0 : Distributed with CEAMS package version 7.3.0 — Snooz beta 3.0.0
    - Supports the new optional time elapsed column.

* v2.0.1 : Distributed with CEAMS package version 7.5.0 — Snooz Toolbox 1.1.0
    - Updated the forms to the new look of Snooz Toolbox 1.1.0 (Inter font, light and dark themes).

* v2.0.2 : Distributed with CEAMS package version 7.6.0 — Snooz Toolbox 1.2.0
    - Redesigned the pages and the step descriptions of the tool. The introduction lists all the checks of the validation.
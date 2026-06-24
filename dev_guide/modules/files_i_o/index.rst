Files I/O
=========

.. toctree::
   :maxdepth: 1

   CsvReaderMaster
   DetectionsCohortReview
   DominoConverter
   EDFAnnotationsReader
   EdfXmlReader
   EdfXmlReaderMaster
   EdfXmlWriter
   EventReader
   JsonPathEditorMaster
   PSACohortReview
   PSGReader
   PSGWriter
   RenameFileList
   SleepStagesImporter
   TSVValidatorMaster
   TsvWriter

Quick reference
---------------

.. list-table::
   :widths: 25 15 60
   :header-rows: 1
   :align: left
   :class: left-align-caption wrap-table

   * - Module
     - Version
     - Description
   * - :ref:`Csv Reader Master <module_csvreadermaster>`
     - 2.0.0
     - Reads events from a CSV file.
   * - :ref:`Detections Cohort Review <module_detectionscohortreview>`
     - 2.1.0
     - Reads the spindle/sw output files and generates the "Detected events cohort report" file clean or transposed.
   * - :ref:`Domino Converter <module_dominoconverter>`
     - 2.1.0
     - Converts DOMINO accessory files (ASCII) in one Snooz accessory tsv file.
   * - :ref:`EDF Annotations Reader <module_edfannotationsreader>`
     - 2.0.0
     - Used to read the EDF Annotations signal and create a pandas dataframe with the events.
   * - :ref:`Edf Xml Reader <module_edfxmlreader>`
     - 2.0.0
     - Reads events from a EDF.XML file.
   * - :ref:`Edf Xml Reader Master <module_edfxmlreadermaster>`
     - 2.0.0
     - Reads events from a EDF.XML files or .XML files.
   * - :ref:`Edf Xml Writer <module_edfxmlwriter>`
     - 2.0.0
     - Creates an XML file based on compumedic format.
   * - :ref:`Event Reader <module_eventreader>`
     - 3.0.0
     - Reads events from a Tsv file.
   * - :ref:`Json Path Editor Master <module_jsonpatheditormaster>`
     - 2.0.0
     - Edits JSON files by replacing paths within the JSON structure.
   * - :ref:`PSA Cohort Review <module_psacohortreview>`
     - 2.5.0
     - Reads the PSA output file and generates the PSA file clean or transposed.
   * - :ref:`PSGReader <module_psgreader>`
     - 2.5.0
     - Reads a PSG file.
   * - :ref:`PSGWriter <module_psgwriter>`
     - 2.3.0
     - Writes a PSG file.
   * - :ref:`Rename File List <module_renamefilelist>`
     - 2.1.0
     - Renames files based on input parameters such as prefix.
   * - :ref:`Sleep Stages Importer <module_sleepstagesimporter>`
     - 2.1.0
     - Imports sleep stages from a textfile into the sleep_stages dataframe.
   * - :ref:`TSV Validator Master <module_tsvvalidatormaster>`
     - 2.0.0
     - Validates TSV files by checking their encoding and structure.
   * - :ref:`Tsv Writer <module_tsvwriter>`
     - 2.0.0
     - Saves events to a CSV file.

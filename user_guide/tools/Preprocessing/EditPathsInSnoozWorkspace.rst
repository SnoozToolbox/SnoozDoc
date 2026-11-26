.. _EditPathsInSnoozWorkspace:

===============================
Edit Paths in Snooz Workspace
===============================

This tool helps you update the internal paths in your Snooz workspaces (JSON files) to ensure compatibility across different systems.


Key Features
----------------

1. Path Adaptation

      - Automatically updates paths stored in Snooz workspace files when transferring them to a different machine or environment
      - Finds the absolute Windows paths (``C:/`` or ``C:\``) and the network paths (``//`` or ``\\``) written in the workspaces


2. System Compatibility
      - Shows the paths with ``/`` as separator, Windows paths written with ``\`` included
      - Adjusts for changes in directory depth or structure

How to Use
-----------

 - Select one or more Snooz workspaces (with .json extension), or choose an entire folder
 - Snooz can batch-process multiple workspaces at once
 - A warning is shown if an edited path does not exist
 - Preview all path changes before running the tool or saving the modified files in the select all mode
 - **A warning** is displayed if the exact same path appears in more than one selected workspace. To avoid confusion during path replacement, users must load only workspaces with unique paths.

.. note::
      Please ensure that all intended workspaces **are selected** before running the tool. If no workspaces are selected, the path modifications will not be applied, even if the workspaces are loaded.


Input
-----
 - Snooz workspace files (.json)
 - Paths as plain strings inside the workspace
 - Output folder and suffix for saving modified files


Output
------
 - Updated Snooz workspace files with updated paths, saved in the output folder as ``<name>_<suffix>.json`` (the original files are not changed)


Version History
-----------------

* v2.0.0 : Distributed with CEAMS package version 7.3.0 — Snooz beta 3.0.0
    - Initial release of the tool.

* v2.0.1 : Distributed with CEAMS package version 7.5.0 — Snooz Toolbox 1.1.0
    - Updated the forms to the new look of Snooz Toolbox 1.1.0 (Inter font, light and dark themes).

* v2.0.2 : Distributed with CEAMS package version 7.6.0 — Snooz Toolbox 1.2.0
    - Redesigned the pages and the step descriptions of the tool, including the settings view of the Json Path Editor Master module. The step Setting Step is now named Edit Paths.
    - Corrected the introduction: the paths found are the absolute Windows paths and the network paths, not the relative paths.
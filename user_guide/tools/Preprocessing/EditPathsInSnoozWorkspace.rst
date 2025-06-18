.. _EditPathsInSnoozWorkspace:

===============================
Edit Paths in Snooz Workspace
===============================

Description
-----------

This tool helps you update the internal paths in your Snooz workspaces (JSON files) to ensure compatibility across different systems.


Key Features
----------------

1. Path Adaptation

      - Automatically updates paths stored in Snooz workspace files when transferring them to a different machine or environment
      - Supports both absolute and relative paths


2. System Compatibility
      - Converts between Windows (\) and Unix (/) path formats
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
 - utput folder and suffix for saving modified files


Output
------
 - Updated Snooz workspace files with updated paths

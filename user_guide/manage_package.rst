.. _manage_package:

=======================
Snooz packages
=======================

In Snooz, a package is a structured folder hierarchy that groups related package items together. 

A package can contain four different types of items: 

1. **Modules** : Modules are building blocks to create an analysis pipeline called a process. A module is intended to accomplish a simple task such as filtering a signal.

2. **Process** : Process are built from interconnected modules to created a complete analysis pipeline, such as loading files, analysis them, and generating a report.

3. **Tools** : Tools are an abstraction layer over a process that provides a user-friendly step-by-step interface. (See :ref:`tools` for more information.)

4. **Apps** : An app is an application that operates within Snooz. (See :ref:`apps` for more information.)

.. note::

  A package can include a mix of different item types inside.  However, at CEAMS, we decided to create different packages for each item type.  For example, we have the packages CEAMSModules, CEAMSTools and CEAMSApps.


To manage the packages
=======================

To manage the packages via Snooz.

- Launch Snooz
- Navigate to **File -> Settings -> Packages**.
   - (On macOS : Navigate to **Snooz -> Preferences or Settings -> Packages**)

During the initial installation of Snooz, the packages that come with Snooz are activated (checked) by default. Each package can be expanded, allowing you to activate (check) or deactivate (uncheck) individual tools, modules or apps within the package.

    .. image:: ./packages.png
      :width: 1000
      :alt: Alternative text   


To add a package
---------------------

1. Press **Add from folder**.
2. Browse to the folder containing the tool or module package you want to add.  The folder must include the JSON file of the package (e.g., `ceams_package/moduled/CEAMSModules/CEAMSModules.json`).
3. Select the folder and press **Select Folder**. I.e. `CEAMSModules` folder.
4. Activate (check) the desired version of the package (tools or modules).
5. Deactivate (uncheck) any unwanted versions of the package (tools or modules).
6. Press **Apply**.
7. Close the window.
8. Verify the version of the tools available in the menu.

.. warning::
   
   **Packages in Development**

   Users may receive packages to validate before a Snooz release. The received zipped file typically includes two folders named with the version number, such as CEAMSModule_6_9_1 and CEAMSTools_6_9_1.
   To add the packages in Snooz, use the folders named **CEAMSModules** and **CEAMSTools** located within the version-numbered folders.


Problem with the Snooz Settings?
----------------------------------
When you reinstall Snooz or add/remove different packages (during development), 
you may encounter conflicting settings. Here is a procedure to reset Snooz to its default settings:

- Launch Snooz.
- Navigate to **File -> Settings -> General Settings** 
   - (On macOS : **Snooz -> Preferences or Settings -> General Settings**)
- Press **Reset to default**.  
- Close Snooz.
- Relaunch Snooz.

This will reset Snooz to its original state, with only the default packages added and activated.

If you're unable to launch Snooz on Windows (especially for developers), try removing the registry keys for Snooz:

 - Close Snooz
 - Open the Registry Editor (type **Registry Editor** in the Windows search bar)
 - Delete the **Snooz** folder under "HKEY_CURRENT_USER/Software/CEAMS"
 - Relaunch Snooz and manage your packages properly


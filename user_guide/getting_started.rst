.. _getting_started:

==========================
Getting Started with Snooz
==========================

The goal of this document is to  detail how to download, install and launch Snooz.

.. note::

  **CÉAMS members** if you need access to the Snooz Toolbox, which supports reading NATUS PSG files (version 9.1), please send an email to snooztoolbox.cnmtl@ssss.gouv.qc.ca—we'll be happy to assist!

.. _OS_Compatibility:

System Compatibility and Requirements for Snooz
====================================================

Windows
--------

Snooz has been developed and validated exclusively on Windows 11.

macOS
------

- Snooz is compatible only with Macs featuring the T2 security chip on Intel processors.  
- It is not supported on Macs with M1 or newer Apple Silicon processors.
- Snooz is compatible with macOS versions 14.3 (Sonoma) through 15.2 (Sequoia).

Linux
------

Snooz has been developed and validated on Ubuntu 22.04 LTS and should be compatible with Ubuntu 24.04 LTS.


First Snooz installation
==========================

The link to download the Snooz installer is provided by email. To request it, please visit https://snooztoolbox.com/ and fill out the form in the `Download section <https://snooztoolbox.com/download/>`_, then submit it.

On Windows platforms 
---------------------

1. Download the Installer using the link provided in the Snooz email after submitting your profile.
2. Double click on the zip file downloaded.
3. Double click on the SnoozSetup.exe included in the zip file.
4. Follow the instructions (make sure the previous version of Snooz is closed).

.. warning::  

    Snooz is not signed yet!
    If you get this warning below :  
     
    1. Click on More info.
    2. Select Run anyway.
    
    .. image:: ./Windows_protected.png
      :width: 700
      :alt: Alternative text    

The installation may take a few seconds.
When the installation is complete click “Next” to finish the install.
Click “Finish”.
You are done!

If you encounter issues, see the requirements in :ref:`OS_Compatibility`.

On macOS platforms
--------------------- 

1. Download the Installer using the link provided in the Snooz email after submitting your profile.
2. Double-click on the downloaded file to install.
3. Drag and drop the Snooz application in the Applications folder. 
4. Since Snooz is not signed yet, you need to mark it as an exception (see the note lower). 
5. To launch Snooz type the following in the terminal: ``/Applications/Snooz.app/Contents/MacOS/Snooz``

.. note::
  To mark Snooz as an exception: 
    | Open a terminal and type either :
    | ``find /Applications/Snooz.app -exec xattr -c {} \;`` or 
    | ``xattr -cr /Applications/Snooz.app``, depending on your environment.

.. warning::  
  Ensure that Snooz has full disk access to launch it from the Launchpad by following these steps:

     1. Open System Settings.
     2. Navigate to Privacy & Security.
     3. Click on Full Disk Access.
     4. If Snooz is not listed, click the + (plus) icon, then select Snooz from the Applications folder.
     5. Click Quit & Reopen when prompted.
     6. Relaunch Snooz.

  If Snooz does not have full disk access, it may hang when loading a file chosen via the Snooz interface.
  Launching Snooz from the terminal provides broader disk access than the Launchpad, so using the terminal is recommended if you prefer not to change the settings.

If you encounter issues, see the requirements in :ref:`OS_Compatibility`.

On Linux platforms
---------------------

1. Download the Installer using the link provided in the Snooz email after submitting your profile.
2. Install Snooz.
   
   Open the installer via the Ubuntu software center or Software install and click install  

   or install Snooz via the terminal : ``sudo dpkg -i SnoozSetup.deb``

.. note::
  Use the filename of the .deb file you have downloaded.

If you encounter issues, see the requirements in :ref:`OS_Compatibility`.

Launch Snooz
=================================

On Windows platforms
--------------------- 

Type Snooz in the Windows Search.

On MAC platforms
--------------------- 

Use Finder to locate Snooz in Applications.

On Linux platforms
--------------------- 

From the Applications -> Snooz


Update Snooz from the interface
=================================

1. Launch the Snooz application already installed on your desktop.  
2. Navigate to the menu Help > About Snooz (macOS : Snooz > About Snooz)
3. If the installed version is older than the released version **download** Snooz for your OS.
4. Close Snooz to avoid errors during the installation.  
5. (Optional) You can uninstall the previous version of Snooz to delete obsolete packages.  
6. Run the installer.  
7. After installation, launch the new version of Snooz.  
8. Activate the latest version of the packages you are interested in. Navigate to File > Settings > Packages (macOS Snooz > Preferences > Packages) in Snooz. Check/uncheck the right versions.
9. To activate only the most recent version of the packages installed with Snooz, you can press **Reset to default** in the General Settings.

.. warning::

  **CÉAMS members** if you need an update for the Snooz Toolbox, which supports reading NATUS PSG files (version 9.1), please send an email to snooztoolbox.cnmtl@ssss.gouv.qc.ca—we'll be happy to assist!   

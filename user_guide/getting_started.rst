.. _getting_started:

============================
Getting Started with Snooz
============================

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

Snooz supports both Intel-based Macs (including those with the T2 security chip) and Apple Silicon Macs (M1 and newer).
Supported macOS versions: 14.3 (Sonoma) through 15.2 (Sequoia).  

.. warning::

  Make sure to download the correct Snooz installer for your architecture. Two separate links are provided in the email and are clearly labeled: **Intel** and **arm64**.

Linux
------

Snooz is built on Ubuntu 22.04 LTS and tested on Ubuntu 24.04 LTS. It is expected to be compatible with recent Ubuntu LTS versions.


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

    - Two files are available: a **.deb** file and a **.zip** file. 
    - Recommended - Use the .deb file for easier installation (requires admin rights).
    - Alternative - Without admin rights, use the .zip file.

2. Recommended - Install Snooz via the **.deb** file.

    - Open the installer via the Ubuntu Software Center (or Software Install) and click Install. 

    - Or install Snooz via the terminal :

        - using dpkg (simple direct installation): ``sudo dpkg -i Snooz-Linux-xxx.deb``
        - using apt (resolves dependencies): ``sudo apt install Snooz-Linux-xxx.deb``

3. Alternative - Install Snooz via the **.zip** file.

    - Open a terminal in your Downloads folder and run: 

        - ``mkdir -p ~/.local/opt``
        - ``unzip Snooz-Linux-xxx.zip -d ~/.local/opt/``

.. note::
    Use the exact filename of the installer you downloaded.

If you encounter issues, see the requirements in :ref:`OS_Compatibility`.

Launch Snooz
=================================

On Windows platforms
--------------------- 

Type Snooz in the Windows Search.

On MAC platforms
--------------------- 

1. Use Finder to locate Snooz in Applications.

2. Or, launch Snooz from a terminal: 

   - Standard application launch (may require Full Disk Access): ``open -a Snooz`` 

   - Alternative launch method: ``/Applications/Snooz.app/Contents/MacOS/Snooz``

On Linux platforms
--------------------- 

1. From the Applications menu, click on **Snooz**.

2. Or, depending on the installation method, launch Snooz from a terminal:

   - For the `.deb` installation: ``/opt/Snooz/Snooz``

   - For the `.zip` installation: ``~/.local/opt/Snooz/Snooz``

Uninstall Snooz
=================================

On Windows platforms
---------------------
1. Open the Start menu and click on Settings (the gear icon).
2. Click on Apps.
3. In the Apps & features section, scroll down to find Snooz in the list of installed applications.
4. Click on Snooz, then click the Uninstall button that appears.

On MAC platforms
---------------------
1. Open Finder and navigate to the Applications folder.
2. Locate the Snooz application.
3. Right-click (or Control-click) on the Snooz application and select Move to Trash from the context menu.

On Linux platforms
---------------------
1. If you installed Snooz using the .deb file, open a terminal and run: ``sudo apt remove snooz``.
2. If you installed Snooz using the .zip file, simply delete the folder where you extracted the files (e.g., ``~/.local/opt/Snooz``).


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

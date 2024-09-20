.. _information:

=======================================
Information
=======================================

At this point, we assume you are familiar with the :ref:`installation`, know how to :ref:`run_snooz`, and have had a chance to :ref:`explore_ex`.

You are looking for more information about the Snooz architecture.  
Here some additional information about the **Packages**, **Tools**, **Modules** and **Apps**.

.. toctree::

  info_packages
  info_tools
  info_modules
  info_apps
  
Meet the managers
=======================================
Managers in Snooz are the core of the application. Each manager oversees a specific set of related features. 
For instance, the PackageManager handles loading and unloading packages and package items, 
while the ContentManager displays the content managed by other managers, such as the ProcessManager, the ToolManager, and the AppManager.

Interractions between managers
---------------------------------------------
Diagrams of the interactions between managers are presented below.

- User clicks on a tool in the menu and another tool was already loaded : 

  .. image:: ./open_tool_diagrame_sequence.png
    :width: 900
    :alt: Alternative text 


- A tool is being loaded after the user clicks on it in the menu.

  .. image:: ./steps_widget.png
    :width: 900
    :alt: Alternative text 


How module, tool and package versioning works
===============================================
The main purpose of versioning is to ensure the ability to reproduce older analyses, even if new developments change how modules and tools function. 

Package item interaction with endpoints and hooks
====================================================
Snooz is a highly flexible application. Endpoints and hooks were designed to facilitate communication between Apps and Tools, 
but this concept has been extended throughout the application to manage the interaction of PackageItems (Modules, Tools, Apps) with the core Snooz application.
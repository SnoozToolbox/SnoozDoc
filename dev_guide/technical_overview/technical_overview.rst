.. _technical_overview:

Technical Overview
==================

Snooz Toolbox is a Python 3.10 software for analyzing sleep recordings (Polysomnography). 
It is developed by the team at the CARSM (Center for Advanced Research in Sleep Medicine) in Montreal (http://ceams-carsm.ca/en/). 
Snooz is built using a cross-platform graphical interface framework called PyQt, making it compatible with Windows, Linux, and Mac computers. 
Fbs pro is used to package and distribute it as a standalone executable.

.. contents::
   :local:

The big picture
-----------------
Snooz is an analysis platform for sleep studies recordings (Polysomnography). 
It is a highly flexible and extensible software. 
However, this flexibility comes with the trade-off of increased complexity for software developers tasked with creating new features. 
The purpose of this documentation is to assist you in installing and setting up the development environment.

First, let's take a moment to understand how and why it functions the way it does.

Snooz can be adapted for any kind of field that uses some kind of process. 
This flexibility is made possible by the concept of Modules, Process, Tools and Apps.

1. **Modules** : Modules are building blocks to create an analysis pipeline called a process. A module is intended to accomplish a simple task such as filtering a signal.

2. **Process** : Process are built from interconnected modules to created a complete analysis pipeline, such as loading files, analysis them, and generating a report.

3. **Tools** : Tools are an abstraction layer over a process that provides a user-friendly step-by-step interface. (See :ref:`tools` for more information.)

4. **Apps** : An app is an application that operates within Snooz. (See :ref:`apps` for more information.)

To have more information about the architecture, see :ref:`information`.

Package and versioning
------------------------------
A challenge with a system like this is that when changes are made to a module, it has the potential to disrupt all processes and tools that depend on it. 
This poses issues on multiple fronts. 

* Firstly, it complicates the reproduction of past analyses. 
* Secondly, any modification to a module results in a cascade of adjustments needed for all tools utilizing it.

To address this challenge, we implement a concept of versioning and packages. 
Each module is assigned a specific version, and all modules are encapsulated within a package. 
When creating a process, the versions of the modules used are recorded. 
Upon reloading that process, Snooz identifies the corresponding package containing that module version and loads it into memory. 
This ensures that improvements made to the module over time do not jeopardize the functionality of previous tools.

Each tool also possesses a version and is contained within a package. 
In Snooz, the process of adding a new tool consists of importing a new package. 
This way, you can develop a new process with a step-by-step interface and new modules. 
Then, you only need to send your package to a colleague for them to start using it by importing it into Snooz.

To have more information about the versioning, see :ref:`versioning`.
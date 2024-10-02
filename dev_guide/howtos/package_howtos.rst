.. _package_howtos:

How Tos - Package
=================

Before creating your own package, module, or tool, you need to have a properly configured development environment for Snooz. See :ref:`installation` for more details.

Ensure that you have created your repository (e.g., my_snooz_repo) to manage your packages. See :ref:`run_snooz` for more details.  

It is assumed that you have already explored Snooz and have an understanding of its structure. See :ref:`explore_ex` for more details. 

.. contents::
   :local:

How to create create a package
--------------------------------

We use a command-line tool to help create a package. To access the terminal in VS Code, make sure to close Snooz beforehand. 

- In VS Code navigate to **Terminal -> New Terminal**
- Select your repository you forked from snooz_package_template (e.g. my_snooz_repo)
- Make sure the virtual environment **snooz_310_env** is activated (see :ref:`installation`)
- In the terminal type : ``python main_utils.py``
- Select **1- Create a package**
- Fill the information as follows (examples bellow):

   | -- Package Type --
   | Is this a package containing tools, modules, apps (t/m/a)? : t

   | -- Package Name --
   | Only letters, no space, camel case (ie: MyPackage): UserTools
   | This is a new package.
   |    Package author (optional): First name Last name
   |    Package description (optional): Package to test Snooz
   |    Package url (optional):[leave blank if not applicable]

You can now find your new package under the **tools**, **modules** or **apps** subfolder in your repository, depending on the package type you provided.
From here, you can create new modules, tools, and apps within this package.

To add your package and activate it in Snooz, see : :ref:`manage_package`.

.. Note::
   Note that you can move a module or a tool to another package, but you'll need to modify the **json** file of the old and new package.

How to release a new version of a package
-------------------------------------------

When you are ready to share your package with others, it's best practice to release your package to freeze the current version. 
We use a command-line tool to assist with the release process. To access the terminal in VS Code, make sure to close Snooz beforehand.

- In VS Code navigate to **Terminal -> New Terminal**
- Select your repository you forked from snooz_package_template (e.g. my_snooz_repo)
- Make sure the virtual environment **snooz_310_env** is activated (see :ref:`installation`)
- In the terminal, type : ``python main_utils.py``
- Select **6- Create a release package**

All the available packages in your repository will be copied under the **Release** folder in a new folder named according to the version of each package.

Here is an example of a release folder structure that includes 3 types of packages: 

- release/CEAMSApps_0_0_1/CEAMSApps
- release/CEAMSModules_6_10_0/CEAMSModules
- release/CEAMSTools_6_10_0/CEAMSTools

The idea is to share the folder named according to the version of the package in order to emphasize the version number.

How to import a package in Snooz
----------------------------------

To add your package and activate it in Snooz, see : :ref:`manage_package`.

How to update the package version
-----------------------------------------

The package version is specified in the JSON file that describes the package. To update the version, simply edit the JSON file manually.
Change the value of the ``package_version`` field.

For an example of a JSON file, see :ref:`info_packages`


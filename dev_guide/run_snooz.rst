.. _run_snooz:

=======================================
Run Snooz from the source code
=======================================

To run Snooz from the source code, you need to have your Snooz workspace configured for VS Code.  See :ref:`installation` for more details.

* Open VS Code
* Navigate to File-> Open workspace from file
* Choose the file snooz.code-workspace from the "snooz-toolbox" repository
* Navigate to Run -> Start Debugging (F5)

If everything is properly set up, the Snooz application should start.

Which tools do you want to run?
=======================================
Depending on your selection, follow the steps below.

.. contents::
   :local:

Tools released with Snooz
-------------------------------------------
Different versions of the CEAMS packages are available in the "snooz-toolbox" repository.
Those packages can be activated via the Snooz menu.

* Launch Snooz (F5)
* Navigate to File Menu from Snooz -> Settings -> Packages
* Check the desired packages. For more details see : :ref:`manage_package`.
* Tools will be availables from the Snooz menu. For more details see :ref:`tools`.

Tools from the development version
-------------------------------------------
You want to work with the latest development version of the CEAMS package?

* Clone the "snooz-package-ceams" repository into your "snooz_workspace" folder.

   - ``git clone https://github.com/SnoozToolbox/snooz-package-ceams.git``
   - See :ref:`installation` for more details about the "snooz_workspace" folder.

* Add the folder "snooz-package-ceams" into the VS Code workspace.

   - Open VS Code
   - Navigate to File-> Open workspace from file
   - Choose the file snooz.code-workspace from the "snooz-toolbox" repository
   - Navigate to File-> Add Folder to Workspace
   - Select the folder "snooz-package-ceams"
   - The file snooz.code-workspace in the "snooz-toolbox" folder will be updated automatically. 

* Add and activate the development version of the CEAMS package in Snooz.

   - Launch Snooz (F5)
   - In Snooz, navigate to File -> Settings -> Packages
   - Add the "snooz-package-ceams/modules/CEAMSModules" folder in the Snooz package settings
   - Add the "snooz-package-ceams/tools/CEAMSTools" folder in the Snooz package settings
   - Check these 2 packages
   - For more details, see :ref:`manage_package`

Tools from your own package
-------------------------------------------
You want to create modules and tools for your own purpose?
Fork and clone the "snooz-package-template" repository to get started with all the needed structure to develop a package within Snooz.

The "snooz-package-template" repository contains the empty structure needed to create your own modules, tools and apps. 

* Fork the "snooz-package-template" repository

   - go to `snooz-package-template <https://github.com/SnoozToolbox/snooz-package-template.git>`_
   - click on fork   
   - You should rename the repository to identify your work, e.g., my_snooz_repo.

* Clone your forked "snooz-package-template" repository, e.g., my_snooz_repo.
* Read the README.md in this repository to know how to use it.  Complete the setup before starting development.

* Add the folder of your new repository into the VS Code workspace.

   - Open VS Code
   - Navigate to File-> Open workspace from file
   - Choose the file snooz.code-workspace from the "snooz-toolbox" repository
   - Navigate to File-> Add Folder to Workspace
   - Select your folder, e.g., my_snooz_repo.
   - The file snooz.code-workspace in the "snooz-toolbox" folder will be updated automatically. 

For now, your repository contains only the provided examples, e.g., ExampleModulesPackage and ExampleToolsPackage.  
You can still add and activate these packages in Snooz, and you'll follow the same procedure with your own packages once they are created.

* Add and activate your the Example package in Snooz. 

   - Launch Snooz (F5)
   - In Snooz, navigate to File -> Settings -> Packages
   - Add the "my_snooz_repo/modules/ExampleModulesPackage" folder in the Snooz package settings
   - Add the "my_snooz_repo/tools/ExampleToolsPackage" folder in the Snooz package settings
   - For more details, see :ref:`manage_package`

We suggest exploring the provided examples before starting your own development. See :ref:`explore_ex` to continue.

.. note::

   **Syncing a fork**

   Sync your fork (e.g., "my_snooz_repo") to keep it up-to-date with the upstream repository "snooz-package-template".  
   You will be notified on GitHub if your fork is outdated compared to the upstream repository.
   Follow the guide on `syncing-a-fork <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork>`_ from GitHub.

.. toctree::

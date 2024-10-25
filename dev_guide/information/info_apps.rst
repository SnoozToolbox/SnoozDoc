.. _info_apps:

=======================================
Apps
=======================================

- For a gentle introduction, see :ref:`technical_overview`.
- (TO DO) To explore an app, see :ref:`explore_ex`.
- (TO DO)To know how to play with apps, see .

The details of the app are inside its JSON file (e.g. AppA.json)

.. code-block:: JSON

    {   
        "item_name": "AppA",
        "item_type": "app",
        "item_api_version": "1.0.0",
        "dependencies": [
            {
                "package_name": "ExampleAppsPackage",
                "package_version": "0.0.0",
                "deleteable": false
            },
            {
                "package_name": "CEAMSModules",
                "package_version": "6.9.0"
            }
        ],
        "app_params":{
            "app_label":"App A",
            "app_category":"Examples",
            "custom_endpoints": ["AppA_endpoint"]
        }
    }


The description of each needed attribute of the app : 
   
.. list-table:: 
   :widths: 50 50 50
   :header-rows: 1

   * - Attribute
     - Description
     - Notes
   * - item_name
     - The name of the app.
     - The name helps to identify the item, but we can find many instances of this item in the items list.
   * - item_type
     - The type of items.
     - Valid values are: **module**, **tool**, **process** and **app**.
   * - package_api_version
     - The version of the structure of this file. 
     - The api version is linked to the Snooz architecture (for Snooz beta the api version is 1.0.0).
   * - dependencies
     - A list of dictionnary that describes the package depedencies.
     - In the current example, its own package ExampleAppsPackage v0.0.0 and the CEAMSModules v6.9.0 are needed.
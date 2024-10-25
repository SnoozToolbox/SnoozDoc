.. _info_packages:

=======================================
Packages
=======================================

- For a gentle introduction, see :ref:`manage_package` and :ref:`technical_overview`.
- To explore a package, see :ref:`explore_ex`.
- To know how to play with packages, see :ref:`package_howtos`.

The details of the package are inside its JSON file (e.g. MyPackage.json)

.. code-block:: JSON

   {
      "package_name": "MyPackage",
      "package_version": "1.1.0",
      "package_author": "",
      "package_url": "",
      "package_description": "This is an example package",
      "package_api_version": "1.0.0",
      "items": [
         {
               "item_name": "AppZ",
               "item_type": "app",
               "item_version": "0.9.0",
               "item_hooks": [
                  {
                     "endpoint_name": "menu_endpoint",
                     "parameters": {
                           "menu_category": "CEAMS Apps",
                           "menu_label": "App Z"
                     }
                  }
               ]
         }
      ]
   }

The description of each needed attribute of the package : 
   
.. list-table:: 
   :widths: 50 50 50
   :header-rows: 1

   * - Attribute
     - Description
     - Notes
   * - package_name
     - The name of the package.
     - 
   * - package_version
     - The version of the package.
     - The version follows this guidelines : :ref:`versioning`.  This version may be used by other packages if any dependencies.
   * - package_api_version
     - The version of the structure of this file. 
     - The api version is linked to the Snooz architecture (for Snooz beta the api version is 1.0.0).
   * - items
     - The list of package items within the package.
     - Items can be either Modules, Tools, Process or Apps.
   * - items.item_name
     - The name of the package item.
     - The name helps to identify the item, but we can find many instances of this item in the items list.
   * - items.item_type
     - The type of items.
     - Valid values are: **module**, **tool**, **process** and **app**.
   * - items.item_version
     - The type of items.
     - For modules item, this must follow the guidelines : :ref:`versioning`.
   * - items.item_hooks
     - Which Snooz endpoint it will interact with.
     - For more details on hooks and endpoint : TODO.


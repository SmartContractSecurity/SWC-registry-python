Getting Started with swc-registry-python
========================================

SWC-registry-python is a python package for accessing SWC-registry content. 


Quick start
-----------

Assuming you have Python already:

.. sourcecode:: bash

    $ pip install swc-registry

Check the package work:

.. sourcecode:: python

    from swc_registry import SWC

    swc = SWC('SWC-100')
    print(swc.title)

    // Function Default Visibility


Get the latest content of SWC-registry
--------------------------------------

On first use of the SWC methods, the SWC registry is initialized from file (swc-definition.json) out cache. If user wants to get the latest information about SWC-registry he needs to pass the second argument of SWC class.

.. sourcecode:: python

    from swc_registry import SWC

    swc = SWC('SWC-100', True)
    print(swc.title)

    // Function Default Visibility
ABI Mapping Tools
=================

The **ABI Mapping Tools** are a collection of software tools to support the mapping of data onto scaffolds.

Adding Content
--------------

.. warning::

   Remove this section for an actual release!!

To add content to this repository, you will need to either edit restructured text files here or add a submodule for a mapping tool.
For content added through a submodule, you add an entry for the submodule in the table of content directives in the sections below.

Adding a submodule is simple::

 git submodule add https://<location-of-repository-here>

Where (hopefully it is obvious) you need to replace *<location-of-repository-here>* with an actual URL.

If you are using the `mapping tools template instructions <https://github.com/ABI-Tutorials/ABI-MappingTools-Documentation-Template>`_ you can add an entry into the table of contents similarly to what is already there.

Overview
--------

The **ABI Mapping Tools** is comprised of a large collection of disparate software packages.
In general the mapping tools are split into a user interface (UI) and engine.
The UI for mapping tools are provided as plugins for MAP Client.
The engines for mapping tools are standard Python packages that can be installed and utilised independently from the UI.

MAP Client
----------

The Musculoskeletal Atlas Project Client (MAP Client) is an open-source cross-platform framework for managing workflows.
A workflow, as far as MAP Client is concerned, consists of a number of connected workflow steps.
The MAP Client framework is a plugin-based application where the plugins are workflow steps.
MAP Client is a Python based application which makes use of the Qt widget library.

Documentation for the project can be found at `MAP Client documentation <https://map-client.readthedocs.io/en/latest/>`_.

MAP Client is available to download from `MAP Client download <https://github.com/MusculoskeletalAtlasProject/mapclient/releases>`_.
It is also available from `PyPI.org <https://pypi.org/project/mapclient/>`_, where you can install it with pip: :code:`pip install mapclient`.

To get the best out of the MAP Client you will need to get some plugins.
A collection of available plugins can be found at `MAP Client plugins <https://github.com/mapclient-plugins>`_.

UI Documentation
----------------

This section of the documentation covers the user interface plugins used in MAP Client.

.. toctree::
   :maxdepth: 1

   mapclientplugins.geometryfitter/docs/index
   mapclientplugins.scaffoldcreator/docs/index
   mapclientplugins.dataembedderstep/docs/index

Library Documentation
---------------------

This section of the documentation covers the libraries used behind the user interfaces.

.. toctree::
   :maxdepth: 1

   scaffoldmaker/docs/index
   opencmiss.maths/docs/index

Funding Agencies
----------------

The National Institutes of Health (NIH) have provided the funding for this work through the SPARC project.

.. image:: _images/sparc-logo.png
  :width: 400
  :alt: SPARC logo

Contributing Organisations
--------------------------

The Auckland Bioengineering Institute (ABI) has contributed to this work.

.. image:: _images/abi-logo.png
  :width: 150
  :alt: ABI logo


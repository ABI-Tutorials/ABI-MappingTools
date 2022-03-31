ABI Mapping Tools
=================

The **ABI Mapping Tools** are a collection of software tools to support the mapping of data onto scaffolds.

.. note::

   This project is under active development.

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
   :titlesonly:

   mapclientplugins.meshgeneratorstep/docs/index

Engine Documentation
--------------------

This section of the documentation covers the engines used behind the user interfaces.

.. toctree::
   :titlesonly:

   scaffoldmaker/docs/index

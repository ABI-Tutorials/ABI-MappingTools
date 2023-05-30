ABI Mapping Tools
=================

The **ABI Mapping Tools** are a collection of software tools to support the mapping of data onto scaffolds.

In general the mapping tools are split into a user interface (UI) and enginei (a software library).
The UI for mapping tools are provided as plugins for MAP Client.
The engines for mapping tools are standard Python packages that can be installed and utilised independently from the UI.

MAP Client
----------

The Musculoskeletal Atlas Project Client (MAP Client) is an open-source cross-platform framework for managing workflows.
A workflow, as far as MAP Client is concerned, consists of a number of connected workflow steps.
The MAP Client framework is a plugin-based application where the plugins are workflow steps.
MAP Client is a Python based application which makes use of the Qt widget library.

.. container:: tocdescr

   .. container:: descr

      :doc:`Installing MAP Client <mapclient/docs/getting_started/install-mapclient>`

   .. container:: descr

      :doc:`About MAP Client <mapclient/docs/index>`


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


.. container:: global-index-toc

   .. toctree::
      :hidden:
      :caption: Getting Started
      :maxdepth: 1

      mapclient/docs/getting_started/install-mapclient.rst
      mapclient/docs/getting_started/install-plugins.rst
      mapclient/docs/getting_started/create-workflow.rst
      mapclient/docs/getting_started/help.rst

   .. toctree::
      :hidden:
      :caption: External setup
      :maxdepth: 2

      plugins/index.rst
      libraries/index.rst

   .. toctree::
      :hidden:
      :caption: Tutorials
      :maxdepth: 1
   
      mapclient/docs/manual/index.rst
      mapclient/docs/developer/index.rst

   .. toctree::
      :hidden:
      :caption: Versions
      :maxdepth: 1

      versions.rst

   .. toctree::
      :hidden:
      :caption: Appendix
      :maxdepth: 3

      glossary.rst

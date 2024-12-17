ABI Mapping Tools
=================

The **ABI Mapping Tools** are a collection of software tools to support the mapping of data onto scaffolds.

In general the mapping tools are split into a graphical user interface (GUI) and engine (a software library).
The GUI for mapping tools are provided as plugins for MAP Client.
The engines for mapping tools are standard Python packages that can be installed and utilised independently from the GUI.

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


Feedback
--------

You are welcome to submit feedback for the ABI Mapping Tools.
To submit feedback please use one of the following channels:

* E-mail mapping tools: `mapping.tools@sparc.science <mailto:mapping.tools@sparc.science>`_
* Report an issue on GitHub: https://github.com/MusculoskeletalAtlasProject/mapclient/issues/new/
* Create a Wrike ticket: `Scaffold mapping tools feedback <https://www.wrike.com/frontend/requestforms/index.html?token=eyJhY2NvdW50SWQiOjMyMDM1ODgsInRhc2tGb3JtSWQiOjU5NTQxOH0JNDc5MDcxNjE3MTY3MQkyYjJlMWExNzFmOTMxZDUxNDJkY2Y2YWNhOTJiNjg5NzMzYzVlYTc2NzU1YmM4NzljNzMxMWVmNmU2MDkyYzdk>`_

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


.. toctree::
   :hidden:

   mapclient/docs/index.rst

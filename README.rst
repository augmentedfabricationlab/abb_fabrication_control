============================================================
abb_fabrication_control: ABB Fabrication Control
============================================================

.. start-badges

.. image:: https://img.shields.io/badge/License-MIT-blue.svg
    :target: https://github.com/augmentedfabricationlab/abb_fabrication_control/blob/master/LICENSE
    :alt: License MIT

.. image:: https://travis-ci.org/augmentedfabricationlab/abb_fabrication_control.svg?branch=master
    :target: https://travis-ci.org/augmentedfabricationlab/abb_fabrication_control
    :alt: Travis CI

.. end-badges

.. Write project description

**A general fabrication control module for the ABB robots.**

**Quick links:** [compas docs](https://compas-dev.github.io/main/) | [compas_fab docs](https://gramaziokohler.github.io/compas_fab/latest/) | [compas_rrc_docs](https://compas-rrc.github.io/compas_rrc/latest/reference/index.html) | [rrc github repository](https://github.com/compas-rrc/compas_rrc) | [overview compas extensions](https://compas.dev/extensions.html) | [urdf and moveit tutorials](https://gramaziokohler.github.io/compas_fab/latest/examples/03_backends_ros/07_ros_create_urdf_ur5_with_measurement_tool.html) | [troubleshooting](#docker-troubleshooting)

Requirements
------------

* Operating System: **Windows 10 Pro** <sup>(1)</sup>.
* [Rhinoceros 3D 7.0](https://www.rhino3d.com/)
* [Anaconda Python Distribution](https://www.anaconda.com/download/): 3.x
* [Docker Community Edition](https://www.docker.com/get-started): Download it for [Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows). Leave "switch Linux containers to Windows containers" disabled.
* Git: [official command-line client](https://git-scm.com/) or visual GUI (e.g. [Github Desktop](https://desktop.github.com/) or [SourceTree](https://www.sourcetreeapp.com/))
* [ABB RobotStudio](https://new.abb.com/products/robotics/robotstudio/downloads): 6.08 (only available for Windows). After install, **make sure you add the latest RobotWare, 6.12.00 or newer** (`Add-Ins` -> `RobotApps` -> `Filter for RobotWare` and add the version `6.12.00` or newer in the drop-down menu to the right). Please find further instructions for the installation [here](README_ROBOTSTUDIO.md).
* [VS Code](https://code.visualstudio.com/) with the following `Extensions`:
  * `Python` (official extension)
  * `Docker` (official extension, optional)

<sup>(1): Windows 10 Home does not support running Docker.</sup>

Dependencies
------------

* [COMPAS RRC](https://github.com/compas-rrc/compas_rrc)

Getting Started
------------

### 1. Setting up the Anaconda environment with all dependencies

Execute the commands below in Anaconda Prompt:

#### Install Compas & Compas Fab
 
    (base) conda config --add channels conda-forge
    (base) conda create -n afc compas_fab --yes
    (base) conda activate afc

#### Install Compas RRC

    (ffc) conda install compas_rrc
    
#### Install on Rhino
    
    (ffc) python -m compas_rhino.install -v 7.0
    
#### Verify Installation

    (ffc) pip show compas_fab
    
    Name: compas-fab
    Version: 0.XX.X
    Summary: Robotic fabrication package for the COMPAS Framework
    ....
    
### 2. Cloning and installing the repository

#### Repository Cloning

* Create a workspace directory: C:\Users\YOUR_USERNAME\workspace
* Open Github Desktop and clone the repository [this repository](https://github.com/augmentedfabricationlab/afc_fabrication_control) into you workspace folder.

Credits
-------------

This package was created by Lidia Atanasova <lidia.atanasova@tum.de> `@lidiatanasova <https://github.com/lidiatanasova>`_ at `@augmentedfabricationlab <https://github.com/augmentedfabricationlab>`_

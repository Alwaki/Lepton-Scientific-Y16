# Lepton Scientific Y16

A short script to record quantitative images from FLIR Lepton cameras, using Purethermal board.

## Description

The Lepton camera is a small LWIR thermal camera, weighing close to 1g. There exist several boards which simplify interactions with this camera, and in this package we utilize the PureThermal 3.0 board. While it is easy to access data using the provided interface, using the data for scientific measurements requires further work. This script provides that functionality for those who want to use Y16 raw format with no automatic gain and normalization.

## Getting Started

Note: Tested on Ubuntu 22.04, using Lepton 3.5 and 3.1R, and Purethermal 3.0 board.

### Dependencies

* OpenCV2
* Numpy
* v4l2-ctl

### Executing program

from the appropriate folder, execute the code in terminal:

```
python camera.py
```
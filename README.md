<p align="center">
  <img src="logo/pydaq-logo.png" alt= “PYDAQ” class=“center” width="50%" height="50%">
</p> 

[![PyPI version](https://img.shields.io/pypi/v/pydaq?color=a26969)](https://github.com/samirmartins/pydaq)
[![License](https://img.shields.io/pypi/l/pydaq?color=a26969)](https://opensource.org/licenses/BSD-3-Clause)
[![openissues](https://img.shields.io/github/issues/samirmartins/pydaq?color=a26969)](https://github.com/samirmartins/pydaq/issues)
[![issuesclosed](https://img.shields.io/github/issues-closed-raw/samirmartins/pydaq?color=a26969)](https://github.com/samirmartins/pydaq/issues)
[![downloads](https://img.shields.io/pypi/dm/pydaq?color=a26969)](https://pypi.org/project/pydaq/)
[![python](https://img.shields.io/pypi/pyversions/pydaq?color=a26969)](https://pypi.org/project/pydaq/)
[![status](https://img.shields.io/pypi/status/pydaq?color=a26969)](https://pypi.org/project/pydaq/)
[![contributors](https://img.shields.io/github/contributors/samirmartins/pydaq?color=a26969)](https://github.com/samirmartins/pydaq/graphs/contributors)
[![forks](https://img.shields.io/github/forks/samirmartins/pydaq?color=a26969&style=social)](https://github.com/samirmartins/pydaq/network/members)
[![stars](https://img.shields.io/github/stars/samirmartins/pydaq?color=a26969&style=social)](https://github.com/samirmartins/pydaq/stargazers)




# PYDAQ - Data Acquisition and Experimental Analysis with Python


----
Using Python for applications with experimental data (Arduino and NIDAQ boards)
----

This package was firstly designed to use experimental device for data 
acquisition and signal generator, when performing different experiment, 
such as a step-response test. 

Despite this, one can use PYDAQ to acquire and send a signal from 
any system, using different boards [(check examples folder)](examples), 
through a Graphical User Interface or via command line. In this sense
the user is capable to generate a customized signal which can be easily
applied to a system. 

It is noteworthy that this application makes data acquisition and 
empirical experiments simpler, faster and easier. This is relevant
when the user needs empirical data to construct black box linear and
nonlinear models, commomly used in research projects in forecasting and 
model-based control schemes.
 
The code provided here allows user to save acquired data in .dat files in 
a path specified by the user (or at Desktop, if no path is provided), as well
as send a user-defined data, which can be any nonlinear input signal 
[(you are strongly advised to check the )](https://samirmartins.github.io/pydaq/)

In what follows you will find

- Installation and Requirements
- Quick view and Main features 
- Using Graphical User Interfaces



---
Installation and Requirements
---

The fastest way to install PYDAQ is using pip:

```console
pip install pydaq
```

PYDAQ requires:

- Installed driver of the board used (Arduino or National Instruments NIDAQ)
- nidaqmx (>=0.6.5) for data acquisition from National Instruments Boards
- matplotlib (>=3.5.3) as a visualization tool
- numpy (>=1.22.3) to process data
- PySimpleGUI (>=4.60.3) as a Graphical User Interface
- PyQt5 as a backend for PySimpleGui
- pyserial (>=3.5) to manage data to/from Arduino


---
Quick view and Main features
---

| Feature                      |                                                                                                                                                                                                                                          Description |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Send Data (NIDAQ)            |                                                                                                                                                   This feature allows the user to send data through any NIDAQ board using a graphical user interface |
| Send Data (Arduino)          |                                                                                                                                               This feature allows the user to send data through any Arduino board through a graphical user interface |
| Get Data (NIDAQ)             |                                        Here the user is able to get data from a NIDAQ board, using any terminal configuration (Diff, RSE, NRSE), sample time and other parameters. Acquired data can also be saved and plot for further applications |
| Get Data (Arduino)           |                                                                                                    Here the user is able to get data from an Arduino board, using several options. Acquired data can also be saved and plot for further applications |
| Step Response (NIDAQ) |   In this feature one can perform an automatic step response experiment using a NIDAQ board. Data genereted by the experiment can also be saved to be used in further applications, such as obtaining linear and nonlinear models from acquired data |
| Step Response (Arduino)      | In this feature one can perform an automatic step response experiment using an Arduino. Data genereted by the experiment can also be saved to be used in further applications, such as obtaining linear and nonlinear models from acquired data |
 

---
Using Graphical User Interfaces (more details in [documentation](https://samirmartins.github.io/pydaq/) and [examples](examples)):
---

Graphical User Interface (NIDAQmx):

```python
from pydaq.get_data import Get_data

g = Get_data()
g.get_data_nidaq_gui()
```

Command line (NIDAQmx):

```python
from pydaq.get_data import Get_data

g = Get_data("Dev1", "ai0", 0.5, 10.0, True, "C:\\Users\\Samir\\Desktop", True)
g.get_data_nidaq()
```


![Graphical User Interface PYDAQmx](figures/gui.png)

![Data Acquired - Visual](figures/data_acquired.png)

![Data Acquired - .dat](figures/data.png)
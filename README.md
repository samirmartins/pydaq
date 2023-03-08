<p align="center">
  <img src="logo/pydaq-logo.png" alt= “PYDAQ” class=“center” width="40%" height="40%">
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
Using Python for applications with experimental data (NIDAQmx)
----

This project uses python for data acquisition and empirical experiments. 
It was firstly designed to be used as a data acquisition system 
when acquiring data for a step-response experiment. 

Despite this, one can use PYDAQ to acquire signal from 
any system, using different boards [(check examples folder)](examples), 
without any line of code. 

The code provided here allows user to save acquired data in .dat files in 
a path specified by the user (or at Desktop, if no path is provided)

You can find below some examples from the GUI (Graphical 
User Interface).

---
Quick view
---

![Graphical User Interface PYDAQmx](figures/gui.png)

![Data Acquired - Visual](figures/data_acquired.png)

![Data Acquired - .dat](figures/data.png)


---
To install:
---

Just as another Python package, run:

```python
pip install pydaq
```

---
To use (more details in [examples](examples)):
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
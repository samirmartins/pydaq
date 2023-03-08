<p align="center">
  <img src="docs/img/logo.png" alt= “PYDAQ” class=“center” width="70%" height="70%">
</p> 

# PYDAQ

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
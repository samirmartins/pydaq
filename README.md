# PYDAQmx

----
Using Python for applications with NIDAQmx boards
----

This project uses python for data acquisition. It 
was designed to be used as a data acquisition system 
when acquiring data for a step-response experiment. 

Despite this, one can use PYDAQmx to acquire signal from 
any system, using any NIDAQmx board, without any line 
of code. It will save acquired data in .dat files in 
a path specified by the user (or at Desktop, if no 
path is provided)

You can find below some examples from the GUI (Graphical 
User Interface).

---
Quick view
---

---
To install:
---

Just run:

```python
pip install pydaqmx
```

---
To use:
---

Graphical User Interface:

```python
from pydaqmx.step_response_gui import step_response_gui
step_response_gui()
```

Command line:

```python
from pydaqmx.step_response import step_response
step_response("AnalogInput", "ai0", 0.5, 10.0, True, "C:\\Users\\Samir\\Desktop")
```
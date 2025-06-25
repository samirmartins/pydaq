# Digital Filters NIDAQ

**NOTE**: Before working with PYDAQ, the device driver should be installed and working correctly as a DAQ (Data Acquisition) device.

## Controlling using Graphical User Interface (GUI)

Using the digital filters through the GUI is very simple, and with just two lines of code, you can open the GUI:

```python
from pydaq.pydaq_global import PydaqGui

PydaqGui()
```

After running the command, the GUI will appear. Navigate to the 'Get Data' screen, where you'll see a radio button to choose whether or not to apply the digital filters. When the 'Yes' option is selected, a new window will appear.

![](img/digital_filter_window.png)

## Parameters

- **Filter**: In this option you can choose your filter, if will be FIR or IIR.

- **Plot frequency response**: You can choose if in the end of the data acquisition if you would like to see the frequency response.

- **Filter design**: Here can you choose the design of your filter.

- **Order**: The user can entry with some value to choose the order of the filter.

- **Type**: The user can define the type of Filter, between "Lowpass, Highpass, Bandpass or Bandstop".

- **Cutoff** User can define the cutoff frequency.



# Sending Data with NIDAQ Boards

**NOTE**: before working with PYDAQ, device driver should be installed and working correctly as a DAQ (Data Acquisition) device  

## Sending Data using Graphical User Interface (GUI)

Using GUI to send data is really straighforward and require only 
three LOC (lines of code):

```python
from pydaq.send_data import Send_data

# Class Send_data
s = Send_data()

# Method send_data_nidaq_gui
s.send_data_nidaq_gui()
```

After this command, the following screen will show up, where the 
user is able to define parameters and start to acquire data.

![](/img/send_data_nidaq_gui.png)

The user is now able to select desired device, analog output channel and sample period. Also, 
the user will define if the data will or not be plotted. The data that will be sent should be in 
the output range defined, formated as one data per line and saved as a .dat file. After
configuration is done, the user only need to click on **SEND DATA** button to start the process.

## Sending data using command line

It will be presented how to use Send_data (and send_data_nidaq) to send a signal using a National Instruments board. 

Firstly, import library and define parameters: 

```python
# Importing PYDAQ
from pydaq.send_data import Send_data

# Defining parameters
device_name = "Dev1"
channel_used = "ao0"
sample_period_in_seconds = 1
data = [1,2,3,4,1,2,3,4,1,2,3,4] # It can be either a list or a numpy array
ao_min = 0 # Minimum allowed analog output value
ao_max = 5 # Maximum allowed analog output value
will_plot = True
```

Then, instantiate a class with defined parametes and send the data

```python
# Class Get_data
s = Send_data(data = data, 
              device=device_name, 
              channel= channel_used, 
              ts=sample_period_in_seconds,
              ao_min= ao_min, 
              ao_max=ao_max, 
              plot=will_plot)

# Method send_data_nidaq
s.send_data_nidaq()
```

If you choose to plot you can see the data sent on screen, i.e:

![](/img/sending_data_nidaq.png)

# Step response with NIDAQ boards

**NOTE 1**: before working with PYDAQ, device driver should be installed and working correctly as a DAQ (Data
Acquisition) device

## Step Response using Graphical User Interface (GUI)

Using GUI for step response is really straighforward and require only
two LOC (lines of code):

```python
from pydaq.pydaq_global import PydaqGui

# Launch the interface
PydaqGui()
```

After this command, the graphical user interface screen will show up, where the
user should select the NIDAQ option and go to the Step Response tab,
to be able to define parameters and start to acquire data.

![](img/step_response_nidaq_gui.png)

The user is now able to select desired NIDAQ device, analog input and
analog output channel, as well as analog input terminal configuration.
Step range and sample period can be adjusted along with session duration.
Step will be applied in the defined time. Also, the user will define if
the data will or not be plotted and saved.

## Step Response using command line

It will be presented how to use StepResponse (and step_response_nidaq) to
perform a step response experiment using an NIDAQ board.

Firstly, import library and define parameters:

```python
# Importing PYDAQ
from pydaq.step_response import StepResponse

# Defining parameters
device_name = "Dev1"
ao_channel_used = "ao0"
ai_channel_used = "ai0"
sample_period_in_seconds = 1
session_duration_in_seconds = 10.0
step_time_in_seconds = 3.0
step_min_in_volts = 0
step_max_in_volts = 5
terminal_configuration = 'Diff'
will_plot = "no" # Can be realtime, end or no
```

Then, instantiate a class with defined parametes and send the data

```python
# Class StepResponse
s = StepResponse(device=device_name,
                 ao_channel=ao_channel_used,
                 ai_channel=ai_channel_used,
                 ts=sample_period_in_seconds,
                 session_duration=session_duration_in_seconds,
                 step_time=step_time_in_seconds,
                 step_min=step_min_in_volts,
                 step_max=step_max_in_volts,
                 terminal=terminal_configuration,
                 plot_mode=will_plot)

# Method step_response_nidaq
s.step_response_nidaq()
```

If you choose to plot you can see the data sent on screen, i.e:

![](img/step_response_nidaq.png)

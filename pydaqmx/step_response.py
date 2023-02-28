import nidaqmx
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
from timesched import Scheduler
import numpy as np

def step_response(device="AnalogInput", channel = "ai0", ts = 1.0, session_duration = 60.0, save = False, path = None):
    """
        This function can be used for data acquisition and step response experiments using Python + NIDAQmx boards.

    :author: Samir Angelo Milani Martins
             - https://www.samirmartins.com.br
             - https://www.github.com/samirmartins/

    :param:
        device: nidaqmx device from where data will be colected. Example: "AnalogInput"
        channel: channel from where data will be acquired. Example: ai0
        ts: sample period, in seconds.
        session_duration: session duration, in seconds.
        save: if True, saves data in path defined by path.
        path: where data will be saved.

    :return:

    :example:
        step_response("AnalogInput", "ai0", 1.0, 60.0, True, "C:\\Users\\Samir\\Desktop")
    """

    # Initializing variables
    data = []
    time_var = []

    # Number of cycles necessary
    cycles = int(np.floor(session_duration/ts))

    # Initializing device, with channel defined
    task = nidaqmx.Task()
    task.ai_channels.add_ai_voltage_chan(device+'/'+channel)

    # create the figure and axes objects
    fig, ax = plt.subplots()

    # Run GUI event loop
    plt.ion()

    # Title and labels and plot creation
    plt.title("Step Response", fontsize=20)
    plt.xlabel("Time")
    plt.ylabel("Voltage")
    line, = ax.plot(time_var, data)

    # Main loop, where data will be acquired
    for k in range(cycles):

        # Acquire data
        temp = task.read()

        # Wait for ts seconds
        time.sleep(ts)

        # Queue data in a list
        data.append(temp)
        time_var.append(k)

        # Update interface
        # updating data values
        line.set_xdata(time_var)
        line.set_ydata(data)
        fig.canvas.draw()
        fig.canvas.flush_events()
        ax.set_xlim([0, 1.1*session_duration])
        ax.set_ylim([-1.1*max(np.abs(data)), 1.1*max(np.abs(data))])

    # Closing task
    task.close()

    # Check if data will or not be saved, and save accordingly
    if save:
        # Checking if path were or not defined by the user
        if path is None: # Saving in Desktop if it is not defined
            path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

        # Saving time_var
        for t in time_var:
            file_time = open(path + '\\time.dat', 'w')
            file_time.write(str(t) + "\n")
            file_time.close()

        # Saving data
        for d in data:
            file_data = open(path + '\\data.dat', 'w')
            file_data.write(str(d) + "\n")
            file_data.close()

import nidaqmx
import time
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import numpy as np
import warnings

def step_response(device="AnalogInput", channel = "ai0", ts = 0.5, session_duration = 10.0, save = True, path = None):
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
        step_response("AnalogInput", "ai0", 0.5, 10.0, True, "C:\\Users\\Samir\\Desktop")
    """

    # Checking if path were or not defined by the user
    if path is None:  # Saving in Desktop if it is not defined
        path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

    # Check if able to save data in defined path
    if not os.path.exists(path):
        warnings.warn('Defined path does not exists! Please redefine path and run the code again')
        return

    # Initializing variables
    data = []
    time_var = []

    # Changing Matplotlib backend
    mpl.use('Qt5Agg')

    # Number of cycles necessary
    cycles = int(np.floor(session_duration/ts))

    # Initializing device, with channel defined
    task = nidaqmx.Task()
    task.ai_channels.add_ai_voltage_chan(device+'/'+channel)

    # create the figure and axes objects
    fig, ax = plt.subplots()
    fig._label = 'iter_plot' # Defining label


    # Run GUI event loop
    plt.ion()

    # Title and labels and plot creation
    plt.title("Step Response")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Voltage")
    plt.grid()
    line, = ax.plot(time_var, data)
    plt.show()

    # Main loop, where data will be acquired
    for k in range(cycles+1):

        # Acquire data
        temp = task.read()

        # Counting time to append data and update interface
        st = time.time()

        # Queue data in a list
        data.append(temp)
        time_var.append(k*ts)

        # Update interface

        # Checking if there is still an open figure. If not, stop the for loop.
        try:
            plt.get_figlabels().index('iter_plot')
        except:
            break

        # updating data values
        line.set_xdata(time_var)
        line.set_ydata(data)
        fig.canvas.draw()
        fig.canvas.flush_events()
        ax.set_xlim([0, 1.1*session_duration])
        ax.set_ylim([-1.1*max(np.abs(data)), 1.1*max(np.abs(data))])

        # Getting end time
        et = time.time()

        # Wait for (ts - delta_time) seconds
        try:
            time.sleep(ts + (st-et))
        except:
            warnings.warn("Time spent to append data and update interface was greater than ts. "
                          "You CANNOT trust time.dat")


    # Closing task
    task.close()

    # Check if data will or not be saved, and save accordingly
    if save:

        # Saving time_var
        file_time = open(path + '\\time.dat', 'w')
        for t in time_var:
            file_time.write(str(t) + "\n")
        file_time.close()

        # Saving data
        file_data = open(path + '\\data.dat', 'w')
        for d in data:
            file_data.write(str(d) + "\n")
        file_data.close()

    return

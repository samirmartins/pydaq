import nidaqmx
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

def step_response(device="AnalogInput", channel = "ai0", ts = 1.0, session_duration = 600, save = False, path = None):
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
        step_response("AnalogInput", "ai0", 1.0, 600, True, "C:\Users\Samir\Desktop")

    """

    # Initializing variables
    data = []
    time = []

    # Number of cycles necessary
    cycles = session_duration/ts

    # Initializing device, with channel defined
    task = nidaqmx.Task()
    task.ai_channels.add_ai_voltage_chan(device+'/'+channel)

    # Create the figure and axes objects
    fig, ax = plt.subplots()

    # Main loop, where data will be acquired
    for k in range(cycles):

        # Acquire data
        temp = task.read()

        # Wait for ts seconds
        time.sleep(ts)

        # Queue data in a list
        data.append(temp)
        time.append(k)

        # Update Interface


    # Check if data will or not be saved, and save accordingly
    if save:
        # Checking if path were or not defined by the user
        if path is None: # Saving in Desktop if it is not defined
            path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

        file_time = open(path+'\\time.dat', 'w')
        for t in time:
            file_time.write(str(t) + "\n")
        file_time.close()

        file_data = open(path+'\\data.dat', 'w')
        for d in data:
            file_data.write(str(d) + "\n")
        file_data.close()



    ################ Melhorias: executar aquisição a cada ts segundos (planejado), e não com sleep. Com sleep não é tão preciso como com scheduler.

    #
    # from random import randint
    #
    # import matplotlib.pyplot as plt
    # from matplotlib.animation import FuncAnimation
    #
    # # create empty lists for the x and y data
    # x = []
    # y = []
    #
    # # create the figure and axes objects
    # fig, ax = plt.subplots()
    #
    # def animate(i):
    #     pt = randint(1, 9)  # grab a random integer to be the next y-value in the animation
    #     x.append(i)
    #     y.append(pt)
    #
    #     ax.clear()
    #     ax.plot(x, y)
    #     ax.set_xlim([0, 20])
    #     ax.set_ylim([0, 10])
    #
    # ani = FuncAnimation(fig, animate, frames=20, interval=500, repeat=False)
    #
    # plt.show()

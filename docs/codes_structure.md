# PyDAQ Structure

The PyDAQ project is divided into various parts that handle different functionalities. The entire code structure is contained within the `pydaq` folder, which includes the following main divisions:

## Main Layout
The PyDAQ layout is organized into several tabs, including:
- **Get Data**: For data acquisition.
- **Send Data**: For sending data.
- **Step Response**: For step response functionality.

### Relevant Files
If you encounter any mathematical errors or want to modify functionalities and contribute to the project, the relevant files are:

- **pydaq/get_data.py**: Related to data acquisition.
- **pydaq/send_data.py**: Manages data transmission.
- **pydaq/step_response.py**: Handles the step response.
- **pydaq/pydaq_global.py**: Contains general functions for PyDAQ’s interaction with Arduino and NIDAQ.

Once you locate the relevant code, you will also have access to comments explaining the functionality of each section, helping you better understand how the code works and where to make modifications.

## Contributing to Design, Fixing Typos or Adding a New Widget

If you're interested in contributing to the PyDAQ design or have spotted typographical errors and want to correct them, access the `uis` folder. The interfaces were created using [Qt Design Studio](https://doc.qt.io/qtdesignstudio/). To modify the interface, follow these steps:

1. **Install Qt Design Studio** on your computer.
2. **Access the interface files**: Here are 2 examples of the 8 ui files we have.
   - **pydaq/uis/PyDAQ_Base.ui**: Contains the layout for the main menu.
   - **pydaq/uis/PyDAQ_get_data_Arduino_Widget.ui**: Layout for the widget related to data acquisition via Arduino.

### Adding or Modification and Saving
After making changes to the design, save the files as Python files `.py`. Here are 2 examples files that clearify naming conventions:
- For the main menu: `pydaq/uis/ui_PyDAQ_Base.py`
- For the Get Data widget: `pydaq/uis/ui_PyDAQ_get_data_Arduino_widget.py`

By following this convention, you ensure proper integration with the rest of the PyDAQ system, contributing through github, as seen [here](CONTRIBUTING.md)
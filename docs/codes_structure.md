# PyDAQ Structure

The PyDAQ project is divided into various parts that handle different functionalities. The entire code structure is contained within the `pydaq` folder, which includes the following main divisions:

## Main Layout

The PyDAQ layout is organized into several tabs, including:

- **Get Data**: For data acquisition.
- **Send Data**: For sending data.
- **Step Response**: For step response functionality.
- **PID Control**: For implementing a PID controller.
- **Get Model**: For extracting or loading models from system identification.

### Relevant Files

If you encounter any mathematical errors or want to modify functionalities and contribute to the project, the relevant files are:

- **pydaq/get_data.py**: Related to data acquisition.
- **pydaq/send_data.py**: Manages data transmission.
- **pydaq/step_response.py**: Handles the step response.
- **pydaq/pid_control.py**: Implements the PID control logic.
- **pydaq/get_model.py**: Responsible for loading and managing system models.
- **pydaq/pydaq_global.py**: Contains general utility functions for PyDAQ’s interaction with Arduino and NIDAQ.

Once you locate the relevant code, you will also have access to comments explaining the functionality of each section, helping you better understand how the code works and where to make modifications.

## Contributing to Design, Fixing Typos or Adding a New Widget

If you're interested in contributing to the PyDAQ interface design, correcting typographical issues, or integrating a new widget, head to the `uis` folder. The interfaces were created using [Qt Design Studio](https://doc.qt.io/qtdesignstudio/), but you can also use the Qt Designer bundled with `pyside6`.

### Editing UI Files

To modify the interface:

1. **Install Qt Design Studio** or run `pip install pyside6` and use the Qt Designer that comes with it.
2. **Access the `.ui` files** and open them in the designer.
3. You can export the layout directly to Python code using the "Save As Python File" option if using the PySide6 Designer.

If you're using another method, you can also manually convert the `.ui` file to `.py` using:

```bash
pyuic6 NameOfFile.ui -o ui_NameOfFile.py
```

#### Example Files

- **pydaq/uis/PyDAQ_Base.ui**: Contains the layout for the main menu.
- **pydaq/uis/PyDAQ_get_data_Arduino_Widget.ui**: Layout for the Arduino data acquisition widget.

### Integrating New Widgets

- If you're **adding a new widget** to the main interface (`PyDAQ_Base.ui`), you **must use the promoted widget feature** inside the Qt Designer to correctly embed your custom widget.
- If you're only **modifying an existing promoted widget**, such as `pydaq/uis/PyDAQ_get_data_Arduino_Widget.ui`, you can save it directly as a `.py` file using the Python export option from the Designer (if using `pyside6`). 

> Make sure to **preserve the naming convention** (e.g., `ui_<OriginalFileName>.py`) to ensure seamless integration with the PyDAQ backend logic.

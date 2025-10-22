Contributing
============

PYDAQ is intended to be a community project. You are more than welcome to contribute!

Bug reporting and New Features
----------------------------
If you find any bugs or have suggestions for new features,
please report them on [issue tracker](https://github.com/samirmartins/pydaq/issues) on GitHub.

Documentation
-------------

Documentation is as important as the library itself and PYDAQ documentation
can be found [here](https://samirmartins.github.io/pydaq/).
English is not my primary language, so if you find any typo or wrong phrases, do not hesitate to point me out.

Development environment
-----------------------

These are some basic steps to help us with coding:

1. Install and Setup Git on your computer.
3. [Fork PYDAQ](https://help.github.com/articles/fork-a-repo/)
4. [Clone the fork on your local machine](https://help.github.com/articles/cloning-a-repository/)
5. Install it in editable mode using
   ```console
   pip install -e /path/to/pydaq
   ```   
6. Create a new branch.
7. Make changes following the coding style of the project (or suggesting improvements).
8. Run the tests.
9. Write and/or adapt existing test if needed.
10. Add documentation if needed.
11. Commit.
12. [Push to your fork](https://help.github.com/articles/pushing-to-a-remote/)
13. [Open a pull request!](https://help.github.com/articles/creating-a-pull-request/)

---

# PYDAQ Structure

The PyDAQ project is divided into various parts that handle different functionalities.  
All the core source code is contained within the `pydaq/` directory.

---

## 📁 Relevant Files

Below is a summary of the key files and their roles within the `pydaq/` folder:

| File | Description |
|------|--------------|
| `pydaq/get_data.py` | Implements the data acquisition logic and filters. |
| `pydaq/send_data.py` | Implements the data sending logic. |
| `pydaq/step_response.py` | Implements the step response logic. |
| `pydaq/pid_control.py` and `pid_control_window_dialog.py` | Implement the PID control logic. |
| `pydaq/get_model.py` | Implements the system model identification logic. |

All files include **inline comments** and **function docstrings** to help you understand their purpose and how to safely modify or extend their behavior.

---

## 🧩 Contributing to Interface Design, Fixing Typos, or Adding Widgets

If your contribution involves **interface design**, **layout adjustments**, or **adding new widgets**,  
you’ll be working in the `pydaq/uis/` folder.

The user interfaces are built using [Qt Design Studio](https://doc.qt.io/qtdesignstudio/),  
but you can also use the **Qt Designer** that comes with `PySide6` (recommended).

### Editing `.ui` Files

1. Install Qt Design Studio, or install `pyside6`:
   ```bash
   pip install pyside6
   ```
2. Open the desired `.ui` file (for example, `PYDAQ_Base.ui`) in Qt Designer or Qt Design Studio.  
3. To export the layout directly to Python, use **"Save As Python File"** inside the Designer.  
   Alternatively, you can convert it manually via:
   ```bash
   pyuic6 NameOfFile.ui -o ui_NameOfFile.py
   ```

### Example Files

| File | Description |
|------|--------------|
| `pydaq/uis/PYDAQ_Base.ui` | Layout for the main PyDAQ window. |
| `pydaq/uis/PYDAQ_get_data_Arduino_Widget.ui` | Layout for the Arduino data acquisition widget. |

---

## 🧱 Integrating New Widgets

- When **adding a new widget** to `PYDAQ_Base.ui`, use the **Promote Widget** feature inside Qt Designer to properly integrate your custom widget into the PyDAQ application.  
- If you’re **modifying an existing promoted widget**, simply re-export the `.ui` file as a `.py` module.  
- Keep the naming pattern `ui_<OriginalFileName>.py` to ensure the application can import your updated interface automatically.

---

## 🔍 Where to Start When Contributing

If you are unsure where to start contributing:

- **For logic improvements:** check the corresponding `.py` file under `pydaq/`.  
- **For UI changes:** explore the `.ui` files in `pydaq/uis/`.  
- **For bug fixes:** look into the related functional area (PID, data acquisition, etc.).  

Each function and class is **documented** to make it easier to understand the flow before implementing your changes.

---

## ✅ Summary

| Area | Folder | What You’ll Find |
|------|---------|------------------|
| Core logic | `pydaq/` | Main Python modules for control, data handling, and modeling |
| Interfaces | `pydaq/uis/` | `.ui` design files for GUI layouts |
| Programming | `pydaq/guis/` | `.py` files generated from `.ui` layouts |
| Utilities | `pydaq/utils/` | Common utility functions and helper methods |
| Documentation | `docs/` | Project documentation and usage guides |

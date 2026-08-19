# Launch & customize from a script

You can start the GUI from a Python session or script instead of the
`mmgui` CLI — useful for integrating it with other Python code or
customizing it before it appears.

## Basic launch

```python
from pymmcore_gui import create_mmgui

create_mmgui()
```

This initializes the application and shows the main GUI window, blocking on
the Qt event loop until the window is closed.

## Customizing before launch

Pass `exec_app=False` to get the main window back without starting the
event loop, so you can modify it first:

```python
from pymmcore_gui import create_mmgui
from pymmcore_gui._qt.QtWidgets import QApplication

# (you do not need to create a QApplication instance yourself)

window = create_mmgui(exec_app=False)

# customize the app or window here
# window.mmcore  # the CMMCorePlus instance used by the GUI

QApplication.instance().exec()  # start the Qt event loop
```

## Using an existing `CMMCorePlus` instance

If you already have a `CMMCorePlus` instance you want the GUI to control,
pass it directly:

```python
from pymmcore_plus import CMMCorePlus
from pymmcore_gui import create_mmgui

core = CMMCorePlus()
core.loadSystemConfiguration()

create_mmgui(mmcore=core, mm_config=False)  # mm_config=False: don't reload a config
```

By default (`mmcore=None`), the GUI uses the global `CMMCorePlus.instance()`
singleton if one exists, or creates a new one.

See [`create_mmgui`](../reference/api.md#pymmcore_gui.create_mmgui) for the full
parameter reference, including disabling the exception hook or telemetry
prompt.

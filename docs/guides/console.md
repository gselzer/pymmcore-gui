# Use the interactive console

`pymmcore-gui` includes an embedded IPython console (`qtconsole`-based),
useful for scripting one-off device interactions, inspecting state, or
prototyping acquisition logic without leaving the app.

Open it from the **Widgets** toolbar, the **Window** menu, or
++ctrl+shift+c++.

## What's available

The console starts with a few names already in scope:

| Name | What it is |
| --- | --- |
| `mmc`, `core`, `mmcore` | The running `CMMCorePlus` instance (same one the GUI's widgets are all connected to) |
| `mda` | The `CMMCorePlus.mda` `MDARunner`, for starting/observing acquisitions |

All top-level names from `pymmcore_plus` and `pymmcore_gui` are also
available without importing them.

## Example

```python
# snap and inspect an image directly
mmc.snapImage()
img = mmc.getImage()
img.shape

# list loaded devices
mmc.getLoadedDevices()

# subscribe to acquisition events
mmc.mda.events.frameReady.connect(lambda img, event, meta: print(event.index))
```

Because this is the same `mmc` instance driving the GUI, any changes you
make (loading a config, moving a stage, changing a property) are reflected
immediately in the open panels, and vice versa.

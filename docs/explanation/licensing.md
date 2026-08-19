# Licensing

`pymmcore-gui` itself, and all pymmcore-plus ecosystem projects, are
provided under the [BSD-3-Clause license](https://github.com/pymmcore-plus/pymmcore-gui/blob/main/LICENSE).

## Why the bundled app is GPL

The [bundled application](../install.md#bundled-application)
currently includes [PyQt6](https://riverbankcomputing.com/software/pyqt/),
which is licensed under the GNU General Public License v3.0. Because it's
statically bundled together, the **bundled application** is distributed as
a combined work under the terms of the GPLv3 — even though the
`pymmcore-gui` source code itself remains BSD-3-Clause.

If you install `pymmcore-gui` as a Python package and bring your own Qt
bindings, you are not bound by this: installing with `PySide6` instead of
`PyQt6` avoids the GPL dependency entirely, since PySide6 is LGPL-licensed.
See the `pyside` dependency group in `pyproject.toml` for how to switch
bindings in a development install.

If the GPL bundled app is limiting for your use case, please [open an
issue](https://github.com/pymmcore-plus/pymmcore-gui/issues) — a
PySide6-based bundle may be possible in the future.

## Micro-Manager core & device adapters

`pymmcore-gui` depends on the [C++ MMCore and
Devices](https://github.com/micro-manager/mmCoreAndDevices), which are
licensed under a mix of LGPL and BSD-3-Clause, depending on the specific
device adapter or module.

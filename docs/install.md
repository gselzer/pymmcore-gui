# Install

This page describes the various pathways to get `pymmcore-gui` running on your machine:

## Bundled app

For a fully self-contained, double-clickable app (includes the Python
runtime and all dependencies — nothing else to install), download a
pre-built bundle:

| Platform | Download |
| :------: | -------- |
| Windows | [pymmgui-Windows.zip](https://nightly.link/pymmcore-plus/pymmcore-gui/workflows/bundle/main/pymmgui-Windows.zip) |
| macOS | [pymmgui-macOS.zip](https://nightly.link/pymmcore-plus/pymmcore-gui/workflows/bundle/main/pymmgui-macOS.zip) |

Extract the archive and run the application inside.

!!! important
    The bundled application does **not** include Micro-Manager device
    adapters — install them separately via **Devices > Install Devices...**
    in the GUI, or see [Install device adapters](guides/device_adapters.md).

## Python package

Installing as a Python package is the better option if you want to
[script or embed the GUI](guides/scripting.md), or run it inside an existing Python environment.

`pymmcore-gui` isn't on PyPI yet, so install directly from GitHub:

=== "pip"

    ```sh
    pip install git+https://github.com/pymmcore-plus/pymmcore-gui
    ```

=== "uv"

    ```sh
    uv pip install git+https://github.com/pymmcore-plus/pymmcore-gui
    # or, to add it to a project:
    uv add git+https://github.com/pymmcore-plus/pymmcore-gui
    ```

A Qt binding ([PyQt6](https://riverbankcomputing.com/software/pyqt/)) is
pulled in automatically — you don't need to install one yourself. See
[Choosing a Qt binding](#choosing-a-qt-binding) below if you'd rather use
PySide6.

Then install the Micro-Manager device adapters and launch:

```sh
mmcore install   # installs device adapters — see guides/device_adapters.md
mmgui            # launches the app
```

!!! note "Pin a commit for reproducible installs"
    Since the GitHub `main` branch may change at any time, pin a specific
    `<commit>` if you're adding this as a project dependency:

    ```toml
    [project]
    dependencies = [
        "pymmcore-gui @ git+https://github.com/pymmcore-plus/pymmcore-gui@<commit>"
    ]
    ```

## Choosing a Qt binding

By default, installing `pymmcore-gui` pulls in
[PyQt6](https://riverbankcomputing.com/software/pyqt/) — this is a hard
dependency, so there's nothing extra to configure for a normal install.
PyQt6 is GPLv3-licensed, which has implications if you redistribute an app
built on top of `pymmcore-gui` — see [Licensing](explanation/licensing.md).

[PySide6](https://www.qt.io/qt-for-python) (LGPL) is supported as an
alternative binding, but currently requires a source install with the
`PySide6` dependency group — see
[Installing for development](#installing-for-development) below.

## Installing for development

To work on `pymmcore-gui` itself, clone the repo and install with
[uv](https://docs.astral.sh/uv/getting-started/installation/):

```sh
git clone https://github.com/pymmcore-plus/pymmcore-gui.git
cd pymmcore-gui
uv sync
uv run mmgui
```

To use PySide6 instead of the default PyQt6 in a development install:

```sh
uv sync --group pyside --no-install-package PyQt6 --no-install-package PyQt6Ads
```

See [Contributing](contributing.md) for testing, linting, and bundle-build
instructions.

## Verifying your installation

```sh
mmgui --version
```

prints the installed `pymmcore-gui`, `pymmcore-plus`, and `pymmcore`/
`pymmcore-nano` versions — useful when reporting a bug.

## Next steps

- New to the app? Follow the [tutorial](tutorial.md).
- Ready to connect real hardware? See
  [Connect to real hardware](guides/hardware.md).
- Looking for a specific `mmgui` flag? See the [CLI reference](reference/cli.md).

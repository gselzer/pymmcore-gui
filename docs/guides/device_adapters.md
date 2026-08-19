# Install device adapters

`pymmcore-gui` needs Micro-Manager's C++ device adapters on your system
(these ship separately from the Python packages, since they're
platform-specific compiled libraries). There are three ways to get them:

## From within the GUI

**Devices > Install Devices...** opens an install widget
(`pymmcore-widgets`' `InstallWidget`) that lets you pick a Micro-Manager
version and install its device adapters without leaving the app. This is
the easiest option for the [bundled application](../install.md#bundled-application),
which does not include device adapters.

## From the command line

```sh
mmcore install
```

If you don't have `pymmcore-plus[cli]` installed in your environment, you
can still run it via `uv`:

```sh
uv run --with pymmcore-plus mmcore install
```

*(requires [uv](https://docs.astral.sh/uv/getting-started/installation/))*

## Manual installation

Install the [latest Micro-Manager nightly
build](https://micro-manager.org/Micro-Manager_Nightly_Builds) directly.
`pymmcore-plus` will look for it on the standard Micro-Manager installation
paths — see [pymmcore-plus: Installing Micro-Manager device
adapters](https://pymmcore-plus.github.io/pymmcore-plus/install/#installing-micro-manager-device-adapters)
for how the search path works, and how to override it with
`MICROMANAGER_PATH`.

# Tutorial: Your First Acquisition

This tutorial walks through installing `pymmcore-gui`, launching it, and
running your first multi-dimensional acquisition — using Micro-Manager's
built-in demo devices, so no real hardware is required.

## 1. Install

```sh
pip install git+https://github.com/pymmcore-plus/pymmcore-gui
```

`pymmcore-gui` needs the Micro-Manager device adapters. Install them with:

```sh
mmcore install
```

!!! tip
    You can also download a pre-built, double-clickable application bundle
    instead of installing via `pip`. See [Install](install.md)
    for both options.

## 2. Launch with the demo configuration

```sh
mmgui --demo-config
```

The main window appears with the demo devices already loaded: a simulated
camera, stage, and light path. You should see a toolbar across the top and
several docked panels — a **Config Groups** panel and an **MDA** panel are
open by default.

## 3. Snap and preview a live image

Click the camera icon (**Snap**) in the toolbar, or press ++ctrl+k++. A
preview window opens showing a simulated image from the demo camera. Click
the live-mode icon (or press ++ctrl+l++) to stream continuously instead of
snapping single frames.

## 4. Set up a simple acquisition

Open the **MDA** panel (it's open by default; if you've closed it, reopen it
from the **Window** menu or with ++ctrl+shift+m++). This panel is built from
`pymmcore-widgets`' `MDAWidget`, and lets you define a
[useq-schema](https://pymmcore-plus.github.io/useq-schema) acquisition:

1. Under **Time**, enable a short time series (e.g. 3 timepoints, 1 second
   apart).
2. Under **Channels**, add the `DAPI` and `FITC` channels from the demo
   configuration.
3. Leave **Z Stacks** and **Positions** unchecked for now.

## 5. Run it

Click **Run**. The acquisition starts, and each frame streams into the image
preview as it's acquired. When it finishes, the full stack is available for
viewing in the viewer's dimension sliders (timepoint, channel).

## Next steps

- To connect to real hardware instead of the demo config, see
  [Connect to real hardware](guides/hardware.md).
- To explore the full range of acquisition options (z-stacks, positions,
  grids), see [Run a multi-dimensional acquisition](guides/mda.md).
- To save acquired data to disk, see [Save to OME-TIFF / OME-Zarr](guides/saving.md).

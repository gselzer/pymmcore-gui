# Run a multi-dimensional acquisition

The **MDA** panel (open by default, or reopen with ++ctrl+shift+m++) lets
you define and run rich imaging protocols using
[useq-schema](https://pymmcore-plus.github.io/useq-schema). It's built on
`pymmcore-widgets`' `MDAWidget`.

## Building a sequence

The panel exposes one tab per acquisition axis:

- **Time** — number of timepoints and interval
- **Z Stacks** — range/step, or a list of explicit positions, relative to
  current or absolute stage position
- **Channels** — one or more channels from your loaded config's `Channel`
  group, each with its own exposure time
- **Positions** — an XY (and optionally Z) position list, or a grid
  generated over a plate/region

Axes can be freely combined and reordered — useq-schema will interleave them
according to the order you choose (e.g. channels-within-z, or z-within-time).

## Saving acquired data

By default, `pymmcore-gui`'s MDA panel writes acquired data **in-memory**
(so you can inspect it in the viewer without configuring an output path
first). To persist data to disk as it's acquired, set a save location and
writer format — see [Save to OME-TIFF / OME-Zarr](saving.md).

## Running, pausing, and canceling

Click **Run** to start. While running, the panel's **Run** button becomes
**Pause**/**Cancel** controls. Progress and the current frame are reflected
live in the image preview.

## Watching progress programmatically

Because `pymmcore-gui` is built on `pymmcore-plus`, all the usual
[MDA events](https://pymmcore-plus.github.io/pymmcore-plus/guides/events/)
(`frameReady`, `sequenceStarted`, `sequenceFinished`, etc.) are available on
`mmcore.mda.events` if you're driving or observing the acquisition from the
[console](console.md) or a script.

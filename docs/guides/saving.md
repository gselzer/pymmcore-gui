# Save to OME-TIFF / OME-Zarr

By default, the [MDA panel](mda.md) keeps acquired data in memory only. To
write data to disk as it's acquired:

1. In the MDA panel's **Save** section, check **Save to disk**.
2. Choose a destination directory and a base filename.
3. Choose a writer format from the dropdown — `pymmcore-gui` writes via
   [`ome-writers`](https://github.com/pymmcore-plus/ome-writers), supporting:
    - **OME-TIFF**
    - **OME-Zarr**

Metadata (stage positions, exposure times, timestamps, channel/config
info) is captured from each frame's useq-schema `MDAEvent` and written
alongside the pixel data.

!!! note "Work in progress"
    File I/O and metadata preservation are an active area of improvement.
    If you hit a gap (a missing metadata field, an unsupported layout), please
    [open an issue](https://github.com/pymmcore-plus/pymmcore-gui/issues).

## Saving programmatically

If you're driving the acquisition from the [console](console.md) or a
script rather than the MDA panel, pass an output path/writer directly to
`mmcore.run_mda(...)` — see [pymmcore-plus: The Acquisition
Engine](https://pymmcore-plus.github.io/pymmcore-plus/guides/mda_engine/)
for details on writer options at that layer.

# Connect to real hardware

By default, if no configuration is loaded, `pymmcore-gui` uses
Micro-Manager's demo devices so you can try the app without hardware. To
connect to a real microscope, you need a Micro-Manager hardware
configuration file (`.cfg`).

## Option 1: Build a config with the Hardware Config Wizard

Open **Devices > Hardware Config Wizard...** (or press its toolbar/menu
shortcut). The wizard walks through:

1. Selecting device adapters and adding devices
2. Assigning device roles (camera, focus/Z stage, XY stage, shutter, etc.)
3. Grouping properties into config groups and presets (e.g. a `Channel`
   group with `DAPI`/`FITC` presets)
4. Saving the result to a `.cfg` file

This is the same wizard used by classic MMStudio, wrapped as a
`pymmcore-widgets` `ConfigWizard`.

## Option 2: Load an existing config file

If you already have a `.cfg` file (e.g. exported from MMStudio, or shared by
a labmate):

- **Devices > Load System Configuration...** — opens a file picker
- Or launch with `mmgui --config path/to/your.cfg`

## Saving changes

After editing devices/groups/presets (via the wizard or the **Config
Groups** / **Property Browser** panels), save back to disk with
**Devices > Save System Configuration...**.

## Troubleshooting

If loading a configuration fails with a device-adapter or "incompatible
interface version" error, see [Troubleshooting](../troubleshooting.md).

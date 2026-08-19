# Configure application settings

`pymmcore-gui` persists user preferences (window layout, last-used config,
telemetry opt-in, etc.) to a JSON settings file, managed with the `mmgui
settings` command.

```sh
# open the settings file in your default editor
mmgui settings --edit

# reveal the settings file in your file explorer / Finder
mmgui settings --reveal

# erase all settings and restore defaults
mmgui settings --reset
```

Running `mmgui settings` with no flags prints the location of the settings
file (and help text).

For the structure of the settings file itself, see the [settings
schema](../reference/settings-schema.md) reference. Settings can also be
overridden per-launch with environment variables — see [Environment
variables](../reference/env-var.md).

!!! tip "Resetting just the layout"
    If only your window/panel layout is misbehaving, `--reset` is a bigger
    hammer than you probably need — it also clears your last-used config
    path and telemetry choice. See [Customize the layout](layout.md) for a
    more targeted reset.

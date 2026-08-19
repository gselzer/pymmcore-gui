# Troubleshooting

## "This app is going to destroy your computer!" / unsigned app warning

The [bundled application](install.md#bundled-application) isn't
currently code-signed, so macOS/Windows will warn you before letting it run.
You'll need to explicitly allow it (e.g. via "Open Anyway" in macOS System
Settings, or "More info > Run anyway" on Windows SmartScreen).

## Micro-Manager directory not found

```text
pymmcore-plus - ERROR - (_util.py:131) could not find micromanager directory. Please run 'mmcore install'
```

This means the app can't find the Micro-Manager device adapters. See
[Install device adapters](guides/device_adapters.md).

## Incompatible device interface version

```text
OSError: Line 7: Device,DHub,DemoCamera,DHub
Failed to load device "DHub" from adapter module "DemoCamera" [ ... Incompatible device interface version (required = 71; found = 70) ]
```

Your installed device adapters are out of date relative to `pymmcore-plus`.
Update them (e.g. `mmcore install`, or via **Devices > Install Devices...**
in the GUI) — see [Install device adapters](guides/device_adapters.md).

## The GUI opens but the panel I expect is missing

Panels stay closed/open based on your saved [layout](guides/layout.md).
Reopen a closed panel from the **Window** menu, or reset the layout entirely
with `mmgui settings --reset` (this also clears other saved preferences —
see [App settings](guides/settings.md)).

## An error/crash report dialog appeared

`pymmcore-gui` can optionally send anonymized crash reports to help
developers fix bugs — you're asked for consent the first time this comes
up, and can change your answer any time via
[app settings](guides/settings.md), or disable it entirely with `mmgui run
--no-telemetry`. See [Environment variables](reference/env-var.md) for the
underlying toggles.

## Still stuck?

Please [open an issue](https://github.com/pymmcore-plus/pymmcore-gui/issues)
or ask on the [Image.sc forum](https://forum.image.sc/tag/pymmcore-plus).

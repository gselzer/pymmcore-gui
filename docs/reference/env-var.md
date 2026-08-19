# Environment Variables

The following environment variables configure `pymmcore-gui`. Boolean
variables can be set to `1`, `0`, `True`, or `False` (case insensitive).

## App settings overrides

These mirror fields in the [settings file](settings-schema.md) (prefix
`PMM_`), and take precedence over the saved settings file:

| Variable | Description | Default |
| --- | --- | --- |
| **`PMM_SEND_ERROR_REPORTS`** | Send error reports to the developers. Unset means "ask". | unset |
| **`PMM_LAST_CONFIG`** | Path to the last-used Micro-Manager config file. | unset |
| **`PMM_AUTO_LOAD_LAST_CONFIG`** | Automatically reload `PMM_LAST_CONFIG` on startup without prompting. | unset |
| **`PMM_FALLBACK_TO_DEMO_CONFIG`** | Load the demo config if no other config is found. | `False` |

## Error reporting / telemetry

| Variable | Description | Default |
| --- | --- | --- |
| **`MM_TELEMETRY_SHOW_HOSTNAME`** | Include hostname in error reports. | `"0"` (disabled) |
| **`MM_TELEMETRY_SHOW_LOCALS`** | Include local variables in error report tracebacks. | `"1"` (enabled) |
| **`MM_TELEMETRY_DEBUG`** | Enable Sentry SDK debug logging. | unset |

Use `mmgui run --no-telemetry` (or `create_mmgui(install_sentry=False)`) to
disable error reporting entirely for a session — see the
[CLI reference](cli.md).

## Debugging

| Variable | Description | Default |
| --- | --- | --- |
| **`MMGUI_DEBUG_EXCEPTIONS`** | Drop into `pdb` on an unhandled exception in the GUI. | unset |
| **`MMGUI_EXIT_ON_EXCEPTION`** | Exit the process after handling an unhandled exception (useful in CI). | unset |

## Inherited from pymmcore-plus

`pymmcore-gui` sets
[`PYMM_SIGNALS_BACKEND`](https://pymmcore-plus.github.io/pymmcore-plus/env_var/)`=qt`
by default on import, so that core events integrate with the Qt event loop.
See the [pymmcore-plus environment variables
reference](https://pymmcore-plus.github.io/pymmcore-plus/env_var/) for the
rest — those apply here too, since `pymmcore-gui` is built directly on
`CMMCorePlus`.

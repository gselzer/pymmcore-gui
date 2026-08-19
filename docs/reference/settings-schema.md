# Settings file schema

`pymmcore-gui` stores user preferences as JSON. Find its location with
`mmgui settings` (no flags), or open it directly with `mmgui settings
--edit`. See [Configure application settings](../guides/settings.md) for the
CLI.

Values are loaded with the following precedence (highest first): values
passed programmatically, environment variables (prefixed `PMM_`, see
[Environment variables](env-var.md)), a `.env` file, then this settings
file.

::: pymmcore_gui._settings.SettingsV1
    options:
      filters: ["!^model_config$"]

::: pymmcore_gui._settings.WindowSettingsV1
    options:
      filters: ["!^model_config$"]

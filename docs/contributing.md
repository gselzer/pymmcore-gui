# Contributing

Thanks for thinking of a way to help improve this project! Contributions
come in all shapes and sizes beyond writing code — improving
[documentation](#contributing-documentation), opening
[issues](https://github.com/pymmcore-plus/pymmcore-gui/issues) for bugs,
asking for clarification on things you find unclear, and requesting new
features are all valuable.

## Contributing code

All development happens in the
[pymmcore-plus/pymmcore-gui](https://github.com/pymmcore-plus/pymmcore-gui)
repo. Dependencies are managed with
[uv](https://docs.astral.sh/uv/getting-started/installation/):

```sh
git clone https://github.com/pymmcore-plus/pymmcore-gui.git
cd pymmcore-gui
uv sync
uv run mmgui       # run the app
uv run pytest      # run the test suite
uv run prek -a     # lint & type-check (must pass before merge, along with tests)
```

Use [conventional commits](https://www.conventionalcommits.org/) style
(`feat:`, `fix:`, `docs:`, `refactor:`, `test:`) for commit messages.

See the full [contributor guide](https://github.com/pymmcore-plus/pymmcore-gui/blob/main/CONTRIBUTING.md)
in the repo for details on the bundled-application build, settings/config
internals, and Qt backend switching (PyQt6 vs. PySide6).

## Contributing documentation

This site is built with [MkDocs](https://www.mkdocs.org/) from the files in
the `docs/` folder. To build and preview locally:

```sh
uv run --group docs mkdocs serve
```

The docs will be live at <http://127.0.0.1:8000> and update automatically as
you edit and save.

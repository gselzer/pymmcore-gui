# Architecture

`pymmcore-gui` is a thin composition layer: almost none of its functionality
is implemented from scratch. Instead, it wires together four libraries and
adds the application shell (window, menus, docking, persistence) around
them.

```text
┌─────────────────────────────────────────────────────────┐
│                      pymmcore-gui                        │
│   MicroManagerGUI (QMainWindow) · actions · settings      │
├───────────────┬───────────────┬──────────────┬───────────┤
│ pymmcore-plus │ useq-schema   │ pymmcore-     │    ndv    │
│ CMMCorePlus,  │ MDASequence,  │ widgets       │  image/   │
│ MDAEngine,    │ MDAEvent      │ Qt panels for │  stack    │
│ events        │               │ devices/MDA   │  viewer   │
└───────────────┴───────────────┴──────────────┴───────────┘
```

- **`pymmcore-plus`** owns the single source of truth: a `CMMCorePlus`
  instance (`window.mmcore`), reached via `CMMCorePlus.instance()` so that
  every widget and the console share it.
- **`useq-schema`** is the data model passed between the MDA panel and
  `CMMCorePlus.run_mda()` — it never touches Qt.
- **`pymmcore-widgets`** supplies the actual panel implementations (Property
  Browser, MDA widget, Config Groups, Stage Control, etc.); `pymmcore-gui`
  mostly instantiates and docks them, occasionally subclassing to adjust
  defaults (see `create_mda_widget` in `actions/widget_actions.py`, which
  hides the `tiff-sequence` writer and defaults to an in-memory save).
- **`ndv`** renders acquired/live frames in the image preview panels.

## The actions system

Every menu item, toolbar button, and dockable panel is backed by an
`ActionInfo` or `WidgetActionInfo` — a declarative description (key, label,
icon, shortcut, which dock area it prefers) rather than hand-wired
menu-building code. `MicroManagerGUI.MENUS` and `.TOOLBARS` are just
mappings from a menu/toolbar name to a list of these action keys (or a
callable that builds a `QMenu`/`QToolBar` directly, for more custom cases
like the Window menu). This is what makes it possible to reopen any panel
from the **Window** menu without every panel needing bespoke menu code — see
the [actions API](../reference/api.md#actions).

## Docking & persistence

Panel layout is managed by [Qt Advanced Docking
System](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System). Its
state, plus main-window geometry and the set of open panels, is serialized
into the [settings file](../reference/settings-schema.md) on close and
restored on the next launch — see [Customize the
layout](../guides/layout.md).

## Where this can break down

Because most panels are `pymmcore-widgets` components used close to
as-is, deep customization of an individual panel's behavior currently means
subclassing it in `pymmcore-gui` (as `create_mda_widget` does) rather than a
first-class plugin/extension mechanism. Improving this is one of the
project's stated goals.

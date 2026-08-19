# API Reference

`pymmcore-gui`'s public API is intentionally small: most users interact with
the application through the GUI or the [CLI](cli.md), not by importing
`pymmcore_gui` directly. The exceptions are for
[scripting/embedding](../guides/scripting.md) the app.

## Launching

::: pymmcore_gui.create_mmgui

## Main window

::: pymmcore_gui.MicroManagerGUI

## Actions

The actions system underlies the GUI's menus, toolbars, and keyboard
shortcuts — each menu item / toolbar button / dockable panel is backed by an
`ActionInfo` (or `WidgetActionInfo`) registered under a `CoreAction` or
`WidgetAction` key. See [Keyboard shortcuts](shortcuts.md) for the full,
generated list of built-in actions.

::: pymmcore_gui.ActionInfo

::: pymmcore_gui.CoreAction

::: pymmcore_gui.WidgetAction

# Customize the layout

`pymmcore-gui`'s panels are dockable, using [Qt Advanced Docking
System](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System)
(via `PyQt6Ads`/`PySide6-QtAds`). You can:

- **Drag** a panel's title bar to dock it to a different edge, or float it
  as its own window
- **Tab** panels together by dragging one onto another
- **Close** a panel with its title-bar close button, or toggle it from the
  **Window** menu
- **Reopen** any closed panel from the **Window** menu, which lists every
  widget action not already pinned to another menu (Devices, etc.)

## Toolbars

Toolbars (**Camera Actions**, **Optical Configs**, **Widgets**) can be
toggled, and dragged to reposition, the same way as in any Qt application —
right-click the toolbar area for a toggle menu.

## Persistence

Your layout is saved automatically when the app closes, and restored on the
next launch. This includes:

- Main window geometry and state
- Dock widget positions and floating/tabbed arrangement
- Which panels were open

This is stored in your [app settings](settings.md) file
(`window.geometry`, `window.window_state`, `window.dock_manager_state`,
`window.open_widgets`). To reset to a clean default layout:

```sh
mmgui settings --reset
```

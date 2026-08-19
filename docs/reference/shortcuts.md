# Keyboard shortcuts & menus

## Menu bar

| Menu | Contents |
| --- | --- |
| **pymmcore-gui** | About |
| **Devices** | Device Property Browser, Hardware Config Wizard, Load/Save System Configuration, Install Devices |
| **Window** | Every panel not already listed above (toggles visibility) |
| **Help** | — |

## Keyboard shortcuts

| Shortcut | Action |
| --- | --- |
| ++ctrl+k++ | Snap image |
| ++ctrl+l++ | Toggle live mode |
| ++ctrl+shift+c++ | Console |
| ++ctrl+shift+p++ | Device Property Browser |
| ++ctrl+shift+i++ | Install Devices |
| ++ctrl+shift+m++ | MDA panel |
| ++ctrl+shift+r++ | Camera ROI |
| ++ctrl+shift+g++ | Config Groups |
| ++ctrl+shift+x++ | Pixel Size Configuration |
| ++ctrl+shift+e++ | Exception Log |
| ++ctrl+shift+s++ | Stage Control |

Panels without a listed shortcut (Hardware Config Wizard, Stage Explorer,
About) are reached via their menu entry, or the **Window** menu.

Every shortcut and menu placement above is defined by an `ActionInfo` /
`WidgetActionInfo` in the [actions API](api.md#actions) — those are the
source of truth if this page and the running app ever disagree.

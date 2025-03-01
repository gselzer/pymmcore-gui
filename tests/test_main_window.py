from __future__ import annotations

from typing import TYPE_CHECKING

from pymmcore_gui import CoreAction, MicroManagerGUI, WidgetAction

if TYPE_CHECKING:
    from pytestqt.qtbot import QtBot


def test_main_window(qtbot: QtBot) -> None:
    gui = MicroManagerGUI()
    qtbot.addWidget(gui)
    for w_action in WidgetAction:
        gui.get_action(w_action)
        gui.get_widget(w_action)
        assert w_action in gui._qactions
        assert w_action in gui._qwidgets

    for c_action in CoreAction:
        gui.get_action(c_action)
        assert c_action in gui._qactions

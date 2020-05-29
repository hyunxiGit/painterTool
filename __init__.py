from PySide2 import QtWidgets
import substance_painter.ui
from painterTool import shelf_deploy

import importlib
importlib.reload(shelf_deploy)

from PySide2 import QtCore, QtGui, QtWidgets

plugin_widgets = []
"""Keep track of added myui elements for cleanup"""

def start_plugin():
    """This method is called when the plugin is started."""


    form = shelf_deploy.Form()

    substance_painter.ui.add_dock_widget(form)
    # Store added widget for proper cleanup when stopping the plugin
    plugin_widgets.append(form)

def close_plugin():
    """This method is called when the plugin is stopped."""
    # We need to remove all added widgets from the UI.
    for widget in plugin_widgets:
        substance_painter.ui.delete_ui_element(widget)
    plugin_widgets.clear()

if __name__ == "__main__":
    start_plugin()
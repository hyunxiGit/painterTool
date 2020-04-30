"""The hello world of python scripting in Substance Painter
"""
from PySide2 import QtWidgets
import substance_painter.ui
from PainterTool import myTool

plugin_widgets = []
"""Keep track of added myui elements for cleanup"""

def start_plugin():
    """This method is called when the plugin is started."""
    qt_app = myTool.MyQtApp()
    qt_app.show()
    print ("test Python Tool init")
    plugin_widgets.append(qt_app)

def close_plugin():
    """This method is called when the plugin is stopped."""
    # We need to remove all added widgets from the UI.
    for widget in plugin_widgets:
        substance_painter.my_ui.delete_ui_element(widget)
    plugin_widgets.clear()

if __name__ == "__main__":
    start_plugin()
import PySide2.QtWidgets as QtWidgets
from PainterTool.my_ui import main

class MyQtApp (main.Ui_MainWindow , QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp , self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Hello World')
        self.btn_ok.clicked.connect(self.btn_ok_clicked)

    def btn_ok_clicked(self):
        print ("ok btn clicked")

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()

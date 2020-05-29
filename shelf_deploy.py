import shutil
import configparser
from PySide2 import QtCore, QtGui, QtWidgets
import os
import sys

painter_tools_dir = os.path.join(os.environ["IW_PROJECT_DIR"], r"game\bin\arttoolsshg\dcc\substance\painter")
doc_path = os.path.join(os.getenv('USERPROFILE'), 'Documents', 'Allegorithmic')
src_ini = os.path.dirname(os.path.realpath(__file__)) + '\\shelf.ini'
dst_ini = os.path.join(doc_path, 'shelf.ini')

class Form(QtWidgets.QDialog):

    def __init__(self):
        super(Form, self).__init__(None)

        # Create widgets
        self.setWindowTitle('Painter Plugin')
        self.setSizePolicy( QtWidgets.QSizePolicy.Expanding , QtWidgets.QSizePolicy.Fixed)
        self.resize(242, 60)

        self.myTeam = 'None'

        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.label.setText('Please choose your team for substance shelf')
        self.label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        self.cb_team = QtWidgets.QComboBox(self)
        self.cb_team.setObjectName("cb_team")
        self.cb_team.addItem("Default")
        self.cb_team.addItem("Character")
        self.cb_team.addItem("environment")
        self.cb_team.addItem("weapon")

        self.saveBtn = QtWidgets.QPushButton("Save", self)
        self.saveBtn.setObjectName('saveBtn')
        self.saveBtn.clicked.connect(self.save)

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.cb_team)
        self.verticalLayout.addWidget(self.saveBtn)
        self.gridLayout.addLayout(self.verticalLayout,0,0,1,1)
        self.setLayout(self.verticalLayout)

    # Greets the user
    def save(self):
        try :
            cb_team_text = self.cb_team.currentText()

            info = 'You are saving your team as {_t}'.format(_t=cb_team_text)
            userInfo = QtWidgets.QMessageBox.question(self, 'Saving setting file', info, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

            if userInfo == QtWidgets.QMessageBox.Yes:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setText("Your team is saved, you can close the window now.")
                msgBox.exec()

            elif userInfo == QtWidgets.QMessageBox.No:
                pass
        except Exception as e:
            print(' > Failed to complete Painter setup. {0}'.format(e))
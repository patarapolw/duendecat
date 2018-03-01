from . import mainWindow

from duendecat.dir import CONFIG_FILE

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QCheckBox, QLineEdit, QPushButton
from PyQt5.QtGui import QIntValidator

import logging
import json
from collections import OrderedDict


def load():
    logging.debug("Preferences loaded")

    global window
    window = MainWindow()
    window.showUI()


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('Preferences')

    def showUI(self):
        param = OrderedDict(sorted(loadConfig().items()))

        self.text = dict()
        self.textEdit = dict()
        overall = QVBoxLayout()
        for key, value in param.items():
            self.text[key] = QLabel(key)
            if type(value) is bool:
                self.textEdit[key] = QCheckBox()
                self.textEdit[key].setChecked(value)
            elif type(value) is int:
                self.textEdit[key] = QLineEdit(str(value))
                self.textEdit[key].setValidator(QIntValidator())
                self.textEdit[key].setMaxLength(2)
            else:
                self.textEdit[key] = QLineEdit(value)

            item = QHBoxLayout()
            item.addWidget(self.text[key])
            item.addWidget(self.textEdit[key])

            overall.addLayout(item)

        submit = QPushButton('Update Preferences')
        submit.clicked.connect(self.saveConfig)
        overall.addWidget(submit)

        self.setLayout(overall)

        self.show()

    def saveConfig(self):
        param = dict()
        for key in self.textEdit.keys():
            if isinstance(self.textEdit[key], QLineEdit):
                temp = self.textEdit[key].text()
                if temp.isdigit():
                    text = int(temp)
                else:
                    text = temp
            else:
                text = self.textEdit[key].isChecked()
            param[key] = text

        with open(CONFIG_FILE, 'w') as f:
            f.write(json.dumps(param, indent=4))

        # Update the main UI
        mainWindow.getParam(**param)


def loadConfig():
    with open(CONFIG_FILE, 'r') as f:
        param = json.load(f)

    return param


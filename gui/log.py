import sys, os
if __name__ == '__main__':
	os.chdir('../')
	sys.path.insert(0,'.')

from common import common

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import logging
import json

LOGFILE = 'log.txt'

def load():
	logging.debug("Preferences loaded")

	global window
	window = MainWindow()
	window.loadUI()

class MainWindow(QWidget):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle('Log')

	def loadUI(self):
		text = loadText()

		self.logOutput = QTextEdit()
		font = self.logOutput.font()
		font.setPointSize(10)
		self.logOutput.setCurrentFont(font)
		self.logOutput.setText(text)
		self.logOutput.moveCursor(QTextCursor.End)

		sb = self.logOutput.verticalScrollBar()
		sb.setValue(sb.maximum())

		buttonReset = QPushButton('Reset')
		buttonReset.clicked.connect(self.reset)

		buttonUpdate = QPushButton('Update')
		buttonUpdate.clicked.connect(self.update)

		bottom = QHBoxLayout()
		bottom.addWidget(buttonReset)
		bottom.addWidget(buttonUpdate)

		overall = QVBoxLayout()
		overall.addWidget(self.logOutput)
		overall.addLayout(bottom)
		self.setLayout(overall)
		self.show()

	def reset(self):
		open(LOGFILE, 'w').close()
		self.logOutput.setText('')

	def update(self):
		text = loadText()
		self.logOutput.setText(text)
		self.logOutput.moveCursor(QTextCursor.End)

def loadText():
	with open(LOGFILE, 'r',encoding='utf8') as f:
		text = f.read()

	return text

if __name__ == '__main__':
	app = QApplication(sys.argv)
	load()
	sys.exit(app.exec_())
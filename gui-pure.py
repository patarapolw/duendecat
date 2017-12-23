# -*- coding: utf8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class MainWindow(QWidget):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle('Duendecat')

	options = ['JLPT N5', 'JLPT N4', 'JLPT N3', 'JLPT N2', 'JLPT N1',
		'any', 'wanikani']

	jp_sen = 'Japanese sentence'
	en_sen = '\n\n'

	def showUI(self):
		option_box = QComboBox()
		option_box.addItems(self.options)

		level_chooser = QSpinBox()

		submit = QPushButton('Generate')
		submit.clicked.connect(self.handleButton)

		top2 = QHBoxLayout()
		top2.addWidget(level_chooser)
		top2.addWidget(submit)

		top = QHBoxLayout()
		top.addWidget(option_box)
		top.addLayout(top2)
		

		label_jp = QLabel(self.jp_sen)
		label_jp.setWordWrap(True)
		label_en = QLabel(self.en_sen)
		label_jp.setWordWrap(True)

		overall = QVBoxLayout()
		overall.addLayout(top)
		overall.addWidget(label_jp)
		overall.addWidget(label_en)

		self.setLayout(overall)

	def handleButton(self):
		self.label_jp.setText('さよなら')

app = QApplication(sys.argv)
window = MainWindow()

window.showUI()
window.show()

app.exec_()
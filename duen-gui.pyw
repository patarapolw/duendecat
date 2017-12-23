#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# -*- coding: utf8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, os
from time import time

import furigana
from openpyxl import *
from random import randint
import random
from time import sleep
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

jlpt = 'N4' #Parameter: Sheet Name, JLPT Level, 'any', 'wanikani'
level = 20

def getSentence(kanji_col,jp_col,kana_col,en_col,sheet):
	str1 = ''
	str2 = ''
	i = 2
	while True:
		cell_level = sheet[kanji_col + str(i)].value
		if(cell_level == None):
			i = i-1
			break
		if(cell_level <= level):
			pass
			#logging.debug(kanji_col + str(i))
		else:
			break
		i = i+1

	rand = randint(2,i)

	str1 += furigana.kanji(sheet[jp_col + str(rand)].value)
	str2 += sheet[kana_col + str(rand)].value + '<br>'
	str2 += sheet[en_col + str(rand)].value + '<br>'
	str2 += 'Kanji level ' + str(int(sheet[kanji_col + str(rand)].value))

	return [str1, str2]

def getSheet(jlpt, level, wb):
	sheet_array = wb.get_sheet_names()
	if(jlpt=='any'):
		jlpt = random.choice(sheet_array)
	elif(jlpt=='wanikani'):
		if(level <= 10):
			jlpt = 'WK１０以下'
		elif(level <= 20):
			jlpt = random.choice(['N5','WK１０以下'])
		elif(level <= 30):
			jlpt = random.choice(['N5','N4','WK１０以下','Kana','Set01','Set02',
				'Set03','Set04','Set05','Set06','Set07','Set08','Set09','Set10'])
		elif(level <= 40):
			jlpt = random.choice(['N5','N4','N3',
				'WK１０以下','WK１０以上','Kana','Set01','Set02',
				'Set03','Set04','Set05','Set06','Set07','Set08','Set09','Set10'])
		elif(level <= 50):
			jlpt = random.choice(['N5','N4','N3','N2',
				'WK１０以下','WK１０以上','Kana','Set01','Set02',
				'Set03','Set04','Set05','Set06','Set07','Set08','Set09','Set10'])
		elif(level < 60):
			jlpt = random.choice(['N5','N4','N3','N2',
				'WK１０以下','WK１０以上','Kana','Set01','Set02',
				'Set03','Set04','Set05','Set06','Set07','Set08','Set09','Set10'])
		elif(level >=60):
			jlpt = random.choice(sheet_array)
	else:
		pass

	return jlpt

def textOutput(jlpt, sheet):
	if(jlpt[0:1]=='N'):
		kanji_col,jp_col,kana_col,en_col = ('H','A','F','B')
		addendum = '<br>JLPT '+ jlpt
	elif(jlpt[0:2]=='WK'):
		kanji_col,jp_col,kana_col,en_col = ('E','C','C','D')
		addendum = '<br>WaniKani context sentence'
	elif(jlpt=='Kana'):
		kanji_col,jp_col,kana_col,en_col =('J','E','E','F')
		addendum = '<br>Kana context sentence'
	else:
		kanji_col,jp_col,kana_col,en_col = ('K','F','F','G')
		addendum =  '<br>' + jlpt + ' context sentence'
	jp, en = getSentence(kanji_col,jp_col,kana_col,en_col,sheet)
	en += addendum
	return [jp, en]

class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle('Duendecat')

	options = ['JLPT N5', 'JLPT N4', 'JLPT N3', 'JLPT N2', 'JLPT N1',
		'any', 'based on WaniKani level']

	jp_sen = 'Loading'
	en_sen = '\n\n'

	def showUI(self):
		option_box = QComboBox()
		option_box.addItems(self.options)
		if(self.jlpt == 'wanikani'):
			self.jlpt = 'based on WaniKani level'
		if(self.jlpt[0] == 'N'):
			self.jlpt = 'JLPT ' + self.jlpt
		option_box.setCurrentIndex(self.options.index(self.jlpt))
		option_box.currentIndexChanged[str].connect(self.jlptChanged)

		self.level_chooser = MySpinBox()
		self.level_chooser.setPrefix('WaniKani Level ')
		self.level_chooser.setValue(self.level)
		self.level_chooser.lineEdit().setReadOnly(True)
		self.level_chooser.valueChanged.connect(self.levelChanged)
		self.level_chooser.keyPressed.connect(self.on_key)
		#logging.debug(level_chooser.key)

		submit = QPushButton('Generate')
		submit.clicked.connect(self.handleButton)

		top2 = QHBoxLayout()
		top2.addWidget(self.level_chooser)
		top2.addWidget(submit)

		top = QHBoxLayout()
		top.addWidget(option_box)
		top.addLayout(top2)

		if(self.jlpt == 'based on WaniKani level'):
			self.jlpt = 'wanikani'
		elif(self.jlpt[0:4] == 'JLPT'):
			self.jlpt = self.jlpt[5:]

		logging.debug(self.jlpt)

		self.jlpt = getSheet(self.jlpt, self.level, self.wb)
		self.jp_sen, self.en_sen = textOutput(self.jlpt, self.wb[self.jlpt])

		self.label_jp = QLabel(self.jp_sen)
		self.label_jp.setWordWrap(True)
		font = self.label_jp.font()
		font.setPointSize(20)
		self.label_jp.setFont(font)

		self.label_en = QLabel('Click to show translation.')
		clickable(self.label_en).connect(self.showSentence)
		self.label_en.setWordWrap(True)

		#sys.stdout.buffer.write(self.jp_sen.encode('utf8'))
		#sys.stdout.buffer.write(self.en_sen.encode('utf8'))

		overall = QVBoxLayout()
		overall.addLayout(top)
		overall.addWidget(self.label_jp)
		overall.addWidget(self.label_en)

		wid = QWidget()
		wid.setLayout(overall)
		self.setCentralWidget(wid)

		timer = QTimer()
		self.time = QTime(0, 0, 0)

		timer.timeout.connect(self.timerEvent)
		timer.start(100)

		self.zero_time = time()
		self.sen_total = 0

		self.time = QTime(0, 0, 0)
		self.time_elapsed = 'Time elapsed: ' + self.time.toString("mm:ss")

		self.statusBar = QStatusBar()
		self.statusBar.showMessage('Welcome to Duendecat.' + ' '*10 + self.time_elapsed)
		self.setStatusBar(self.statusBar)

		self.timer = QTimer()
		self.timer.timeout.connect(self.count)
		self.timer.start(1000*1)

		self.setGeometry(200,100,600,200)
		self.show()

	def on_key(self):
		logging.debug(self.level_chooser.key)
		if self.level_chooser.key == Qt.Key_Space:
			self.showSentence()
		elif self.level_chooser.key == Qt.Key_Return:
			self.updateUI()

	def jlptChanged(self, s):
		self.jlpt = s
		self.zero_time = time()
		self.sen_total = 0
		self.time = QTime(0, 0, 0)

	def levelChanged(self, level):
		self.level = level
		self.zero_time = time()
		self.sen_total = 0
		self.time = QTime(0, 0, 0)
		#logging.debug(self.level)

	def handleButton(self):
		self.updateUI()

	def showSentence(self):
		if self.label_en.text() == 'Click to show translation.':
			self.label_en.setText(self.en_sen)
		else:
			self.updateUI()

	def updateUI(self):
		if(self.jlpt == 'based on WaniKani level'):
			self.jlpt = 'wanikani'
		elif(self.jlpt[0:4] == 'JLPT'):
			self.jlpt = self.jlpt[5:]

		logging.debug(self.jlpt)

		self.jlpt = getSheet(self.jlpt, self.level, self.wb)
		self.jp_sen, self.en_sen = textOutput(self.jlpt, self.wb[self.jlpt])
		self.label_jp.setText(self.jp_sen)
		self.label_en.setText('Click to show translation.')
		clickable(self.label_en).connect(self.showSentence)

		self.now = time()
		time_elapsed = self.now - self.zero_time
		self.sen_total += 1
		sentence_per_minute = self.sen_total / time_elapsed * 60
		self.statusBar.showMessage('Total sentence(s): ' + str(self.sen_total)
			+ ' '*10 + 'Sentence per minute: ' + str(round(sentence_per_minute, 1))
			+ ' '*10 + self.time_elapsed)

		#sys.stdout.buffer.write(self.jp_sen.encode('utf8'))
		#sys.stdout.buffer.write(self.en_sen.encode('utf8'))

	def count(self):
		self.time = self.time.addSecs(1)
		self.time_elapsed = 'Time elapsed: ' + self.time.toString("mm:ss")
		self.statusBar.showMessage(self.statusBar.currentMessage()[:-len(self.time_elapsed)] + self.time_elapsed )

def clickable(widget):
	class Filter(QObject):
		clicked = pyqtSignal()
		def eventFilter(self, obj, event):
			if obj == widget:
				if event.type() == QEvent.MouseButtonRelease:
					if obj.rect().contains(event.pos()):
						self.clicked.emit()
						return True
			return False

	filter = Filter(widget)
	widget.installEventFilter(filter)
	return filter.clicked

class MySpinBox(QSpinBox):
	keyPressed = pyqtSignal()
	#key = ''

	def keyPressEvent(self, event):
		super(MySpinBox, self).keyPressEvent(event)
		if type(event) == QKeyEvent:
			self.key = event.key()
		self.keyPressed.emit()

######### Start ###################

app = QApplication(sys.argv)
window = MainWindow()

if getattr(sys, 'frozen', False):
	application_path = os.path.dirname(sys.executable)
	os.chdir(application_path)

logging.debug('CWD: ' + os.getcwd())
logging.debug('Loading Excel')
wb = load_workbook('duendecat.xlsx')
logging.debug('Excel loaded\n')

window.jlpt = jlpt
window.level = level
window.wb = wb

window.showUI()

app.exec_()
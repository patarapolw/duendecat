from duendecat.reader import Data
from duendecat.gui import preferences, log

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
from random import randint
import logging
from time import time


def load(**param):
    logging.debug(param)
    logging.debug('Welcome to GUI')

    app = QApplication(sys.argv[:1])
    global window, data
    window = MainWindow()

    data = Data(**param)

    window.param = param
    window.data = data
    window.showUI()

    app.exec_()


def getParam(**param):
    window.param = param
    data.setParam(**param)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('Duendecat')

        menubar = self.menuBar()

        settings = menubar.addMenu('&Settings')
        pref = QAction('Preferences', self)
        settings.triggered[QAction].connect(preferences.load)
        settings.addAction(pref)

        view = menubar.addMenu('&View')
        logging = QAction('Log...', self)
        view.triggered[QAction].connect(log.load)
        view.addAction(logging)

    def showUI(self):
        self.was_speaking = time()
        self.shown_sentence = False
        self.options = self.data.wb.sheetnames + ['any', 'depends']
        option_box = QComboBox()
        option_box.addItems(self.options)
        option_box.setCurrentIndex(self.options.index(self.param['sheet']))
        option_box.currentIndexChanged[str].connect(self.jlptChanged)

        self.level_chooser = MySpinBox()
        self.level_chooser.setPrefix(self.data.character_type + ' level ')
        self.level_chooser.setValue(self.param['level'])
        self.level_chooser.lineEdit().setReadOnly(True)
        self.level_chooser.valueChanged.connect(self.levelChanged)
        self.level_chooser.keyPressed.connect(self.on_key)
        # logging.debug(level_chooser.key)

        submit = QPushButton('Generate')
        submit.clicked.connect(self.handleButton)

        top2 = QHBoxLayout()
        top2.addWidget(self.level_chooser)
        top2.addWidget(submit)

        top = QHBoxLayout()
        top.addWidget(option_box)
        top.addLayout(top2)

        self.top_sen, self.bottom_sen = self.getGuiData(self.param['level'])

        self.label_top = QLabel(self.top_sen)
        self.label_top.setWordWrap(True)
        font = self.label_top.font()
        font.setPointSize(20)
        self.label_top.setFont(font)

        self.label_bottom = QLabel('Click to show translation.')
        clickable(self.label_bottom).connect(self.showSentence)
        self.label_bottom.setWordWrap(True)

        # sys.stdout.buffer.write(self.jp_sen.encode('utf8'))
        # sys.stdout.buffer.write(self.en_sen.encode('utf8'))

        overall = QVBoxLayout()
        overall.addLayout(top)
        overall.addWidget(self.label_top)
        overall.addWidget(self.label_bottom)

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
        self.statusBar.showMessage('Welcome to Duendecat.' + ' ' * 10 + self.time_elapsed)
        self.setStatusBar(self.statusBar)

        self.timer = QTimer()
        self.timer.timeout.connect(self.count)
        self.timer.start(1000 * 1)

        self.setGeometry(200, 100, 600, 200)
        self.show()

        self.data.speak('top', self.row)

    def on_key(self):
        logging.debug(self.level_chooser.key)
        if self.level_chooser.key == Qt.Key_Space:
            self.showSentence()
        elif self.level_chooser.key == Qt.Key_Return:
            self.updateUI()

    def jlptChanged(self, s):
        self.param['sheet'] = s
        self.zero_time = time()
        self.sen_total = 0
        self.time = QTime(0, 0, 0)

    def levelChanged(self, level):
        self.param['level'] = level
        self.zero_time = time()
        self.sen_total = 0
        self.time = QTime(0, 0, 0)

    # logging.debug(self.level)

    def handleButton(self):
        self.updateUI()

    def showSentence(self):
        if not self.shown_sentence:
            self.label_bottom.setText(self.bottom_sen)
            self.shown_sentence = True
            self.data.speak('bottom', self.row)
        else:
            self.updateUI()

    def updateUI(self):
        self.shown_sentence = False
        self.top_sen, self.bottom_sen = self.getGuiData(self.param['level'])
        self.label_top.setText(self.top_sen)
        self.data.speak('top', self.row)
        self.label_bottom.setText('Click to show translation.')
        clickable(self.label_bottom).connect(self.showSentence)

        self.now = time()
        time_elapsed = self.now - self.zero_time
        self.sen_total += 1
        sentence_per_minute = self.sen_total / time_elapsed * 60
        self.statusBar.showMessage('Total sentence(s): ' + str(self.sen_total)
                                   + ' ' * 10 + 'Sentence per minute: ' + str(round(sentence_per_minute, 1))
                                   + ' ' * 10 + self.time_elapsed)

    def getGuiData(self, level):
        max_level_row = self.data.getMaxLevelRow(self.param['level'])
        self.row = randint(2, max_level_row)
        first, last = self.data.getData(self.row, self.param['is_reverse'])

        return first, last

    def count(self):
        self.time = self.time.addSecs(1)
        self.time_elapsed = 'Time elapsed: ' + self.time.toString("mm:ss")
        self.statusBar.showMessage(self.statusBar.currentMessage()[:-len(self.time_elapsed)] + self.time_elapsed)

        if self.param['auto']:
            if self.data.is_speaking:
                self.was_speaking = time()
            else:
                if not self.shown_sentence:
                    lapse = self.param['show_answer_lapse']
                else:
                    lapse = self.param['new_question_lapse']
                if self.was_speaking < time() - lapse:
                    self.showSentence()
                    self.was_speaking = time()
                else:
                    pass


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

    # key = ''

    def keyPressEvent(self, event):
        super(MySpinBox, self).keyPressEvent(event)
        if type(event) == QKeyEvent:
            self.key = event.key()
        self.keyPressed.emit()

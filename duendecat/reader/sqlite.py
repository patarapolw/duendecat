from google_speech import Speech
from threading import Thread

import subprocess, sys
from random import choice
import sqlite3

from duendecat.dir import LOG_FILE, database_path


class Data():
    def __init__(self, **param):
        self.setParam(**param)
        self.conn = sqlite3.connect(database_path(self.filename))
        self.cursor = self.conn.cursor()

        if param['sheet'] == 'any':
            self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            self.table_names = [table[0] for table in self.cursor.fetchall() if table[0] != 'sqlite_sequence']
            self.table = choice(self.table_names)
        else:
            self.table = param['sheet']

        self.cursor.execute('SELECT COUNT(*) FROM {}'.format(self.table))
        self.max_row = self.cursor.fetchone()[0]

    def getLangSen(self, row):
        self.cursor.execute('SELECT lang FROM {} WHERE id=?'.format(self.table), (row, ))
        return self.cursor.fetchone()[0]

    def getReadingSen(self, row):
        self.cursor.execute('SELECT reading FROM {} WHERE id=?'.format(self.table), (row,))
        return self.cursor.fetchone()[0]

    def getEnSen(self, row):
        self.cursor.execute('SELECT en FROM {} WHERE id=?'.format(self.table), (row,))
        return self.cursor.fetchone()[0]

    def getGrammar(self, row):
        self.cursor.execute('SELECT grammar_point, grammar_level FROM {} WHERE id=?'.format(self.table), (row,))
        grammar_point , grammar_level = self.cursor.fetchone()

        raw = grammar_point + '\n' + grammar_level
        return raw

    def getLevel(self, row):
        self.cursor.execute('SELECT char_level FROM {} WHERE id=?'.format(self.table), (row,))
        return self.character_type + ' level ' + self.cursor.fetchone()[0]

    def getLatterPortion(self, row):
        output = []
        output += [self.getReadingSen(row)]
        output += [self.getEnSen(row)]
        output += [self.getGrammar(row)]
        if self.table != 'SpoonFed':
            output += [self.getLevel(row)]

        return '\n'.join(output)

    def getLatterPortionReversed(self, row):
        output = []
        output += [self.getLangSen(row)]
        output += [self.getReadingSen(row)]
        output += [self.getGrammar(row)]
        if self.table != 'SpoonFed':
            output += [self.getLevel(row)]

        return '\n'.join(output)

    def getData(self, row, reverse=False):
        if not reverse:
            first, last = self.getLangSen(row), self.getLatterPortion(row)
        else:
            first, last = self.getEnSen(row), self.getLatterPortionReversed(row)

        with open(LOG_FILE, 'a', encoding='utf8') as f:
            f.write(first)
            f.write('\n')
            f.write(last)
            f.write('\n\n')

        return first, last

    def getMaxLevelRow(self, max_level):
        if self.table == 'SpoonFed':
            max_level = max_level * self.max_row / 60
        for row in range(1, self.max_row):
            self.cursor.execute('SELECT char_level FROM {} WHERE id=?'.format(self.table), (row,))
            level = self.cursor.fetchone()[0]
            if int(level) > max_level:
                return row - 1

        return self.max_row

    def speak(self, sentence_type, row, sleep=False):
        if not self.is_speak:
            return
        if self.reverse:
            if sentence_type == 'top':
                sentence_type = 'bottom'
            else:
                sentence_type = 'top'
        if sentence_type == 'top':
            self.sayLang(self.getLangSen(row), sleep)
        else:
            self.sayEn(self.getEnSen(row), sleep)

    def sayLang(self, sentence, sleep):
        self.say(sentence, self.lang, sleep)

    def sayEn(self, sentence, sleep):
        self.say(sentence, 'en', sleep)

    def say(self, sentence, lang, sleep):
        if lang == 'en':
            speaker = 'alex'
        elif lang == 'jp':
            lang = 'ja'
            speaker = 'kyoko'
        elif lang == 'cn':
            lang = 'zh-CN'
            speaker = 'ting-ting'

        def myfunc():
            self.is_speaking = True

            if self.speech_engine == 'not_set':
                if sys.platform == 'darwin':
                    self.speech_engine = 'mac'
                else:
                    self.speech_engine == 'google'

            if self.speech_engine == 'mac':
                subprocess.call(['say', '-v', speaker, sentence])
            elif self.speech_engine == 'google':
                speech = Speech(sentence, lang)
                speech.play(tuple())

            self.is_speaking = False

        if not sleep:
            t = Thread(target=myfunc)
            t.start()
        else:
            myfunc()

    def setParam(self, **param):
        self.reverse = param['is_reverse']
        self.lang = param['lang']
        self.is_speak = param['speak']
        self.is_speaking = False
        self.speech_engine = param['speech_engine']

        if self.lang == 'cn':
            self.filename = 'HSK.db'
            self.character_type = 'Hanzi'
        else:
            self.filename = 'JLPT.db'
            self.character_type = 'Kanji'

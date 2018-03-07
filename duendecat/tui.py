from __future__ import print_function
from duendecat.reader.sqlite import Data
from duendecat.reader.xlsx import Data as Xlsx
import sys

from random import randint
from time import sleep

import logging


class load():
    def __init__(self, **param):
        logging.debug(param)
        logging.debug('Welcome to CLI')

        if '--xlsx' in sys.argv:
            data = Xlsx(**param)
        else:
            data = Data(**param)

        self.param = param

        self.loopText(data, self.param['times'], data.getMaxLevelRow(param['level']))

    def loopText(self, data, times, max_level_row):
        for i in range(times):
            row = randint(2, max_level_row)
            first, last = data.getData(row, self.param['is_reverse'])

            print(first)
            data.speak('top', row, sleep=True)
            sleep(self.param['show_answer_lapse'])

            print(last)
            data.speak('bottom', row, sleep=True)
            sleep(self.param['new_question_lapse'])

            print()

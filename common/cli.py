if __name__ == '__main__':
    import common
else:
	from . import common

from random import randint
from time import time, sleep

import logging

class load():
	def __init__(self, **param):
		logging.debug(param)
		logging.debug('Welcome to CLI')

		data = common.Data(**param)

		self.param = param

		self.loopText(data, self.param['times'], data.getMaxLevelRow(param['level']))

	def loopText(self, data, times, max_level_row, speak=False):
		for i in range(times):
			row = randint(2, max_level_row)
			first, last = data.getData(row, self.param['is_reverse'])

			common.printText(first)
			data.speak('top', row, sleep=True)
			sleep(self.param['show_answer_lapse'])

			common.printText(last)
			data.speak('bottom', row, sleep=True)
			sleep(self.param['new_question_lapse'])

			print()
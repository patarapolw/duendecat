from source import common
from random import randint
from time import time, sleep

import logging

class load():
	def __init__(self, **param):
		logging.debug(param)
		logging.debug('Welcome to CLI')

		data = common.Data(**param)

		self.is_reverse = param['is_reverse']

		self.loopText(data, param['times'], data.getMaxLevelRow(param['level']))

	def loopText(self, data, times, max_level_row, speak=False):
		for i in range(times):
			row = randint(2, max_level_row)
			first, last = data.getData(row, self.is_reverse)

			common.printText(first)
			sleep(2)

			common.printText(last)
			sleep(1)

			print()
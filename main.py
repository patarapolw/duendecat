#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3
from source import gui, cli
import logging
logging.disable(logging.CRITICAL)

GUI = True

param = {
	'lang': 'cn', # 'jp', 'cn'
	'level': 5,
	'sheet': 'depends', #'default', 'depends', 'any', any sheet names in the xlsx file
	'times': 60,
	'is_reverse': True,
	'speak': True
	}

if param['sheet'] == 'default':
	if param['lang'] == 'jp':
		level = param['level']
		if level in range(1,11):
			param['sheet'] = 'N5'
		elif level in range(11,31):
			param['sheet'] = 'N4'
		elif level in range(31,41):
			param['sheet'] = 'N3'
		elif level in range(41,61):
			param['sheet'] = 'N2'
		else:
			param['sheet'] = 'N1'
	elif param['lang'] == 'cn':
		level = param['level']
		if level in range(1,21):
			param['sheet'] = 'A1'
		elif level in range(21,31):
			param['sheet'] = 'A2'
		elif level in range(31,41):
			param['sheet'] = 'B1'
		elif level in range(41,61):
			param['sheet'] = 'B2'
		else:
			param['sheet'] = 'C1'
elif param['sheet'] == 'depends':
	if param['lang'] == 'jp':
		param['sheet'] = 'any'
	elif param['lang'] == 'cn':
		param['sheet'] = 'SpoonFed'

if GUI:
	gui.load(**param)
else:
	cli.load(**param)
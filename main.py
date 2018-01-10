#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3
from source import gui, cli
import logging
logging.disable(logging.CRITICAL)

GUI = True

param = {
	'lang': 'jp',
	'level': 30,
	'sheet': 'N3',
	'times': 60,
	'is_reverse': False,
	'speak': False
	}

if GUI:
	gui.load(**param)
else:
	cli.load(**param)
#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3
from source import gui, cli
import logging
import argparse
logging.disable(logging.CRITICAL)

parser = argparse.ArgumentParser()
parser.add_argument('--gui', help='Tag if GUI (default: CLI)', action='store_true')
parser.add_argument('--lang', help='cn or jp (default: %(default)s)', default='cn')
parser.add_argument('--level', help='Kanji/Hanzi level (default: %(default)s)', default=5, type=int)
parser.add_argument('--sheet', help='Worksheet to read (default: %(default)s)', default='depends')
parser.add_argument('--times', help='Number of times to repeat (CLI) (default: %(default)s)', default=60, type=int)
parser.add_argument('--lang-first', help='Lang JP/CN before EN (default: reverse)', action='store_false', dest='is_reverse')
parser.add_argument('--reverse', help='EN before Lang JP/CN (default: reverse)', action='store_true', dest='is_reverse')
parser.set_defaults(is_reverse=True)
parser.add_argument('--silent', help='No vocal output (default: speak)', action='store_false', dest='speak')
parser.add_argument('--speak', help='Vocal output (default: speak)', action='store_true', dest='speak')
parser.set_defaults(speak=True)
parser.add_argument('--auto', help='Loop automatically (default: auto)', action='store_true', dest='auto')
parser.add_argument('--no-auto', help='Do not loop automatically (default: auto)', action='store_false', dest='auto')
parser.set_defaults(auto=True)
parser.add_argument('--show-answer-lapse', help='Lapse in seconds to show answer (default: %(default)s)', default=3, type=int)
parser.add_argument('--new-question-lapse', help='Lapse in seconds to show new question (default: %(default)s)', default=1, type=int)
parser.add_argument('--speech-engine', help='Set speech engine. "google" for google_speech (default: %(default)s)', default='not_set')


#parser.print_help()
arg = parser.parse_args()
param = vars(arg)
#print(arg)

#param['gui'] = True

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

if param['gui']:
	gui.load(**param)
else:
	cli.load(**param)
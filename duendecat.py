# -*- coding: utf8 -*-

from openpyxl import *
from random import randint
import random
from time import sleep
import logging
import sys
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

jlpt = 'wanikani' #Parameter: Sheet Name, JLPT Level, 'any', 'wanikani'
level = 30
delay = 5 #in seconds

def printSentence(kanji_col,jp_col,en_col):
	str1 = ''
	str2 = ''
	i = 2
	while True:
		if(sheet[kanji_col + str(i)].value <= level):
			logging.debug(sheet[kanji_col + str(i)].value)
		else:
			break
		i = i+1

	rand = randint(2,i)
	str1 += sheet[jp_col + str(rand)].value
	sys.stdout.buffer.write(str1.encode('utf8'))
	print('')
	sleep(delay)
	str2 += sheet[en_col + str(rand)].value + '\n'
	str2 += 'WaniKani level ' + str(int(sheet[kanji_col + str(rand)].value))
	sys.stdout.buffer.write(str2.encode('utf8'))
	print('')

	return [str1, str2]

#root = Tk()
print('Loading Excel')
wb = load_workbook('duendecat.xlsx')
sheet_array = wb.get_sheet_names()
print('Excel loaded\n')
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
	0

sheet = wb[jlpt]

if(jlpt[0:1]=='N'):
	printSentence('H','A','B')
	print('JLPT '+ jlpt)
elif(jlpt[0:2]=='WK'):
	printSentence('A','C','D')
	print('WaniKani context sentence')
elif(jlpt=='Kana'):
	printSentence('J','E','F')
	print('Kana context sentence')
else:
	printSentence('K','F','G')
	print(jlpt + ' context sentence')

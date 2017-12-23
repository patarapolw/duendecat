#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import re
import unicodedata
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

def is_kanji(ch):
    return 'CJK UNIFIED IDEOGRAPH' in unicodedata.name(ch)

def furigana(text):
    output = ''
    node = convert_text(text)
    logging.debug(node)
    for kanji,furigana in node:
        if(furigana == ''):
            output += kanji
        else:
            output += '<ruby>' + kanji + '<rp>（</rp><rt>' + furigana + '</rt><rp>）</rp></ruby>'

    return output

def kanji(text):
    output = ''
    node = convert_text(text)
    logging.debug(node)
    for kanji,furigana in node:
        output += kanji

    return output

def convert_text(text):
    ret = []
    was_kanji = False
    waiting_for_furigana = False
    reading_furigana = False
    kanji = ''
    furigana = ''

    if(text.find('[') != -1):
        for ch in text:
            if(is_kanji(ch)):
                if(not was_kanji):
                    ret += [[kanji, furigana]]
                    kanji = ch
                    furigana = ''
                else:
                    kanji += ch
                was_kanji = True
            else:
                if(ch == '['):
                    reading_furigana = True
                elif(ch == ']'):
                    ret += [[kanji, furigana]]
                    kanji = ''
                    furigana = ''
                    reading_furigana = False
                else:
                    if(was_kanji):
                        ret += [[kanji, furigana]]
                        kanji = ch
                        furigana = ''
                    else:
                        if(reading_furigana):
                            furigana += ch
                        else:
                            kanji += ch
                was_kanji = False
        ret += [[kanji, furigana]]
    else:
        ret = [[text, '']]

    return ret

#text = 'いい<b>方法[ほうほう]</b>を思[おも]いつきました。'
#logging.debug(convert_text(text))
#str1 = repr(convert_text(text))
#str1 = kanji(text)
#sys.stdout.buffer.write(str1.encode('utf8'))

#nohup $HOME/Documents/GitHub/duendecat/main.py --gui --level 99 --lang jp --sheet N3 --reverse &
#nohup $HOME/Documents/GitHub/duendecat/main.py --gui --level 3 --lang cn --reverse &
nohup $HOME/Documents/GitHub/duendecat/main.py --gui --level 3 --lang cn --lang-first --silent --no-auto &
#$HOME/Documents/GitHub/duendecat/main.py
#$HOME/Documents/GitHub/duendecat/main.py -h

#usage: main.py [-h] [--gui] [--cli] [--lang LANG] [--level LEVEL]
#               [--sheet SHEET] [--times TIMES] [--lang-first] [--reverse]
#               [--silent] [--speak] [--auto] [--no-auto]
#               [--show-answer-lapse SHOW_ANSWER_LAPSE]
#               [--new-question-lapse NEW_QUESTION_LAPSE]
#               [--speech-engine SPEECH_ENGINE]
#
#optional arguments:
#  -h, --help            show this help message and exit
#  --gui                 Tag if GUI (default: True)
#  --cli                 Tag if CLI
#  --lang LANG           cn or jp (default: jp)
#  --level LEVEL         Kanji/Hanzi level (default: 20)
#  --sheet SHEET         Worksheet to read (default: depends)
#  --times TIMES         Number of times to repeat (CLI) (default: 60)
#  --lang-first          Lang JP/CN before EN
#  --reverse             EN before Lang JP/CN (default: False)
#  --silent              No vocal output
#  --speak               Vocal output (default: True)
#  --auto                Loop automatically (default: True)
#  --no-auto             Do not loop automatically
#  --show-answer-lapse SHOW_ANSWER_LAPSE
#                        Lapse in seconds to show answer (default: 3)
#  --new-question-lapse NEW_QUESTION_LAPSE
#                        Lapse in seconds to show new question (default: 1)
#  --speech-engine SPEECH_ENGINE
#                        Set speech engine. "google" for google_speech
#                        (default: not_set)
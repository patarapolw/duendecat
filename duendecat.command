#nohup $HOME/Documents/GitHub/duendecat/main.py --gui --level 99 --lang jp --sheet N3 &
nohup $HOME/Documents/GitHub/duendecat/main.py --gui --level 2 &
#$HOME/Documents/GitHub/duendecat/main.py
#$HOME/Documents/GitHub/duendecat/main.py -h

#usage: main.py [-h] [--gui] [--lang LANG] [--level LEVEL] [--sheet SHEET]
#               [--times TIMES] [--lang-first] [--reverse] [--silent] [--speak]
#               [--auto] [--no-auto] [--show-answer-lapse SHOW_ANSWER_LAPSE]
#               [--new-question-lapse NEW_QUESTION_LAPSE]
#               [--speech-engine SPEECH_ENGINE]
#
#optional arguments:
#  -h, --help            show this help message and exit
#  --gui                 Tag if GUI (default: CLI)
#  --lang LANG           cn or jp (default: cn)
#  --level LEVEL         Kanji/Hanzi level (default: 5)
#  --sheet SHEET         Worksheet to read (default: depends)
#  --times TIMES         Number of times to repeat (CLI) (default: 60)
#  --lang-first          Lang JP/CN before EN (default: reverse)
#  --reverse             EN before Lang JP/CN (default: reverse)
#  --silent              No vocal output (default: speak)
#  --speak               Vocal output (default: speak)
#  --auto                Loop automatically (default: auto)
#  --no-auto             Do not loop automatically (default: auto)
#  --show-answer-lapse SHOW_ANSWER_LAPSE
#                        Lapse in seconds to show answer (default: 3)
#  --new-question-lapse NEW_QUESTION_LAPSE
#                        Lapse in seconds to show new question (default: 1)
#  --speech-engine SPEECH_ENGINE
#                        Set speech engine. "google" for google_speech
#                        (default: not_set)
nohup $HOME/Documents/GitHub/duendecat/main.py --gui --level 99 --lang jp --sheet N3 &
#nohup $HOME/Documents/GitHub/duendecat/main.py --gui --level 2 &
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
#  --gui                 Tag if GUI
#  --lang LANG           cn or jp
#  --level LEVEL         Kanji/Hanzi level
#  --sheet SHEET         Worksheet to read
#  --times TIMES         Number of times to repeat (CLI)
#  --lang-first          Lang JP/CN before EN
#  --reverse             EN before Lang JP/CN
#  --silent              No vocal output
#  --speak               Vocal output
#  --auto                Loop automatically
#  --no-auto             Do not loop automatically
#  --show-answer-lapse SHOW_ANSWER_LAPSE
#                        Lapse in seconds to show answer
#  --new-question-lapse NEW_QUESTION_LAPSE
#                        Lapse in seconds to show new question
#  --speech-engine SPEECH_ENGINE
#                        Set speech engine. "google" for google_speech
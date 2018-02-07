"""
 py2app/py2exe build script for MyApplication.

 Will automatically ensure that all build prerequisites are available
 via ez_setup

 Usage (Mac OS X):
     python setup.py py2app

 Usage (Windows):
     python setup.py py2exe

Usage (Linux):
     python setup.py install
     Normally unix-like platforms will use "setup.py install"
         # and install the main script as such
 """
from setuptools import setup

APP = ['main.py']
DATA_FILES = [
	('database',['database/HSK.xlsx', 'database/JLPT.xlsx']), 'config.txt'
]
OPTIONS = {
    'includes': 'openpyxl',
    'plist': {
    	'CFBundleName': 'Duendecat'
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app','PyQt5','openpyxl'],
)

# setup(
#     app=APP,
#     data_files=DATA_FILES,
#     options={'py2exe': OPTIONS},
#     setup_requires=['py2exe','PyQt5','bcrypt','cffi'],
# )
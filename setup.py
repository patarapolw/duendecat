from setuptools import setup
import sys

mainscript = 'duendecat.py'
setup_requires = ['PyQt5', 'openpyxl==2.3.5', 'google_speech', 'bs4']

if sys.platform == 'darwin':
    setup_requires.append('py2app==0.13')
    extra_options = dict(
        app=[mainscript],
        options=dict(py2app=dict(
            argv_emulation=True
        )),
    )
elif sys.platform == 'win32':
    setup_requires.append('py2exe')
    extra_options = dict(
        app=[mainscript],
    )
else:
    extra_options = dict(
        scripts=[mainscript],
    )

setup(
    name='duendecat',
    data_files=['duendecat/config.json',
                'duendecat/database/HSK.xlsx', 'duendecat/database/JLPT.xlsx',
                'duendecat/log.txt'],
    setup_requires=setup_requires,
    **extra_options
)

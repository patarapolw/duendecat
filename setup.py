from setuptools import setup
import sys

mainscript = 'duendecat.py'
setup_requires = ['PyQt5', 'openpyxl==2.3.5', 'google_speech', 'bs4']

if sys.platform == 'darwin':
    setup_requires.append('py2app')
    extra_options = dict(
        app=[mainscript],
        options=dict(py2app=dict(
            argv_emulation=True,
            plist=dict(
                CFBundleName='Duendecat',
            )
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
    data_files=[
        ('duendecat', ['duendecat/config.json', 'duendecat/log.txt']),
        ('duendecat/database', ['duendecat/database/HSK.xlsx', 'duendecat/database/JLPT.xlsx'])
    ],
    setup_requires=setup_requires,
    **extra_options
)

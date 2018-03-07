from setuptools import setup, find_packages
import sys, os

mainscript = 'duendecat.py'
setup_requires = ['PyQt5', 'bs4']
optional_requires = ['openpyxl==2.3.5', 'google_speech']

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
    packages=find_packages(),
    # package_data={
    #     'duendecat': ['config.json', 'log.txt', 'database/*']
    # },
    # include_package_data=True,
    data_files=[
        ('duendecat', ['duendecat/config.json', 'duendecat/log.txt']),
        ('duendecat/database', [os.path.join('duendecat/database', file) for file in os.listdir('duendecat/database')])
    ],
    setup_requires=setup_requires,
    install_requires=setup_requires,
    entry_points={
        'console_scripts': [
            'duendecat = duendecat.__main__:main'
        ],
        'gui_scripts': [
            'duendecat-gui = duendecat:gui'
        ]
    },
    **extra_options
)

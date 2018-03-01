import os, sys

PROJECT_NAME = 'duendecat'


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.environ.get("_MEIPASS2", os.path.abspath("."))

    return os.path.join(base_path, PROJECT_NAME, relative_path)


def database_path(database):
    return resource_path(os.path.join('database', database))


LOG_FILE = resource_path('log.txt')
CONFIG_FILE = resource_path('config.json')
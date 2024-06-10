#  _________   ________       ___       _       _        ________    ____
# |___   ___| |  ______|     / _ \     | \     / |      |  ______|  |__  |
#     | |     | |______     / /_\ \    |  \   /  |      | | _____      | |
#     | |     |  ______|   /  ___  \   |   \_/   |      | ||___  |     | |
#     | |     | |______   / /     \ \  | |\   /| |      | |____| |  ___| |___
#     |_|     |________| /_/       \_\ |_| \_/ |_|      |________| |_________|
#
from easybar.api import (
    EasyBar,
)
from easybar.exceptions import *
from easybar.version import __version__


__all__ = [
    'EasyBar',
    'EasyBarException',
    'EasyBarFileNotFoundError',
    'EasyBarDecodeError',
    'EasyBarTypeError',
    'EasyBarValueError',
    'EasyBarKeyError',
    'EasyBarStopIteration',
    'EasyBarNotImplementedError',
    '__author__',
    '__doc__',
    '__version__',
]

__author__ = 'University of Liverpool'

__doc__ = 'A simple progress bar for Python.'


class Easybar:
    pass
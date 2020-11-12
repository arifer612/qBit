"""
Creates the Config object to read and parse the qBittorrent configuration file.
"""

import sys

from .directories import config_dir, OS
from os.path import join
from .library import qTorObject


class Config(qTorObject):
    """
    The configuration of the machine's qBittorrent with a human-readable data structure
    """
    def __init__(self, os: str):
        if os == 'Linux':
            config_file = 'qBittorrent.conf'
        elif os == 'Windows':
            config_file = 'qBittorrent.ini'
        elif os == 'Darwin':
            config_file = 'qBittorrent.cfg'
        else:
            sys.exit(1)
        super().__init__(join(config_dir, config_file))

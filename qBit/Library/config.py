"""
Creates the Config object to read and parse the qBittorrent configuration file.
"""

import sys

from PyQt5.QtCore import QSettings  # type: ignore
from .directories import config_dir, OS
from os.path import join


class Config(object):
    """
    The configuration of the machine's qBittorrent with a human-readable data structure
    """
    def __init__(self, os: str):
        if os == 'linux':
            config_file = 'qBittorrent.conf'
        elif os == 'Windows':
            config_file = 'qBittorrent.ini'
        elif os == 'Darwin':
            config_file = 'qBittorrent.cfg'
        else:
            sys.exit(1)
        self.settings = QSettings(join(config_dir, config_file), QSettings.IniFormat)
        self._data = {}  # type: dict
        self._goDeep(self._data)

    def _goDeep(self, conf: dict) -> dict:
        for key in self.settings.childKeys():
            conf[key] = self.settings.value(key)
        if self.settings.childGroups():
            for group in self.settings.childGroups():
                self.settings.beginGroup(group)
                conf[group] = {}
                self._goDeep(conf[group])
                self.settings.endGroup()
        else:
            pass
        return conf

    @property
    def data(self) -> dict:
        return self._data

config = Config(OS)


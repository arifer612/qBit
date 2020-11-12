"""
Standard library API for the whole package
"""

from PyQt5.QtCore import QSettings  # type: ignore
from os.path import expanduser, abspath, isfile, split as sp, splitext as spe
import bencode


class qTorObject(object):
    """
    The configuration of the machine's qBittorrent with a human-readable data structure
    """
    def __init__(self, path: str):
        if not isfile(path):
            raise FileNotFoundError(f"The configuration file {sp(path)[-1]} does not exist.")
        self.settings = QSettings(path, QSettings.IniFormat)
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


class qTorFile(object):
    """
    Parses any torrent files (`.fastresume` and `.torrent` files) into a human-readable data structure
    """
    def __init__(self, path: str):
        if not isfile(abspath(expanduser(path))) or spe(path)[1] not in ('.fastresume', '.torrent'):
            raise FileNotFoundError(f"{path} does not direct to a valid '.fastresume' file.")
        self.hash = spe(sp(path)[-1])[0]
        with open(path, 'rb') as file:
            self._data = bencode.bdecode(file)

    @property
    def data(self) -> dict:
        return self._data
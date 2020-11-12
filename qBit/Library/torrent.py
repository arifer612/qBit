"""
APIs for a torrent file. The torrent files are retrieved from the BT_backup directory.
"""

from .directories import backup_dir
from os.path import splitext as spe, join as jn
from os import listdir
from .library import qTorFile
from typing import Dict, Tuple, Any


class Torrents(object):
    """
    A list of all the torrents managed by the qBittorrent client.
    """
    def __init__(self):
        self._files = {}  # type: Dict[str, Tuple[qTorFile, qTorFile]]
        self._data = {}  # type: Dict[str, Dict[str, Any]]
        self._parse_files()

    def _parse_files(self):
        dir_ = set(spe(file)[0] for file in listdir(backup_dir))  # Get unique hashes
        for file in dir_:
            try:
                qResume = qTorFile(jn(backup_dir, file + '.fastresume'))
            except FileNotFoundError:
                qResume = None
            try:
                qTorrent = qTorFile(jn(backup_dir, file + '.torrent'))
            except FileNotFoundError:
                qTorrent = None
            if qResume and qTorrent:
                if file not in self._files.keys():
                    self._files[file] = (qTorrent, qResume)
                    qData = {**qTorrent.data, **qResume.data}
                    self._data[file] = {key: qData[key] for key in sorted(qData)}  # Making use of the fact that the keys of each file are unique.
            else:
                print(f"{file} is missing a {'.fastresume' if qTorrent else '.torrent'} file.")

    @property
    def data(self) -> Dict[str, Dict[str, Any]]:
        return self._data

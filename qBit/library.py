"""
A library of API to manage the torrents
"""


import bencode

from . import config
from os.path import exists, splitext
from os import path
from .directories import backup_dir
from typing import Dict, Union


def _map_change(file: str, mapping: Dict[Union[str, int], Union[str, int]], *keys) -> None:
    """
    A general method to change the values of the keys of a fastresume file.
    Examples of keys would be `qBt_savePath`, `qBt_category`, `qBt_tags` etc.
    The only keys that should be editable are prepended with qBt.

    Args:
        file (str): The .fastresume file of a torrent.
        mapping (dict): A mapping of the values of the keys.
                        (e.g. For the key `qBt_savePath`, we may have organise our many distros by moving them all to a dedicated seedbox {"~/Downloads/Distros/elementaryos": "/mnt/distros/elementaryos"})
        keys: The keys that this mapping may be applied to. For example, the keys `qBt_savePath` and `save_path` have to have the same values.
    """
    if not isinstance(mapping, Dict):
        raise TypeError(f"{mapping} has to be a map.")
    if not keys:
        raise AssertionError("Keys are required.")

    file = path.join(backup_dir, splitext(file) + '.fastresume')
    if not exists(file):
        raise FileNotFoundError('The file does not exist.')

    errk, errs = [], []
    with open(file, 'rb') as f:
        f_dict = bencode.bdecode(f.read())
        for key in keys:
            if key in f_dict:
                try:
                    f_dict[key] = mapping[f_dict[key]]
                except KeyError:
                    errs.append(f_dict[key])
            else:
                errk.append(key)
        f_dict = bencode.bencode(f_dict)
    with open(file, 'wb') as g:
        g.write(f_dict)

    if errk:
        print(f"{', '.join(key for key in errk)} is/are invalid key(s).")
    if errs:
        print(f"<{'>, <'.join(i for i in errs)}> was/were not mapped.")


def change_path(file: str, path_mapping: Dict[str, str]) -> None:
    _map_change(file, path_mapping, 'save_path', 'qBt_savePath')


def change_category(file: str, cat_mapping: Dict[str, str]) -> None:
    _map_change(file, cat_mapping, 'qBt-category')

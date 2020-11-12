"""
Creates a human-readable data file of all the torrents in the machine.
Directories obtained from the official source at:
https://github.com/qbittorrent/qBittorrent/wiki/Frequently-Asked-Questions#where-does-qbittorrent-save-its-settings
"""

import subprocess
import sys
from os.path import expanduser, join, isdir
import platform


OS = platform.system()  # type: str
if OS == 'Linux':
    query = subprocess.run(['whereis', 'qbittorrent'], stdout=subprocess.PIPE) # type: subprocess.CompletedProcess
    if query.stdout.decode().lstrip('qbittorrent:') == '\n':  # if not installed
        print("qBittorrent is not installed on your system")
        sys.exit(1)
    elif 'snap' in query.stdout.decode().lstrip('qbittorrent:'):  # for snap installs
        config_dir = expanduser(join('~', 'snap', 'qbittorrent-arnatious', 'current', '.config', 'qBittorrent'))  # type: str
        data_dir = expanduser(join('~', 'snap', 'qbittorrent-arnatious', 'current', '.local', 'share', 'data', 'qBittorrent'))  # type: str
    else:  # for apt or deb installs
        config_dir = expanduser(join('~', '.config', 'qBittorrent'))  # type: str
        data_dir = expanduser(join('~', '.local', 'share', 'data', 'qBittorrent'))  # type: str
elif OS == 'Windows':
    config_dir = expanduser(join('%APPDATA', 'qBittorrent'))
    data_dir = expanduser(join('%LOCALAPPDATA', 'qBittorrent'))
    if not (isdir(config_dir) and isdir(data_dir)):
        print("qBittorrent is not installed on your system")
        sys.exit(1)
elif OS == 'Darwin':
    query = subprocess.run(['whereis', 'qbittorrent'], stdout=subprocess.PIPE) # type: subprocess.CompletedProcess
    if query.stdout.decode().lstrip('qbittorrent:') == '\n':  # if not installed
        print("qBittorrent is not installed on your system")
        sys.exit(1)
    else:
        config_dir = expanduser(join('~', '.config', 'qBittorrent'))
        data_dir = expanduser(join('~', 'Library', 'Application Support', 'qBittorrent'))
else:
    print("This can only be run on Linux, Windows, and MacOS systems.")

backup_dir = join(data_dir, 'BT_backup')  # type: str
rss_dir = join(config_dir, 'rss')  # type: str
logs_dir = join(data_dir, 'logs')  # type: str

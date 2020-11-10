"""
Creates a human-readable data file of all the torrents in the machine.
"""

import subprocess
import sys
from os.path import expanduser, join
import platform


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

backup_dir = join(data_dir, 'BT_backup')  # type: str
rss_dir = join(config_dir, 'rss')  # type: str
logs_dir = join(data_dir, 'logs')  # type: str
OS = platform.system()  # type: str

import sys
import pip
import os
import importlib
import subprocess
import concurrent.futures
from os import system


try:
    importlib.import_module('youtube_dl')
except ModuleNotFoundError:
    print('[***]\t Installing youtube-dl python package...')
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'youtube-dl'])
finally:
    globals()['youtube_dl'] = importlib.import_module('youtube_dl')



def get_download_path():
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')



ffmpeg_path = os.getcwd()
download_path = get_download_path()
download_path = os.getcwd()

options = {
        # PERMANENT options
        'quiet': True,
        'format': 'bestaudio/best',
        'ffmpeg_location': f'{ffmpeg_path}/ffmpeg.exe',
        'keepvideo': False,
        'outtmpl': f'{download_path}/%(title)s.bin',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320'
        }],

        # OPTIONAL options
        'noplaylist': True
    }


def download(url):
    with youtube_dl.YoutubeDL(options) as mp3:
        info = mp3.extract_info(url, download=False)
        print('[downloading]\t', info.get('title', None))
        mp3.download([url])
        print('[finished]\t', info.get('title', None))


with concurrent.futures.ThreadPoolExecutor() as executor:
    system('cls')
    print('*** Downloading', len(sys.argv[1:]), 'musics ***')
    executor.map(download, sys.argv[1:])

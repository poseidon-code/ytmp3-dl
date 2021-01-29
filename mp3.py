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


class color:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'


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

# add your own DOWNLOAD PATH below
# download_path = ''

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


status = []
def print_status():
    system('cls')
    print('*** Downloading', len(URLS), 'musics ***')
    [print(item) for item in status]


def download(url):
    with youtube_dl.YoutubeDL(options) as mp3:
        info = mp3.extract_info(url, download=False)
        title = info.get('title', None)

        color_string = color.WARNING + '[downloading]\t' + color.ENDC + title
        status[URLS.index(url)] = color_string
        print_status()

        mp3.download([url])

        color_string = color.OKGREEN + '[finished]\t' + color.ENDC + title
        status[URLS.index(url)] = color_string
        print_status()


URLS = sys.argv[1:]

for url in URLS:
    color_string = color.OKCYAN + '[starting]\t' + color.ENDC + url
    status.append(color_string)


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download, URLS)

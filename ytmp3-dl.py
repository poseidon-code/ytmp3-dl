import concurrent.futures
import getopt
import os
import platform
import sys

import youtube_dl


class color:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'

def clear():
    if os.name == 'nt': os.system('cls')
    else : os.system('clear')

def get_download_path():
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'Downloads')


def get_ffmpeg_location(path=''):
    if path!='':
        if os.path.exists(path) : return path
        else:
            print(color.ERROR, 'ffmpeg at', value, 'NOT FOUND', color.ENDC)
            exit(0)
    elif os.path.exists('/usr/bin/ffmpeg'):
        return '/usr/bin/ffmpeg'
    elif os.path.exists(f'{os.path.abspath(os.getcwd())}/ffmpeg'):
        if platform.system() == 'Windows':
            return f'{os.path.abspath(os.getcwd())}/ffmpeg/windows/ffmpeg.exe'
        elif platform.system() == 'Darwin':
            return f'{os.path.abspath(os.getcwd())}/ffmpeg/darwin/ffmpeg'
        elif platform.system() == 'Linux':
            return f'{os.path.abspath(os.getcwd())}/ffmpeg/linux/ffmpeg'
    else:
        print(color.ERROR, 'ffmpeg NOT FOUND.', color.ENDC,
            '\nIf you are using', color.OKCYAN, '"ytmp3-dl-base"', color.ENDC, 'version, unless valid "ffmpeg" binary location path is passed during execution (-f /path/to/ffmpeg),',
            '\nthis program will not run, as this version does not comes with ffmpeg and its required tools & binaries.',
            '\nYou have to install them seperately for your operating system.',
            '\nhttps://ffmpeg.org/download.html',
            '\n\nYou can always use', color.OKCYAN, '"ytmp3-dl-essentials"', color.ENDC, 'version for every needs, although this comes with extra packages giving it more overall download size.')
        exit(0)


def print_status():
    clear()
    print('*** Downloading', len(URLS), 'musics ***')
    print('*** Download Directory : ', download_path , '***')
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


# driver code
status = []
arguments = sys.argv[1:]
options, URLS = getopt.getopt(arguments, 'f:d:', ['ffmpeg=', 'dir='])

download_path=get_download_path()
for option, value in options:
    if option in ['-d', '--dir']:
        download_path = value

for option, value in options:
    if option in ['-f', '--ffmpeg']:
        ffmpeg_location = get_ffmpeg_location(value)
    else:
        ffmpeg_location = get_ffmpeg_location()

if len(options)==0:
    ffmpeg_location = get_ffmpeg_location()


options = {
        # PERMANENT options
        'quiet': True,
        'format': 'bestaudio/best',
        'ffmpeg_location': ffmpeg_location,
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

for url in URLS:
    color_string = color.OKCYAN + '[starting]\t' + color.ENDC + url
    status.append(color_string)


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download, URLS)
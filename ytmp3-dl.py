#!/usr/bin/env python3

import concurrent.futures
import getopt
import os
import platform
import sys

import yt_dlp


class color:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'

# clear terminal
def clear():
    if os.name=='nt' : os.system('cls')
    else : os.system('clear')



''' Set default download directory '''
def get_download_path():
    # for windows : get default Downloads directory from registry, as USERNAME of the system is required
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    # for linux/osx : get default Downloads directory at Home path ('~')
    else:
        return os.path.join(os.path.expanduser('~'), 'Downloads')



''' Set ffmpeg binary location '''
def get_ffmpeg_location(path=''):
    # if, ffmpeg path is passed from command line arguements
    if path!='':
        # if, passed path exists
        if os.path.exists(path) and (path.split('/')[-1] in ['ffmpeg', 'ffmpeg.exe']) : return path
        # else, the passed ffmpeg path is invalid, exits program
        else : print(color.ERROR + 'ffmpeg at `' + path + '` NOT FOUND' + color.ENDC); exit(0)

    # else if, use the ffmpeg which is already installed by some Operating System's package manager
    elif os.path.exists('/usr/bin/ffmpeg'):
        return '/usr/bin/ffmpeg'

    # else if, use the ffmpeg binaries present with this project
    elif os.path.exists(f'{os.path.abspath(os.getcwd())}/ffmpeg'):
        if platform.system() == 'Windows':
            return f'{os.path.abspath(os.getcwd())}/ffmpeg/windows/ffmpeg.exe'
        elif platform.system() == 'Darwin':
            return f'{os.path.abspath(os.getcwd())}/ffmpeg/darwin/ffmpeg'
        elif platform.system() == 'Linux':
            return f'{os.path.abspath(os.getcwd())}/ffmpeg/linux/ffmpeg'

    # else, if using "ytmp3-dl-base" release version which does not contains ffmpeg binaries,
    # neither a ffmpeg binary location path is passed nor ffmpeg is installed
    else:
        print(color.ERROR + 'ffmpeg NOT FOUND.' + color.ENDC,
            '\nIf you are using', color.OKCYAN, '"ytmp3-dl-base"',color.ENDC, 'version, unless valid "ffmpeg" binary location path is passed during execution (-f /path/to/ffmpeg),',
            '\nthis program will not run, as this version does not comes with ffmpeg and its required tools & binaries.',
            '\nYou have to install them seperately for your operating system.',
            '\nhttps://ffmpeg.org/download.html',
            '\n\nYou can always use', color.OKCYAN, '"ytmp3-dl-essentials"', color.ENDC, 'version for every needs, although this comes with extra packages giving it more overall download size.',
            '\nCheck out the release version for your specific OS here : https://github.com/poseidon-code/ytmp3-dl/releases',
            '\nand download your "ytmp3-dl-essentials" version.')
        exit(0)



''' Printing on terminal '''
def print_status():
    clear()
    print('*** Downloading', len(URLS), 'musics ***')
    print('*** Using ffmpeg at :', ffmpeg_location, '***')
    print('*** Download Directory : ', download_path , '***')
    [print(item) for item in status]



'''Downloading mp3 for every YouTube video URL passed during execution'''
def download(url):
    with yt_dlp.YoutubeDL(options) as mp3:
        info = mp3.extract_info(url, download=False)
        title = info.get('title', None)

        color_string = color.WARNING + '[downloading]\t' + color.ENDC + title
        status[URLS.index(url)] = color_string
        print_status()

        mp3.download([url])

        color_string = color.OKGREEN + '[finished]\t' + color.ENDC + title
        status[URLS.index(url)] = color_string
        print_status()




''' driver code '''
status = []
arguments = sys.argv[1:]
options, URLS = getopt.getopt(arguments, 'f:d:', ['ffmpeg=', 'dir='])   # parse command line options


if len(options)==0:
    # set deafult value to options
    ffmpeg_location = get_ffmpeg_location()
    download_path = get_download_path()
else:
    # set user specified values to options
    for option, value in options:
        if option in ['-d', '--dir'] : download_path = value
        else : download_path = get_download_path()
        
        if option in ['-f', '--ffmpeg'] : ffmpeg_location = get_ffmpeg_location(value)
        else : ffmpeg_location = get_ffmpeg_location()


''' youtube-dl options '''
options = {
        # PERMANENT options
        'quiet': True,
        'format': 'bestaudio/best',
        'ffmpeg_location': ffmpeg_location,
        'keepvideo': False,
        'outtmpl': f'{download_path}/%(title)s.webm',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320'
        }],

        # OPTIONAL options
        'noplaylist': True
    }


''' printing download status on terminal '''
for url in URLS:
    color_string = color.OKCYAN + '[starting]\t' + color.ENDC + url
    status.append(color_string)


''' start download every YouTube URLS passed from command line '''
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download, URLS)

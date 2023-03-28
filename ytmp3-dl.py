#!/usr/bin/env python3

import concurrent.futures
import os
import platform
import shutil
import sys
from getopt import GetoptError, getopt
from pathlib import Path
from typing import List, Tuple

import yt_dlp


# color codes
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



''' Set default download directory (-d, --dir) '''
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



''' Set ffmpeg binary location (-f, --ffmpeg) '''
def get_ffmpeg_path(path=''):
    # if, ffmpeg path is passed from command line arguements
    if path!='':
        # if, passed path exists
        if os.path.exists(path) and (path.split('/')[-1] in ['ffmpeg', 'ffmpeg.exe']) : return path
        # else, the passed ffmpeg path is invalid, exits program
        else : print(f"{color.ERROR}ffmpeg at `{path}` NOT FOUND{color.ENDC}"); exit(0)

    # else if, use the ffmpeg which is already installed by some Operating System's package manager
    elif shutil.which('ffmpeg') != None:
        return shutil.which('ffmpeg')
    
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
        print(
                f"{color.ERROR}ffmpeg NOT FOUND.{color.ENDC}"
        '\n'    f"If you are using {color.OKCYAN}'ytmp3-dl-base'{color.ENDC} version,"
        '\n'    f"unless valid 'ffmpeg' binary location path is passed during execution (-f /path/to/ffmpeg)"
        '\n'    f"this program will not run, as this version does not comes with ffmpeg and its required tools & binaries."
        '\n'    f"You have to install them seperately for your operating system."
        '\n'    f"https://ffmpeg.org/download.html"
        
        '\n\n'  f"You can always use {color.OKCYAN}'ytmp3-dl-essentials'{color.ENDC} version for every needs and hassel free setup,"
        '\n'    f"although this comes with extra packages giving it more overall download size."
        '\n'    f"Check out the release version for your specific OS here : https://github.com/poseidon-code/ytmp3-dl/releases"
        '\n'    f"and download your essentials version."
        
        '\n\n'  f"As an alternative you can always download the source code and use the script directly."
        '\n'    f"Download the source code from here : https://github.com/poseidon-code/ytmp3-dl/archive/refs/heads/main.zip"

        '\n\n'  f"Check out the README.md for more detailed explainations."
        '\n'    f"https://github.com/poseidon-code/ytmp3-dl"
        )
        exit(0)



''' Show help of ytmp3-dl (-h, --help) '''
def usage():
    print(
            f"{color.ERROR}yt{color.WARNING}mp3-dl {color.OKGREEN}v3.0 {color.OKCYAN}~poseidon-code{color.ENDC}"
    '\n'    f"Python script for multi-threaded download of audio from any YouTube video/audio link provided during the runtime,"
    '\n'    f"and converts it to .mp3 format of high quality. It is a wrapper over yt-dlp Python library."
    '\n'    f"Check out the project on Github : https://github.com/poseidon-code/ytmp3-dl"
    )

    print(
    '\n'    f"[OPTIONS]                     [USAGE]"
    '\n'    f"-d, --dir [PATH]              set download directory"
    '\n'    f"-f, --ffmpeg [PATH]           set the exact path to ffmpeg binary"
    '\n'    f"-l, --limit [NUMBER]          set concurrent download limit"

    '\n\n'  f"[FLAGS]                       [USAGE]"
    '\n'    f"-h, --help                    show help on using the ytmp3-dl CLI"
    )
    exit()


''' Printing on terminal '''
def print_status():
    clear()
    print(
            f"{color.ERROR}yt{color.WARNING}mp3-dl {color.OKGREEN}v3.0 {color.OKCYAN}~poseidon-code{color.ENDC}"    
    '\n'    f"{color.ERROR}|{color.ENDC} URLs                       : {len(URLS)}"
    '\n'    f"{color.ERROR}|{color.ENDC} Using ffmpeg at            : {ffmpeg_path}"
    '\n'    f"{color.ERROR}|{color.ENDC} Download Directory         : {download_path}"
    '\n'    f"{color.ERROR}|{color.ENDC} Concurrent Download Limit  : {limit}"
    )
    print()
    [print(item) for item in status]



''' Downloading mp3 for every YouTube video URL passed during execution '''
def download(url):
    with yt_dlp.YoutubeDL(yt_dlp_options) as mp3:
        info = mp3.extract_info(url, download=False)
        title = info.get('title', None)

        status[URLS.index(url)] = f"{color.WARNING}[downloading]{color.ENDC}\t {title}"
        print_status()

        mp3.download([url])

        status[URLS.index(url)] = f"{color.OKGREEN}[finished]{color.ENDC}\t {title}"
        print_status()




''' driver code '''
status: List[str] = []
cli_options: List[Tuple[str, str]]
URLS: List[str]

try:  # parse & handle command line options
    cli_options, URLS = getopt(sys.argv[1:], 'hf:d:l:', ['help', 'ffmpeg=', 'dir=', 'limit='])  
except GetoptError as e: # exit program by showing ytmp3-dl usage
    print(e, '\n')
    usage()


# no options or URLs are passed then show ytmp3-dl usage
if len(cli_options)==0 and len(URLS)==0:
    usage()


# parse and set ytmp3-dl options & flags and proceed to download
if len(cli_options)==0:
    # set deafult value to options
    limit = 2
    ffmpeg_path = get_ffmpeg_path()
    download_path = get_download_path()
else:
    # set user specified values to options
    for option, value in cli_options:
        if option in ['-h', '--help'] : usage()

        if option in ['-d', '--dir'] : download_path = value
        else : download_path = get_download_path()
        
        if option in ['-f', '--ffmpeg'] : ffmpeg_path = get_ffmpeg_path(value)
        else : ffmpeg_path = get_ffmpeg_path()

        if option in ['-l', '--limit'] : 
            try : limit = int(value)
            except ValueError:
                print(f"{color.ERROR}Invalid download limit '{value}'{color.ENDC} (using default 2)")
                limit = 2
                pass
        else : limit = 2


''' youtube-dl options '''
yt_dlp_options = {
        # PERMANENT options
        'quiet': True,
        'format': 'bestaudio/best',
        'ffmpeg_location': ffmpeg_path,
        'keepvideo': False,
        'outtmpl': f'{download_path}/%(title)s.webm',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320'
        }],

        # OPTIONAL options
        'noplaylist': True,
        'noprogress': True,
    }


''' printing download status on terminal '''
for url in URLS : status.append(f"{color.OKCYAN}[starting]{color.ENDC}\t {url}")


''' start download every YouTube URLS passed from command line '''
with concurrent.futures.ThreadPoolExecutor(max_workers=limit) as executor:
    executor.map(download, URLS)

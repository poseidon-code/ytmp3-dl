# **ytmp3-dl**

This is a python script that uses a specific python package **youtube-dl**. It will download the audio file from any video/audio link provided during the execution of the program, and if necessary converts it to **.mp3** format of high quality. Downloads are done in a multithreaded way, so faster downloads ⚡.

---

## **Table Of Contents**
1.  [General Usage](#general-usage)
2.  [Options](#options)
3.  [Usage](#general-usage)
    -   [Script Like Usage](#script-like-usage)
    -   [Release Build Usage](#release-build-usage)
    -   [Build Usage](#build-usage)
4.  [Building](#building)
5.  [Credits](#credits)
6.  [License](#license)
---

## **General Usage**
```bash
$ ytmp3-dl https://youtu.be/dQw4w9WgXcQ
```

You can download set up `ytmp3-dl` as you wish _(see: [script-like](#script-like-usage), [release build](#release-build-usage) usage)_

You can build `ytmp3-dl` for your specific system. Check out [build](#build-usage) usage and entire [Building](#building) section to build your version of `ytmp3-dl` and how to use it more effectively.

Pass some options to customise your downloads. _(see: [Options](#options))_


## **Options**
You can pass command line options and flags to **ytmp3-dl**.
| OPTIONS               | USAGE                         | EXAMPLE |
|-----------------------|-------------------------------|---------|
| `-d`, `--dir` path    | set download directory        | `$ ytmp3-dl -d ~/Music/ <url>` |
| `-f`, `--ffmpeg` path | set the exact path to ffmpeg  | `$ ytmp3-dl -f ~/.local/bin/ffmpeg <url>` |
| `-l`, `--limit` number| set concurrent download limit | `$ ytmp3-dl -l 4 <url>` |

| FLAGS                 | USAGE                         | EXAMPLE |
|-----------------------|-------------------------------|---------|
| `-h`, `--help`        | list available options        | `$ ytmp3-dl -h` |


## Script Like Usage
_(make sure `Python` and `pip` are both installed on your system)_
- Download `ytmp3-dl` script file only
  ```bash
  $ curl -LJO https://raw.githubusercontent.com/poseidon-code/ytmp3-dl/main/ytmp3-dl.py
  ```
- Make `ytmp3-dl` executable
  ```bash
  $ chmod +x ytmp3-dl.py
  ```
- Install `yt-dlp` _(using `pip`)_ and `ffmpeg` _(using your OS's package manager; here: `pacman`)_
  ```bash
  $ pip install yt-dlp
  $ sudo pacman -S ffmpeg
  ```
- You are done here 🍵. Additionally you can set the script to global `$PATH` and use it from there.\
_(check out [General Usage](#general-usage) on how to use the script)_


## Release Build Usage
The builds of this program is available for 64-bit versions of Linux and Windows Operating Systems _(macOS users can download the source code and build it by themselves, see [build instructions](#building))_. These build does not require one to have python (and even ffmpeg) installed. You can download them from [here](https://github.com/poseidon-code/ytmp3-dl/releases).

> **[-base-]: Base Version** \
  This version does not includes ffmpeg binaries, and relies on ffmpeg which is already installed in the user's Operating System. _([Download & Install ffmpeg](https://ffmpeg.org/download.html))_

> **[-essentials-]: Essentials Version** \
  This version comes with compatible ffmpeg binaries, and does not relies on ffmpeg being installed on the Operating System. _(**i.e.** If you don't want to go with the hassel of downloading, installing, setting PATH for ffmpeg, then go with this version.)_


## Build Usage
You can build `ytmp3-dl` for your specific system. Check out entire [Building](#building) section to build your version of `ytmp3-dl` and how to use it more effectively.


## **Building**
To build ytmp3-dl for your system follow these instructions :\
**Prerequisites :**
_(currently tested with these configs only, earlier versions may work too, but no guarantees ;\_\_;)_
- `python` >=3.9
- `pip` >=21.2.4
- `pyinstaller` >=4.7

**Setup Python Virtual Environment**
- Inside the project directory, initialise `venv`, activate it and ensure `pip` :
  ```bash
  $ python -m venv env
  $ . ./env/bin/activate
  $ python -m ensurepip
  ```
- Install `pyinstaller`
  ```bash
  $ pip install pyinstaller
  ```
- Install `ytmp3-dl` dependencies :
  ```bash
  $ pip install -r requirements.txt
  ```

**Start Building**
  ```bash
  $ pyinstaller --onefile ytmp3-dl.py
  ```

**Post Building**
- After building finishes, the actual executable will be at `dist/` directory. You can always `export` the ytmp3-dl binary `PATH` to your shell. Or can make an `alias` for your shell. _(check on setting `$PATH`, inside **Personal Build Usage**)_
  ```.sh
  # inside .bashrc can either of the following lines
  
  # exporting to PATH
  export PATH=$PATH:/path/to/ytmp3-dl/directory/
  
  # OR, setting alias 
  alias ytmp3='/exact/path/to/ytmp3-dl'
  ```

- You can also Copy-Paste the ytmp3-dl binary from `dist/` after building to `~/.local/bin/` directory, and make sure you have this directory exported to your shell's `$PATH` variable _(i.e export PATH=$PATH:$HOME/.local/bin)_.

**Personal Build Usage** \
Since you have build your own **ytmp3-dl** binary for your system, it is also required to have **ffmpeg** installed in your system by your OS's package manager _(i.e.: `sudo pacman -S ffmpeg` for Arch Linux and so on, check for your specific OS)_.

Otherwise you could download the **ffmpeg** binary from [here](https://ffmpeg.org/download.html) and set it to `$PATH` \
_(check:
How to set $PATH for [**Linux**](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix),
[**MacOS**](https://stackoverflow.com/questions/22465332/setting-path-environment-variable-in-osx-permanently)
& [**Windows**](https://stackoverflow.com/questions/24219627/how-to-update-system-path-variable-permanently-from-cmd)
)_



## **Credits**
- _Creator of **yt-dlp** library_ : [yt-dlp](http://github.com/yt-dlp/yt-dlp)
- _Creator of **ffmpeg**_ : [ffmpeg Team](http://ffmpeg.org)

---

## **License**
MIT License

&copy; poseidon-code 2021

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

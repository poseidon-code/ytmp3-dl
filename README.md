# **ytmp3-dl**

This is a python script that uses a specific python package **youtube-dl**. It will download the audio file from any video/audio link provided during the execution of the program, and if necessary converts it to **.mp3** format of high quality. Downloads are done in a multithreaded way, so faster downloads ⚡.

---

## **Table Of Contents**

1.  [General](#General)
2.  [Advanced Usage](#Advanced-Usage)
3.  [Release Builds](#Release-Builds)
4.  [Options](#Options)
5.  [Customizing](#Customizing)
6.  [Authors](#Authors)
7.  [Acknowledgement](#Acknowledgement)
8.  [License](#License)

---

<a name="General"></a>

## General

- The system must have **python** installed and set to the global path. _(downlaod [python](https://www.python.org/downloads/) as per your Operating System. **check** the 'Add Python to system PATH' option while installing in **Windows**)_

- Download the **ytmp3-dl** folder from [here](https://github.com/poseidon-code/ytmp3-dl/archive/master.zip 'ytmp3-dl').

- Open up **cmd** (**terminal** for Linux/macOS).

- **cd** into the directory where you have downloaded the **ytmp3-dl** folder.

  _**otherwise** if your **DEFAULT** Downloads location is C:\Users\YOUR-PC-NAME\Downloads (as of most Windows PC), then write this in **cmd**._

  ```cmd
  C:\Users\YOUR-PC-NAME> cd .\Downloads\ytmp3-dl
  C:\Users\YOUR-PC-NAME\Downloads\ytmp3-dl>
  ```

- Copy the video URL that you want to download. _e.g.: https://www.youtube.com/watch?v=U2NN3tmCVI8_

- While inside the **ytmp3-dl** directory, run the `python ytmp3-dl.py` command:

  ```cmd
  C:\Users\YOUR-PC-NAME\Downloads\ytmp3-dl> python ytmp3-dl.py
  ```

  and paste the URL:

  ```cmd
  C:\Users\YOUR-PC-NAME\Downloads\ytmp3-dl> python ytmp3-dl.py https://www.youtube.com/watch?v=U2NN3tmCVI8
  ```

  you can add multiple URLs _(just add space between URLs)_:

  ```cmd
  C:\Users\YOUR-PC-NAME\Downloads\ytmp3-dl> python ytmp3-dl.py https://www.youtube.com/watch?v=U2NN3tmCVI8 https://www.youtube.com/watch?v=kddC4gi72UE
  ```

  then press **Enter**.

- All the files will be downloaded to the **DEFAULT** Downloads location : _C:\Users\YOUR-PC-NAME\Downloads (as of most Windows OS)_

- You are GOOD NOW 😊

---

<a name="Advanced-Usage"></a>

## Advanced Usage

You can pass command line arguments while downloading using **ytmp3-dl.py**.

- **[-d, --dir]** \
  To set a specific **download directory**, use -d (or --dir) options :
  ```bash
  $ python ytmp3-dl.py -d ~/Music/ https://www.youtube.com/watch?v=kddC4gi72UE
  ```

- **[-f, --ffmpeg]** \
  To set a specific **ffmpeg binary** location, use -f (or --ffmpeg) options :
  ```bash
  $ python ytmp3-dl.py -f ~/.local/bin/ffmpeg https://www.youtube.com/watch?v=kddC4gi72UE
  ```

- You can use all at the same time :
  ```bash
  $ python ytmp3-dl.py -d ~/Music/ -f ~/.local/bin/ffmpeg https://www.youtube.com/watch?v=kddC4gi72UE
  ```

---
<a name="Release-Builds"></a>

## Release Builds

The builds of this program is available for 64-bit versions of Linux, Windows, macOS (Darwin) Operating Systems. These build does not require one to have python (and even ffmpeg) installed. You can download them from [here](https://github.com/poseidon-code/ytmp3-dl/releases/tag/v2.1).

> **[-base-]: Base Version** \
  This version does not includes ffmpeg binaries, and relies on ffmpeg which is already installed in the user's Operating System. _([Download & Install ffmpeg](https://ffmpeg.org/download.html))_

> **[-essentials-]: Essentials Version** \
  This version comes with compatible ffmpeg binaries, and does not relies on ffmpeg being installed on the Operating System. _(**i.e.** If you don't want to go with the hassel of downloading, installing, setting PATH for ffmpeg, then go with this version.)_

---

<a name="Options"></a>

## Options

Here are the list of OPTIONS that can be added by the End User for better customizability of the script and for ease of use. _(view [Customizing](#Customizing) for adding these options inside the script)_

| OPTIONS     | DESCRIPTION                                                                                                                        |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| noplaylist  | **True;** DOES NOT downloads the whole playlist if the video URL provided is that of a video in a playlist. _(default: **False**)_ |
| yesplaylist | **False;** DOES NOT downloads the whole playlist if the video URL provided is that of a video in a playlist. _(default: **True**)_ |
| cachedir    | **True;** ENABLES filesystem caching _(default: **False**)_|

> More options can be added to **youtube-dl** as per your preference. Check all **youtude-dl** options [here](https://github.com/ytdl-org/youtube-dl#options).

---

<a name="Customizing"></a>

## Customizing

Various options of downloading can be added directly to the **ytmp3-dl.py** script. To add custom options, follow these steps _(make sure **python** is installed in your system & PATH is set)_:

- Open **ytmp3-dl.py** with a suitable text editor.
- Press **Ctrl + F** or start **Find** feature of your editor and search for **" OPTIONAL "**.
- Under **OPTIONAL** you can add multitude of Custom Options to make your script unique.
- Enter your desired options by adding a ' **,** ' _(comma)_ at the end of every option you add.
- Yor code will look like this :

  ```python
  options = {
      # PERMANENT options        <--- DON'T CHANGE these options
      'quite': True,
      'format': 'bestaudio/best',
      'ffmpeg_location': f'{ffmpeg_path}/ffmpeg.exe',
      'keepvideo': False,
      'outtmpl': f'{download_path}/%(title)s.bin',
      'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
          'preferredquality': '320'
      }],

      #(OPTIONAL options)        <--- ADD options from here
      'noplaylist': True,
      'options': 'value',
          .       .
          .       .
          .       .
  }
  ```

- The list of all options that can be added are found [here](#Options). _(more options can be added to youtube-dl as per your preference, check all youtude-dl options [here](https://github.com/ytdl-org/youtube-dl#options))_

---

<a name="Authors"></a>

## Authors

- _Creator of **ytmp3-dl**_ : [poseidon-code](http://github.com/poseidon-code)
- _Creator of **youtube-dl** library_ : [ytdl-org](http://www.github.com/ytdl-org)
- _Creator of **ffmpeg** converter_ : [ffmpeg Team](http://ffmpeg.org)

---

<a name="Acknowledgement"></a>

## Acknowledgement

This script is made by poseidon-code using _**python**_ programming language, _**youtube-dl**_ python library and _**ffmepeg**_ media conversion utility for General Use in Public Domain.

<a name="License"></a>

## License

MIT License

&copy; poseidon-code 2021

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

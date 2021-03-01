# **mp3-download-script v2.0**

This is a python script that uses a specific python package **youtube-dl**. It will download the audio file from any video/audio link provided during the execution of the program, and if necessary converts it to **.mp3** format of high quality. Downloads are done in a multithreaded way, so faster downloads ⚡.

---

## **Table Of Contents**

1.  [General](#General)
2.  [Options](#Options)
3.  [Customizing](#Customizing)
4.  [Authors](#Authors)
5.  [Acknowledgement](#Acknowledgement)
6.  [License](#License)

---

<a name="General"></a>

## General

- The system must have **python** installed and set to the global path. _(downlaod [python](https://www.python.org/downloads/) as per your Operating System. **check** the 'Add Python to system PATH' option while installing)_

- Download the **mp3-download-script** folder from [here](https://github.com/poseidon-code/mp3-download-script/archive/master.zip 'mp3-download-script').

- Open up **cmd** (**terminal** for Linux/macOS).

- **cd** into the directory where you have downloaded the **mp3-download-script** folder.

  _**otherwise** if your **DEFAULT** Downloads location is C:\Users\YOUR-PC-NAME\Downloads (as of most Windows PC), then write this in **cmd**._

  ```cmd
  C:\Users\YOUR-PC-NAME> cd downloads\mp3-download-script
  C:\Users\YOUR-PC-NAME\Downloads\mp3-download-script>
  ```

- Copy the video URL that you want to download. _e.g.: https://www.youtube.com/watch?v=U2NN3tmCVI8_

- While inside the **mp3-download-script** directory, run the `python mp3.py` command:

  ```cmd
  C:\Users\YOUR-PC-NAME\Downloads\mp3-download-script> python mp3.py
  ```

  and paste the URL _(mouse right-click)_:

  ```cmd
  C:\Users\YOUR-PC-NAME\Downloads\mp3-download-script> python mp3.py https://www.youtube.com/watch?v=U2NN3tmCVI8
  ```

  you can add multiple URLs _(just add space between URLs)_:

  ```cmd
  C:\Users\YOUR-PC-NAME\Downloads\mp3-download-script> python mp3.py https://www.youtube.com/watch?v=U2NN3tmCVI8 https://www.youtube.com/watch?v=kddC4gi72UE
  ```

  then press **Enter**.

- All the files will be downloaded to the **DEFAULT** Downloads location : _C:\Users\YOUR-PC-NAME\Downloads (as of most Windows OS)_

- You are GOOD NOW 😊

---

<a name="Options"></a>

## Options

Here are the list of OPTIONS that can be added by the End User for better customizability of the script and for ease of use. _(view [Customizing](#Customizing) for adding these options inside the script)_

| OPTIONS     | DESCRIPTION                                                                                                                        |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| noplaylist  | **True;** DOES NOT downloads the whole playlist if the video URL provided is that of a video in a playlist. _(default: **False**)_ |
| yesplaylist | **False;** DOES NOT downloads the whole playlist if the video URL provided is that of a video in a playlist. _(default: **True**)_ |
| cachedir    | **True;** ENABLES filesystem caching _(default: **False**)_                                                                        |

---

<a name="Customizing"></a>

## Customizing

Various options of downloading can be added directly to the **mp3.py** script. To add custom options, follow these steps _(make sure **python** is installed in your system & PATH is set)_:

- Open **mp3.py** with a suitable text editor.
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

- The list of all options that can be added are found [here](#Options).

---

<a name="Authors"></a>

## Authors

- _Creator of **mp3-download-script-v2.0**_ : [poseidon-code](http://github.com/poseidon-code)
- _Creator of **youtube-dl** library_ : [ytdl-org](http://www.github.com/ytdl-org)
- _Creator of **ffmpeg** converter_ : [ffmpeg Team](http://ffmpeg.org)

---

<a name="Acknowledgement"></a>

## Acknowledgement

This script is made by poseidon-code using _python_ programming language, _youtube-dl_ python library and _ffmepeg_ media conversion utility for General Use in Public Domain.

<a name="License"></a>

## License

MIT License

&copy; poseidon-code 2021

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

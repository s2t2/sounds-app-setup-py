# Credits, Notes, and Reference





Errors installing pyaudio package on Windows. Requires "Microsoft Visual C++ Build Tools" first.


```sh
(sounds-env)
Mike@DESKTOP-RC27QBF MINGW64 ~/Desktop/sounds-app
$ pip install -r requirements.txt
Collecting pyaudio (from -r requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/ab/42/b4f04721c5c5bfc196ce156b3c768998ef8c0ae3654ed29ea5020c749a6b/PyAudio-0.2.11.tar.gz
Collecting SpeechRecognition (from -r requirements.txt (line 2))
  Downloading https://files.pythonhosted.org/packages/26/e1/7f5678cd94ec1234269d23756dbdaa4c8cfaed973412f88ae8adf7893a50/SpeechRecognition-3.8.1-py2.py3-none-any.whl (32.8MB)
Building wheels for collected packages: pyaudio
  Building wheel for pyaudio (setup.py): started
  Building wheel for pyaudio (setup.py): finished with status 'error'
  ERROR: Complete output from command 'C:\Users\Mike\Anaconda3\envs\sounds-env\python.exe' -u -c 'import setuptools, tokenize;__file__='"'"'C:\\Users\\Mike\\AppData\\Local\\Temp\\pip-install-rp6a0dpo\\pyaudio\\setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' bdist_wheel -d 'C:\Users\Mike\AppData\Local\Temp\pip-wheel-gpzf6zxn' --python-tag cp37:
  ERROR: running bdist_wheel
  running build
  running build_py
  creating build
  creating build\lib.win-amd64-3.7
  copying src\pyaudio.py -> build\lib.win-amd64-3.7
  running build_ext
  building '_portaudio' extension
  error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": https://visualstudio.microsoft.com/downloads/
  ----------------------------------------
  ERROR: Failed building wheel for pyaudio
  Running setup.py clean for pyaudio
Failed to build pyaudio
Installing collected packages: pyaudio, SpeechRecognition
  Running setup.py install for pyaudio: started
    Running setup.py install for pyaudio: finished with status 'error'
    ERROR: Complete output from command 'C:\Users\Mike\Anaconda3\envs\sounds-env\python.exe' -u -c 'import setuptools, tokenize;__file__='"'"'C:\\Users\\Mike\\AppData\\Local\\Temp\\pip-install-rp6a0dpo\\pyaudio\\setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record 'C:\Users\Mike\AppData\Local\Temp\pip-record-6pahccbe\install-record.txt' --single-version-externally-managed --compile:
    ERROR: running install
    running build
    running build_py
    creating build
    creating build\lib.win-amd64-3.7
    copying src\pyaudio.py -> build\lib.win-amd64-3.7
    running build_ext
    building '_portaudio' extension
    error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": https://visualstudio.microsoft.com/downloads/
    ----------------------------------------
ERROR: Command "'C:\Users\Mike\Anaconda3\envs\sounds-env\python.exe' -u -c 'import setuptools, tokenize;__file__='"'"'C:\\Users\\Mike\\AppData\\Local\\Temp\\pip-install-rp6a0dpo\\pyaudio\\setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record 'C:\Users\Mike\AppData\Local\Temp\pip-record-6pahccbe\install-record.txt' --single-version-externally-managed --compile" failed with error code 1 in C:\Users\Mike\AppData\Local\Temp\pip-install-rp6a0dpo\pyaudio\

```


  + https://github.com/benfred/implicit/issues/76
  + https://github.com/benfred/implicit/issues/76#issuecomment-360872999
  + https://github.com/benfred/implicit/issues/76#issuecomment-414875242
  + https://visualstudio.microsoft.com/visual-cpp-build-tools/




Here's what I did:

Downloaded Microsoft Visual C++ Build Tools from this link: https://visualstudio.microsoft.com/downloads/

Run the installer

Select: Workloads → Visual C++ build tools.

Install options: select only the “Windows 10 SDK” (assuming the computer is Windows 10)

Instructions from: https://www.scivision.co/python-windows-visual-c++-14-required/

See screenshots in [img dir](/img).



Try again: `Cannot open include file: "portaudio.h": No such file or directory`. Need to install portaudio on Windows....


  + https://stackoverflow.com/a/51992497
  + https://anaconda.org/conda-forge/portaudio

```sh
conda install -c conda-forge portaudio
```

Same error message.

  + https://stackoverflow.com/a/52191687

Maybe will work in Python 3.6.

OMG it works.

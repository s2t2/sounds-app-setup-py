# Speech Recognition Setup on Windows

Install C++ Bindings.

Install portaudio.

```sh
conda install -c conda-forge portaudio
```

Use Python 3.6 specifically, not (yet) 3.7.







Now go.


```sh
conda create -n sounds-env-2 python=3.6
conda activate sounds-env-2

pip install -r requirements.txt

python detect.py
```

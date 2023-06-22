# pyspread
start to use pyspread, installed on 09-jun-2023


## install
```
PS L:\home\python> pip install pyspread
Collecting pyspread
  Downloading pyspread-2.2.1-py3-none-any.whl (1.7 MB)
     ---------------------------------------- 1.7/1.7 MB 2.4 MB/s eta 0:00:00
Installing collected packages: pyspread
Successfully installed pyspread-2.2.1

[notice] A new release of pip is available: 23.0.1 -> 23.1.2
[notice] To update, run: C:\Users\Sparisoma Viridi\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip
```

```
PS L:\home\python> pip show pyspread
Name: pyspread
Version: 2.2.1
Summary: Pyspread is a non-traditional spreadsheet application that is based on and written in the programming language Python.
Home-page: https://pyspread.gitlab.io
Author: Martin Manns
Author-email: mmanns@gmx.net
License: GPL v3 :: GNU General Public License
Location: c:\users\sparisoma viridi\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages
Requires:
Required-by:
```


## pip
```
PS L:\home\python> python -m pip install --upgrade pip
Requirement already satisfied: pip in c:\users\sparisoma viridi\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages (23.0.1)
Collecting pip
  Downloading pip-23.1.2-py3-none-any.whl (2.1 MB)
     ---------------------------------------- 2.1/2.1 MB 2.5 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 23.0.1
    Uninstalling pip-23.0.1:
      Successfully uninstalled pip-23.0.1
Successfully installed pip-23.1.2
```

```
PS L:\home\python> pip show pip
Name: pip
Version: 23.1.2
Summary: The PyPA recommended tool for installing Python packages.
Home-page: https://pip.pypa.io/
Author: The pip developers
Author-email: distutils-sig@python.org
License: MIT
Location: c:\users\sparisoma viridi\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages
Requires:
Required-by:
```


## pyqt5
```
PS L:\home\python> pyspread
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\lib\runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\lib\runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "C:\Users\Sparisoma Viridi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\pyspread.exe\__main__.py", line 4, in <module>
  File "C:\Users\Sparisoma Viridi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\pyspread\pyspread.py", line 41, in <module>
    from PyQt5.QtCore import Qt
ModuleNotFoundError: No module named 'PyQt5'
```

```
PS L:\home\python> pip install PyQt5
Collecting PyQt5
  Downloading PyQt5-5.15.9-cp37-abi3-win_amd64.whl (6.8 MB)
     ---------------------------------------- 6.8/6.8 MB 3.0 MB/s eta 0:00:00
Collecting PyQt5-sip<13,>=12.11 (from PyQt5)
  Downloading PyQt5_sip-12.12.1-cp310-cp310-win_amd64.whl (78 kB)
     ---------------------------------------- 78.4/78.4 kB 619.4 kB/s eta 0:00:00
Collecting PyQt5-Qt5>=5.15.2 (from PyQt5)
  Downloading PyQt5_Qt5-5.15.2-py3-none-win_amd64.whl (50.1 MB)
     ---------------------------------------- 50.1/50.1 MB 995.7 kB/s eta 0:00:00
Installing collected packages: PyQt5-Qt5, PyQt5-sip, PyQt5
Successfully installed PyQt5-5.15.9 PyQt5-Qt5-5.15.2 PyQt5-sip-12.12.1
```

```
PS L:\home\python> pip show pyqt5
Name: PyQt5
Version: 5.15.9
Summary: Python bindings for the Qt cross platform application toolkit
Home-page: https://www.riverbankcomputing.com/software/pyqt/
Author: Riverbank Computing Limited
Author-email: info@riverbankcomputing.com
License: GPL v3
Location: c:\users\sparisoma viridi\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages
Requires: PyQt5-Qt5, PyQt5-sip
Required-by:
```


## markdown2
```
PS L:\home\python> pyspread
Warning: Required module markdown2 not found.
```

```
PS L:\home\python> pip install markdown2
Collecting markdown2
  Downloading markdown2-2.4.8-py2.py3-none-any.whl (38 kB)
Installing collected packages: markdown2
Successfully installed markdown2-2.4.8
```

```
PS L:\home\python> pip show markdown2
Name: markdown2
Version: 2.4.8
Summary: A fast and complete Python implementation of Markdown
Home-page: https://github.com/trentm/python-markdown2
Author: Trent Mick
Author-email: trentm@gmail.com
License: MIT
Location: c:\users\sparisoma viridi\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages
Requires:
Required-by:
```


## run
```
```

import os
import sys
import win32api
from pathlib import Path
from subprocess import Popen, CREATE_NEW_CONSOLE

width = win32api.GetSystemMetrics(0)

def dir_content(path):
    win32api.SetCursorPos((width, 0))

    try:
        print(str(path))
    except UnicodeEncodeError:
        pass

    if Path(path).is_dir():
        try:
            for entry in Path(path).iterdir():
                dir_content(entry)
        except PermissionError:
            pass


p = Popen("cmd /c " + sys.executable, creationflags=CREATE_NEW_CONSOLE)

os.system('color 2')
dir_content("C:/")

input()

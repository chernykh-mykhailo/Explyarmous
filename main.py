import os
import sys
from pathlib import Path
from subprocess import Popen, CREATE_NEW_CONSOLE


def dir_content(path):
    os.system('color 2')

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

dir_content("C:/")

input()

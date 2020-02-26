import os
import sys
from pathlib import Path
from subprocess import Popen


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


input()

p = Popen([sys.executable])

dir_content("C:/")

input()

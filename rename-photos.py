"""
Reads file attribute and renames photos based on the
creation date in the following format:
YYYY-MM-DD HH-MM-SS.jpg

path = the location of your files

This script renames ALL FILES in the source folder. YOU CANNOT
UNDO THIS OPERATION

Source and destination folder must be on the same partition. Future
update will fix this
"""

import os
import datetime
from pathlib import Path
import tkinter


path = Path('C:/Users/gabee/Desktop/Practice Files/')
ext = ['.jpg', '.gif', '.png', '.tiff', '.raw']
with os.scandir(path) as loc:
    x = 0
    for i in loc:
        info = i.stat()
        src = i
        dst = str(datetime.datetime.fromtimestamp(info.st_ctime))
        dst = dst.replace(':', '-')
        sep = '.'
        dst = dst.split(sep, 1)[0]
        dst = str(path) + '\\' + dst + ".jpg"
        os.rename(src, dst)
        x += 1
    print("Operation completed on " + str(x) + " files.")
        

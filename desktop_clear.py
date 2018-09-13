import os
import shutil
import time

"""Files not to move"""
EXCEPTIONS = ["desktop.ini", "exception_1.txt", "exception_2.avi"]

date = time.strftime("%d.%m.%Y")
backup_path = "g:/Desktop_backups/{}".format(date)
os.makedirs(date, exist_ok=True)

desktop_path = os.chdir("h:/Users/J/Desktop")
desktop_files = os.listdir()

for file in desktop_files:
    if file not in EXCEPTIONS:
        shutil.move(file, backup_path)

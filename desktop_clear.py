import os
import shutil
import time

EXCEPTIONS = ["desktop.ini", "exception_1.txt", "excepction_2.avi"]
date = time.strftime("%d.%m.%Y")
BACKUP = f"g:/Desktop_backups/{date}"

os.makedirs(date, exist_ok=True)
os.chdir("h:/Users/J/Desktop")
folder = os.listdir()

for file in folder:
    if file not in EXCEPTIONS:
        shutil.move(file, BACKUP)

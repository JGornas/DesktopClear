import os
import shutil
import time

DATE = time.strftime("%d.%m.%Y")
EXCEPTIONS = ["desktop.ini", "plan_programowanie_2018.txt", "django_tutorial"]
BACKUP = f"g:/Desktop_backups/{DATE}"

os.makedirs(DATE, exist_ok=True)
os.chdir("h:/Users/Jake/Desktop")
folder = os.listdir()

for file in folder:
    if file not in EXCEPTIONS:
        shutil.move(file, BACKUP)

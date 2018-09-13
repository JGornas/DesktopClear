import os
import shutil
import time

date = time.strftime("%d.%m.%Y")
EXCEPTIONS = ["desktop.ini", "plan_programowanie_2018.txt", "django_tutorial"]
BACKUP = f"g:/Desktop_backups/{date}"

os.makedirs(date, exist_ok=True)
os.chdir("h:/Users/J/Desktop")
folder = os.listdir()

for file in folder:
    if file not in EXCEPTIONS:
        shutil.move(file, BACKUP)

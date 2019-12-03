import os
from shutil import move
from time import strftime


EXCEPTIONS = ["desktop.ini", "exception_1.txt", "exception_2.avi", "Projekty"]
DESKTOP_PATH = os.path.join("C:\\", "Users", "Jake", "Desktop")
BACKUP_PATH = os.path.join("D:\\", "Desktop_backups", f"{strftime('%m.%d.%Y')}", "")

os.makedirs(BACKUP_PATH, exist_ok=True)
os.chdir(DESKTOP_PATH)
desktop_files = os.listdir(os.getcwd())
[move(file, BACKUP_PATH) for file in desktop_files if file not in EXCEPTIONS]

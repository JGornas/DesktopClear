# Scripts : Desktop_clear


Desktop_clear is a Python script for keeping the desktop out of unwanted files that gather over time.

Python 3.6 dependant (f strings).

## Installation

Clone and open the .py file.
Under DESKTOP_PATH variable enter the path to your desktop. Repeat at BACKUP_PATH with path to backup folder.
To skip specific files or folders add them to EXCEPTIONS list.

## Usage

```python
python desktop_clear.py
```
Execute the script. It will move all files that are not excepted to a new backup directory.

This can be automated using eg. Task Scheduler (Windows)

## Contributing
For changes, please open an issue to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)

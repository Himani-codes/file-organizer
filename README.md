# File Organizer

## What it does
A Python script that sorts the files in a folder into subfolders by file type: Images, Music, Documents and pdfs.

## Features
- Uses a function to avoid repeating the code that creates the folder and moves the file.
- Uses match-case to choose the folder name from the file extension.
- Creates each subfolder only if it does not exist yet, so the script can run again without errors.
- Skips file types it does not know and leaves existing folders alone.

## How to run
1. Open the script and change the `folder` path to the folder you want to sort.
2. Run:

```
python file_organizer.py
```

## Concepts used
- os and shutil modules
- Functions and parameters
- match-case
- File extensions with os.path.splitext

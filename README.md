# Simple todo app

Simple to-do app which run on terminal/command line.
The app is simply command line app which receive input from terminal and process it into local database using python sqlite.

`pyinstaller` library is used to make executeable file from the app (todo.py). The executeable file can be found on `dist/todo/` directory with the file `todo`

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install some dependencies.

You need to use the newer version of pip. To check pip version type `pip -V` in terminal.

To upgrade pip version
```
python3 -m pip install --upgrade pip
```

Install `pyinstaller` library

```
pip install pyinstaller

```

## Usage

To make executable file from todo.py using `pyinstaller`, type
```
pyinstaller todo.py
```

Then go to `dist/todo` and you'll find the `todo` executable file.

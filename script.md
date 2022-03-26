# GUI Hangman Tutorial

In this tutorial you will learn to create a hangman game using with GUI using the MVC framework.

## Setup Environment

Steps:

1. Create virtual environment: 
   	- Mac users, always use `python3` instead of `python`
   	- `python -m venv .venv`
2. make `.gitignore` file:
   	- add virtual environment folder: `/.venv`
3. activate virtual environment
   - open a new terminal:
   - Windows: `.\.venv\Scripts\activate`
   - Mac: `source .venv/bin/activate`
   - Your prompt should start with `(.venv)`
4. Update pip
   - `python -m pip install --upgrade pip`
5. Install packages
   - `python -m pip install PyQt6`
6. Add files to the project directory
   - `hangman.ui`
   - `main_window.py`
   - Rename `main_window.py` to `hangman.py`
7. Generate the Python UI file
   - `pyuic6 -o Ui_hangman.py -x hangman.ui`
8. Update hangman.py file
   - in line 3 change `<ui_filename>` to `ui_hangman`
   - Run the `hangman.py` file and your UI should show.
9. Download the `assests.zip` file into your project directory
   	- extract the file to create a `assests` directory with 12 image files
   	- confirm the files are there and then delete the `assets.zip` file
10. Create a new Python script file called `datastore.py`
11. Download the `dictionary.txt` file into your project directory
12. Your project directory is now set-up. It should contain:
    - `.venv` directory - virtual environment folder
    - `assests` directory - containing 12 gallows images
    - `.githubattributes` - file for GitHub operations
    - `.githubignore` - file listing the directories or files not to be synced
    - `datastore.py` - the Python script containing the model component of our program
    - `dictionary.txt` - file containing the word list we will use
    - `hangman.py` - the Python script containing the control component of our program
    - `hangman.ui` - Qt Designer file which is used to generate our UI
    - `ui_hangman.py` - the Python script containing the view component of our program
13. make sure all your files are saved, then in GitHub Desktop:
    - make a commit
    - push to repository
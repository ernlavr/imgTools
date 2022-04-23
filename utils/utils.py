# Sorts strings by their numerical values if they contain numbers inside them
import os.path
import re
import shutil
from os import walk
from collections import Counter

toIgnore = [".gitignore"]

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def getAllFiles(folder):
    for (dirpath, dirnames, filenames) in walk(folder):
        output = list((Counter(filenames) - Counter(toIgnore)).elements())
        return output

def getInputSubdirs(folder):
    return [ f.path for f in os.scandir(folder) if f.is_dir() ]

def remakeOutputSubdirs(folder):
    # Clear the output
    if (os.path.exists(folder) is True):
        shutil.rmtree(folder)
    os.mkdir(folder)

def clearFolder(folder):
    """
    Deletes all files in the given folder except list of filenames given in the exceptions
    """
    files = getAllFiles(folder)
    for file in files:
        # Skip exceptions
        if file in toIgnore:
            continue
        # Delete
        toDelete = os.path.join(folder, file)
        os.remove(toDelete)


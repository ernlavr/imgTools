import os
import re
from os import walk
import cv2
import shutil
from utils.utils import *

imgFolder = "input/" # Required
output = "output/" # Required

clearFolder(output)
imgs = getAllFiles(imgFolder)
imgs.sort(key=natural_keys)
for index, file in enumerate(imgs):
    # Get the source file and prepare the new name
    src = os.path.join(imgFolder, file)
    newName = f'{index:05d}.jpg'
    dst = os.path.join(output, newName)
    # Copy
    shutil.copyfile(src, dst)
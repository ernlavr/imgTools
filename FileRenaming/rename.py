import os
import re
from os import walk
import cv2
import shutil
from utils.utils import *

INPUT_DIR = "input/" # Required
OUTPUT_DIR = "output/" # Required
subdirs = getInputSubdirs(INPUT_DIR)

for subdirName in subdirs:
    # Get all images from input
    outputDir = subdirName.replace("input", "output")
    remakeOutputSubdirs(outputDir)

    for subdirs, dirs, files in os.walk(subdirName):
        files.sort(key=natural_keys)

        # Crop and save loop
        for index, file in enumerate(files):
            # Get the source file and prepare the new name
            src = os.path.join(subdirName, file)
            newName = f'{index:05d}.jpg'
            dst = os.path.join(outputDir, newName)
            # Copy
            shutil.copyfile(src, dst)
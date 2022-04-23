import os
import re
from os import walk
import cv2
import shutil
from utils.utils import *

INPUT_DIR = "input/" # Required
OUTPUT_DIR = "output/" # Required
NEW_EXT = ".png"
subdirs = getInputSubdirs(INPUT_DIR)

for subdirName in subdirs:
    # Get all images from input
    outputDir = subdirName.replace("input", "output")
    remakeOutputSubdirs(outputDir)

    for subdirs, dirs, files in os.walk(subdirName):
        files.sort(key=natural_keys)

        # Crop and save loop
        for index, file in enumerate(files):
            # Get the source
            src = os.path.join(subdirName, file)
            img = cv2.imread(src)

            # Beging changing and saving
            name, ext = os.path.splitext(file)
            fullName = name + NEW_EXT
            img_output_path = os.path.join(outputDir, fullName)
            responce = cv2.imwrite(img_output_path, img)

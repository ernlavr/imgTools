import os
import re
from os import walk
import cv2
import shutil
import sys
a = os.path.abspath(__file__)
b = os.path.dirname(a)
c = os.path.dirname(b)
sys.path.append(c)

from utils.utils import *

INPUT_DIR = "ChangeExtension/input/" # Required
OUTPUT_DIR = "ChangeExtension/output/" # Required
NEW_EXT = ".jpg"
subdirs = getInputSubdirs(os.path.abspath(INPUT_DIR))

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
            cv2.imwrite(img_output_path, img, [cv2.IMWRITE_JPEG_QUALITY, 50])
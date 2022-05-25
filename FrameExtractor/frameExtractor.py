import cv2
import os
import shutil
import sys

a = os.path.abspath(__file__)
b = os.path.dirname(a)
c = os.path.dirname(b)
sys.path.append(c)

from utils.utils import *

INPUT_DIR = "FrameExtractor/input/"
OUTPUT_DIR = "output/"
applyMedianFilter = True
skipEveryImg = 150


# Get all subdirectories in input
subdirs = getInputSubdirs(os.path.abspath(INPUT_DIR))

for subdirName in subdirs:
  # Clear the output
  outputDir = subdirName.replace("input/", "output/")
  if(os.path.exists(outputDir) is True):
    shutil.rmtree(outputDir)
  os.mkdir(outputDir)

  # Get all files for each subdirectory
  for subdirs, dirs, files in os.walk(subdirName):
    for file in files:
      filePath = os.path.join(subdirName, file)
      vidcap = cv2.VideoCapture(filePath)
      count = 0
      while True:
        success, image = vidcap.read()
        count += 1

        # Break when done
        if success is False:
          break


        outputImg = image
        if(applyMedianFilter):
          outputImg = cv2.medianBlur(image, 5) # Median filter

        # replace extension
        pre, ext = os.path.splitext(file)

        # Save to output
        outputPath = os.path.join(outputDir, pre + str(count) + ".jpg")
        cv2.imwrite(outputPath, outputImg)     # save frame as JPEG file
        print(f'Saved a new frame to {outputPath}')
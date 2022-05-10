import cv2
import os
import shutil


from utils.utils import *

INPUT_DIR = "input"
OUTPUT_DIR = "output"
applyMedianFilter = True

# Get all subdirectories in input
subdirs = getInputSubdirs(INPUT_DIR)
# Clear the output
outputDirL = os.path.join(OUTPUT_DIR, "Left")
outputDirR = os.path.join(OUTPUT_DIR, "Right")
if (os.path.exists(outputDirL) is True):
  shutil.rmtree(outputDirL)
if (os.path.exists(outputDirR) is True):
  shutil.rmtree(outputDirR)
os.mkdir(outputDirL)
os.mkdir(outputDirR)

for subdirName in subdirs:
  # Get all files for each subdirectory
  for subdirs, dirs, files in os.walk(subdirName):
    for file in files:
      filePath = os.path.join(subdirName, file)
      if("_L_" in filePath):
        dst = os.path.join(outputDirL, file)
        shutil.copyfile(filePath, dst)
      else:
        dst = os.path.join(outputDirR, file)
        shutil.copyfile(filePath, dst)

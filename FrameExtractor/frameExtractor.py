import cv2
import os
import shutil


from utils.utils import *

INPUT_DIR = "input/"
OUTPUT_DIR = "output/"
applyMedianFilter = True
skipEveryImg = 150


# Get all subdirectories in input
subdirs = getInputSubdirs(INPUT_DIR)

for subdirName in subdirs:
  # Clear the output
  outputDir = os.path.join(OUTPUT_DIR, subdirName).replace("input/", "")
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
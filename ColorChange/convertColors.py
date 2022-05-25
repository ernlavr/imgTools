import cv2
import os
import shutil
import sys

a = os.path.abspath(__file__)
b = os.path.dirname(a)
c = os.path.dirname(b)
sys.path.append(c)

from utils.utils import *

INPUT_DIR = "ColorChange/input/"
OUTPUT_DIR = "output/"
color = cv2.COLOR_BGR2RGB

# Get all subdirectories in input
subdirs = getInputSubdirs(os.path.abspath(INPUT_DIR))

for subdirName in subdirs:
  # Clear the output
  outputDir = os.path.join(os.path.abspath(OUTPUT_DIR), subdirName).replace("input/", "")
  if(os.path.exists(outputDir) is True):
    shutil.rmtree(outputDir)
  os.mkdir(outputDir)

  # Get all files for each input subdirectory
  for subdirs, dirs, files in os.walk(subdirName):
    print(f"Writing {subdirName}")
    for file in files:
      # Do processing
      src = os.path.join(subdirName, file)
      img = cv2.imread(src)
      im_rgb = cv2.cvtColor(img, color)
      dst = os.path.join(outputDir, file)
      cv2.imwrite(f'{dst}', im_rgb)
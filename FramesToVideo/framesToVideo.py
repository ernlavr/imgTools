import cv2
import os
import shutil
import sys
a = os.path.abspath(__file__)
b = os.path.dirname(a)
c = os.path.dirname(b)
sys.path.append(c)
from utils.utils import *

INPUT_DIR = "FramesToVideo/input/"
OUTPUT_DIR = "FramesToVideo/output/"

# Get all subdirectories in input
subdirs = getInputSubdirs(os.path.abspath(INPUT_DIR))

for subdirName in subdirs:
  # Clear the output
  outputDir = os.path.join(os.path.abspath(OUTPUT_DIR), subdirName).replace("input/", "")
  if(os.path.exists(outputDir) is True):
    shutil.rmtree(outputDir)
  os.mkdir(outputDir)
  outputDst = os.path.join(outputDir, subdirName.replace("input/", "") + ".mp4").replace("\\", "/")

  fourcc = cv2.VideoWriter_fourcc(*'mp4v')
  out = cv2.VideoWriter(outputDst, fourcc, 30.0, (540, 540))

  print(subdirName)
  # Get all files for each input subdirectory
  for subdirs, dirs, files in os.walk(subdirName):
    files.sort(key=natural_keys)

    
    for file in files:

      src = os.path.join(subdirName, file)
      img = cv2.imread(src)
      out.write(img)
      

    out.release()
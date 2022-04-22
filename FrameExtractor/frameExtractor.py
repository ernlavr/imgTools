import cv2
import os
import shutil

INPUT_DIR = "input/"
OUTPUT_DIR = "output/"
applyMedianFilter = True
skipEveryImg = 10

# Clear output directory
shutil.rmtree(OUTPUT_DIR)
os.mkdir(OUTPUT_DIR)

for file in os.listdir(INPUT_DIR):
  filePath = os.path.join(INPUT_DIR, file)
  vidcap = cv2.VideoCapture(filePath)
  success,image = vidcap.read()
  count = 0
  while success:
    count += 1
    if(count % skipEveryImg == 0):  # skips every nTh img
      outputImg = image
      if(applyMedianFilter):
        outputImg = cv2.medianBlur(image, 5) # Median filter

      # replace extension
      pre, ext = os.path.splitext(file)
      
      outputPath = os.path.join(OUTPUT_DIR, pre + str(count) + ".jpg")
      cv2.imwrite(outputPath, outputImg)     # save frame as JPEG file
      print(f'Saved a new frame to {outputPath}')
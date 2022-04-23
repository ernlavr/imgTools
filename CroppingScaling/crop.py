import os
import re
from os import walk
import cv2

from utils.utils import *

INPUT_DIR = "input/" # Required
OUTPUT_DIR = "output/" # Required
crop = False  # Crop or scale
imgs = []

# Cropping
centerCrop = False # Required for Cropping
cropScalar = 2  # Scalar by which we crop

# Scaling
scalingPercentage = 50 # Scalar in percentage by which we scale

def scale(img : str):
    """
    Apply scaling defined by scalingPercentage to the input
    img: path
    """
    img = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    width = int(img.shape[1] * scalingPercentage / 100)
    height = int(img.shape[0] * scalingPercentage / 100)
    dim = (width, height)

    # resize image
    return cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

def crop(img : str):
    """
    Crops the image according to a crop-scalar. If centerCrop is false then 
    crop from top-left, otherwise crop outwards from the center
    img: path
    """
    img = cv2.imread(img)
    height, width, channels = img.shape
    if centerCrop == False:
        newHeight = int(height / cropScalar)
        newWidth = int(width / cropScalar)
        return img[0:newHeight, 0:newWidth]
        

def main():
    # Get all subdirectories in input
    subdirs = getInputSubdirs(INPUT_DIR)

    for subdirName in subdirs:
        # Get all images from input
        outputDir = subdirName.replace("input", "output")
        remakeOutputSubdirs(outputDir)

        for subdirs, dirs, files in os.walk(subdirName):
            files.sort(key=natural_keys)

            # Crop and save loop
            for i in files:
                imgPath = os.path.join(subdirName, i)
                outputPath = os.path.join(outputDir, i)
                if(crop is True):
                    croppedImg = crop(imgPath)
                    cv2.imwrite(f'{outputPath}', croppedImg)
                else: #scale
                    scaledImg = scale(imgPath)
                    cv2.imwrite(f'{outputPath}', scaledImg)

if __name__ == "__main__":
    main()

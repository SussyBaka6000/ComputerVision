import numpy as np
from PIL import Image
import matplotlib.pyplot as pyplot

## 1. convertToGrayScale

def convertToGrayScale(image_path):
    image = Image.open(image_path)
    image_grey = image.convert('LA')
    image_grey.show()
    print(image_grey.mode)
    return image_grey


## calling the method

path = '../resources/cast.jpg'
convertToGrayScale(path)
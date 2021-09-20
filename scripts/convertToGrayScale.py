import cv2
import matplotlib.pyplot as plt
from playground import show_image

## 1. convertToGrayScale

def convertToGrayScale(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    show_image(gray_image)


## calling the method

cast = cv2.imread('../resources/cast.jpg')
convertToGrayScale(cast)
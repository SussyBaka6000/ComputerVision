
import numpy as np
from PIL import Image
import matplotlib.pyplot as pyplot
import cv2
import sys
from ComputerVision import *

# from scripts import shapeDictionary 




# img1 = Image.open('resources/cast.jpg')
# img2 = Image.open('resources/flower.jpg')
# img3 = Image.open('resources/mayim.jpg')
# img4 = Image.open('resources/mayim.jpg')
# img5 = Image.open('resources/mayim.jpg')
# img6 = Image.open('resources/mayim.jpg')
# img7 = Image.open('resources/mayim.jpg')
# img8 = Image.open('resources/mayim.jpg')
# img9 = Image.open('resources/mayim.jpg')
# img10 = Image.open('resources/mayim.jpg')
# img11 = Image.open('resources/mayim.jpg')
# img12 = Image.open('resources/mayim.jpg')
# img13 = Image.open('resources/mayim.jpg')
# my_list = [img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13]
# res = ComputerVision.collageMaker(my_list)



# image_path = 'resources/cast.jpg'
# open_image = Image.open(image_path)
# image_as_npArray = np.array(open_image)
# res = ComputerVision.colorAtCoordinate(image_as_npArray,100,90)
# print(res)




# path = 'resources/cast.jpg'
# ComputerVision.convertToGrayScale(path)


# # ComputerVision.detectFaceInVideo('resources/test.mp4')



ComputerVision.detectObject('resources/flower.jpg','eyes')
# ComputerVision.detectObject('resources/faces.jpg', 'face')



# ComputerVision.extendedDetectObject('resources/faces.jpg',True,False)
# ComputerVision.extendedDetectObject('resources/faces.jpg',True,True)
# ComputerVision.extendedDetectObject('resources/faces.jpg',False,True)




# ComputerVision.reduceToSingleColor("resources/flower.jpg", "b")
# ComputerVision.reduceToSingleColor("resources/flower.jpg", "r")
# ComputerVision.reduceToSingleColor("resources/flower.jpg", "g")
# ComputerVision.reduceToSingleColor("resources/flower.jpg", "m")



# flower = np.array(Image.open('resources/flower.jpg'))
# img1 = np.array(Image.open('resources/1.jpg'))
# img2 = np.array(Image.open('resources/2.jpg'))
# cast = np.array(Image.open('resources/cast.jpg'))

# list = [img1,cast,flower,img2]


# ComputerVision.shapeDictionary(list)
# # shapeDictionary.shapeDictionary(list)
# print(globals())
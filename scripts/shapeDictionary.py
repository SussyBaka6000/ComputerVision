import numpy as np
from PIL import Image
import matplotlib.pyplot as pyplot


# shapeDictionary
# למיין לפי הגובה כי זה מספר השורות
def shapeDictionary(img_list):
    for img in img_list:
        width, height = img.size
        #cm = img.getchannel('R')


        print(width, height)
        print(img.getchannel('R'))



# calling the method

img1 = Image.open('../resources/cast.jpg')
img2 = Image.open('../resources/flower.jpg')
img3 = Image.open('../resources/mayim.jpg')


my_list = [img1, img2, img3]

shapeDictionary(my_list)
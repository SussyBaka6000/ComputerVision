import numpy as np
import matplotlib.pyplot as pyplot
from PIL import Image


def collageMaker(image_list):
    colors = [(1, 2), (0, 2), (0, 1)]

    for i in range(0, len(image_list)):
        image_list[i] = image_list[i].resize((300, 300), Image.ANTIALIAS)
        image_list[i] = np.array(image_list[i])

    length = len(image_list)

    t = 0
    u = 0
    i = 0
    color = colors[u]
    while length != 0:
        if t == 3:
            u = u+1
            t = 0
            if u == 3:
                u = 0
            color = colors[u]

        image_list[i][:, :, color] = 0
        t = t+1
        length = length-1
        i = i+1

    img_list_final = np.concatenate((image_list), axis=0)
    pyplot.imshow(img_list_final)
    pyplot.show()
    return img_list_final


# calling the method
img1 = Image.open('../resources/cast.jpg')
img2 = Image.open('../resources/flower.jpg')
img3 = Image.open('../resources/mayim.jpg')
img4 = Image.open('../resources/mayim.jpg')
img5 = Image.open('../resources/mayim.jpg')
img6 = Image.open('../resources/mayim.jpg')
img7 = Image.open('../resources/mayim.jpg')
img8 = Image.open('../resources/mayim.jpg')
img9 = Image.open('../resources/mayim.jpg')
img10 = Image.open('../resources/mayim.jpg')
img11 = Image.open('../resources/mayim.jpg')
img12 = Image.open('../resources/mayim.jpg')
img13 = Image.open('../resources/mayim.jpg')

my_list = [img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13]

res = collageMaker(my_list)
print(res)
print(type(res))

# pip install numpy
import numpy as np
from PIL import Image
import matplotlib.pyplot as pyplot

# colorAtCoordinate

def colorAtCoordinate(image_np_array,row,col):
    r,g,b = image_np_array[row,col]
    return (r,g,b)




# calling the method
image_path = '../resources/cast.jpg'
open_image = Image.open(image_path)
image_as_npArray = np.array(open_image)
res=colorAtCoordinate(image_as_npArray,100,90)
print(res)
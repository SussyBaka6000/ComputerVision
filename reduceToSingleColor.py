import numpy as np
from PIL import Image
import matplotlib.pyplot as pyplot

def reduceToSingleColor(string , letter):
    flag = 0
    if(letter == "r" or letter == "R"):
        flag = 1
        pyplot.title('Red channel only')
        color = (1,2)
    if(letter == "G" or letter == "g"):
        flag = 1
        pyplot.title('Green channel only')
        color = (0,2)
    if(letter == "B" or letter == "b"):
        flag = 1
        pyplot.title('Blue channel only')
        color = (0,1)    
    if (flag== 0):
        print("Error , the letter must be R or B or G")
        return

    reduced = np.array(Image.open(string)) 
    reduced[:,:,color] = 0
    pyplot.imshow(reduced,aspect="auto")
    pyplot.show()
    

reduceToSingleColor("images/flower.jpg", "b")
reduceToSingleColor("images/flower.jpg", "r")
reduceToSingleColor("images/flower.jpg", "g")
reduceToSingleColor("images/flower.jpg", "m")
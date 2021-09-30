import numpy as np
from PIL import Image

def shapeDictionary(list):
    shape_list=[]
    name_list=[]
    for i in list:
        temp = i.shape #create tupple whith size of ndarray matrix
        shape_list.append(temp) # create list of tuples
        name =  [name for name in globals() if globals()[name] is i] # get object name as string
        name_list.append(name[0]) # create list of names 
    print('Names of the images:', name_list)  #the prints are for check 
    print('Tuples of the img sizes:',shape_list) #the prints are for check 
    res = dict(zip(name_list,shape_list)) # create dict from 2 list
    print('Dictionary:',res)  #the prints are for check 
    order_res = {k: v for k, v in sorted(res.items(), key=lambda x: x[1])} #order dict by values
    print('Ordered Dictionary',order_res) #the prints are for check 
    print(type(order_res))
    return order_res


flower = np.array(Image.open('resources/flower.jpg'))
img1 = np.array(Image.open('resources/1.jpg'))
img2 = np.array(Image.open('resources/2.jpg'))
cast = np.array(Image.open('resources/cast.jpg'))
list = [img1,cast,flower,img2]

# call the function
shapeDictionary(list)


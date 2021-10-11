import numpy as np
from PIL import Image


def shapeDictionary(list):
    shape_list = []
    name_list = []
    for i in list:
        shape = np.array(i).shape  #create tupple whith size of ndarray matrix
        shape_list.append(shape)  # create list of tuples
        name = "img on index "+str(list.index(i)) # create name for the dictionary key
        name_list.append(name) # create list of names 

    print('Tuples of the img sizes:',shape_list) #the prints are for check 
    res = dict(zip(name_list,shape_list)) # create dict from 2 list
    print('Dictionary:',res)  #the prints are for check 
    order_res = {k: v for k, v in sorted(res.items(),key = lambda v: v[1][0])} #order dict by values
    print('Ordered Dictionary by rows',order_res) #the prints are for check 
    return order_res


flower = Image.open('resources/flower.jpg') 
img1 = Image.open('resources/1.jpg')
img2 = Image.open('resources/2.jpg')
cast = Image.open('resources/cast.jpg')
list = [img1,cast,flower,img2]

# call the function
print(shapeDictionary(list))

# mylist = [(3, 5, 8), (6, 2, 8), (2, 9, 4), (6, 8, 5),(6, 9, 5)]
# print(sorted(mylist, key=lambda x: x[0]))
import numpy as np
from PIL import Image

def shapeDictionary(list):

    name_list=[]
    shape_list=[]
    for i in list:
        temp = np.array(i).shape
        shape_list.append(temp) # create list of tuples
        print(temp)
        print(type(temp))
        name = i
        name_list.append(name)
    res = dict(zip(name_list,shape_list)) # create dict from 2 list
    print('Dictionary:',res)  #the prints are for check 
    order_res = {k: v for k, v in sorted(res.items(), key=lambda x: x[1])} #order dict by values
    print('Ordered Dictionary',order_res) #the prints are for check 
    print(type(order_res))
    return order_res


flower = Image.open('resources/flower.jpg')
img1 = Image.open('resources/1.jpg')
img2 = Image.open('resources/2.jpg')
cast = Image.open('resources/cast.jpg')
list = [img1,cast,flower,img2]

print(dir(flower))
# call the function
# shapeDictionary(list)
# print(flower)
# print(type(flower))
# for i in list:
#     print(i.__dict__)
#     break
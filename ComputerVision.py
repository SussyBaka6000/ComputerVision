import numpy as np
from PIL import Image
import matplotlib.pyplot as pyplot
import cv2


class ComputerVision:
    creators = ""

    def __init__(self):
        self.creators = "Maria Slavov, Halil Altif, Geva Jacobovitz"

    @staticmethod
    def convertToGrayScale(image_path):
        image = Image.open(image_path)
        image_grey = image.convert('LA')
        image_grey.show()
        print(image_grey.mode)
        return image_grey

    @staticmethod
    def colorAtCoordinate(image_np_array, row, col):
        r, g, b = image_np_array[row, col]
        return (r, g, b)

    @staticmethod
    def reduceToSingleColor(string, letter):
        flag = 0
        if (letter == "r" or letter == "R"):
            flag = 1
            pyplot.title('Red channel only')
            color = (1, 2)
        if (letter == "G" or letter == "g"):
            flag = 1
            pyplot.title('Green channel only')
            color = (0, 2)
        if (letter == "B" or letter == "b"):
            flag = 1
            pyplot.title('Blue channel only')
            color = (0, 1)
        if (flag == 0):
            print("Error , the letter must be R or B or G")
            return

        reduced = np.array(Image.open(string))
        reduced[:, :, color] = 0
        pyplot.imshow(reduced, aspect="auto")
        pyplot.show()
        return reduced

    @staticmethod
    def collageMaker(image_list):
        colors = [(1, 2), (0, 2), (0, 1)]

        for i in range(0, len(image_list)):
            image_list[i] = image_list[i].resize((300, 300), Image.ANTIALIAS)
            image_list[i] = np.array(image_list[i])

        length = len(image_list)

        t = 0
        u = 0
        i = 0  # אני אוהב ליצור משתנים עם אות אחת (גבע)
        color = colors[u]
        while length != 0:
            if t == 3:
                u = u + 1
                t = 0
                if u == 3:
                    u = 0
                color = colors[u]

            image_list[i][:, :, color] = 0
            t = t + 1
            length = length - 1
            i = i + 1

        img_list_final = np.concatenate((image_list), axis=0)
        pyplot.imshow(img_list_final)
        pyplot.show()
        return img_list_final

    @staticmethod
    def shapeDictionary(list):
        shape_list = []
        name_list = []
        for i in list:
            temp = i.shape  # create tupple whith size of ndarray matrix
            shape_list.append(temp)  # create list of tuples
            name = [name for name in globals() if globals()[name] is i]  # get object name as string
            name_list.append(name[0])  # create list of names
        print('Names of the images:', name_list)  # the prints are for check
        print('Tuples of the img sizes:', shape_list)  # the prints are for check
        res = dict(zip(name_list, shape_list))  # create dict from 2 list
        print('Dictionary:', res)  # the prints are for check
        order_res = {k: v for k, v in sorted(res.items(), key=lambda x: x[1])}  # order dict by values
        print('Ordered Dictionary', order_res)  # the prints are for check
        print(type(order_res))
        return order_res

    @staticmethod
    def extendedDetectObject(string , faceBool, eyeBool):
        if(isinstance(faceBool, bool)==False or isinstance(eyeBool, bool) ==False):
            return(print ("Pleace Enter True or False"))
        if(faceBool == False and eyeBool == False): 
            return(print ("Nothing to detect"))

        def show_image(name):
            while True:
                cv2.imshow('image', name)
                key_pressed = cv2.waitKey(0)
                # if key_pressed & 27: # by default
                if key_pressed & ord('q'): # q character is pressed
                    break
            # cv2.destroyWindow('image') # release image window resources
            cv2.destroyAllWindows()


        imageToCheck = cv2.imread(string)
        # show_image(imageToCheck)

        newImage = imageToCheck.copy()
        # copy imageToCheck to newImage

        gray = cv2.cvtColor(newImage,cv2.COLOR_BGR2GRAY)
        # show_image(gray)

        # choose classifier and training set
        face_classifier = \
            cv2.CascadeClassifier(cv2.data.haarcascades
                                + 'haarcascade_frontalface_default.xml')

        # choose eye classifier and traning set 
        eye_classifier = \
            cv2.CascadeClassifier(cv2.data.haarcascades 
                                +'haarcascade_eye.xml')

        face = face_classifier.detectMultiScale(gray)
        eye = eye_classifier.detectMultiScale(gray)

        if(faceBool == True):
            for(_x,_y,_w,_h) in face:
                cv2.rectangle(newImage,
                            (_x,_y), # upper-left corner
                            (_x+_w,_y+_h), # lower-right corner
                            (0,255,0),
                            10)

        # show_image(imageToCheck)
        if(eyeBool==True):
            for(_x,_y,_w,_h) in eye:
                cv2.rectangle(newImage,
                            (_x,_y), # upper-left corner
                            (_x+_w,_y+_h), # lower-right corner
                            (0,0,0),
                            10)

        show_image(newImage)
        return(newImage)

    @staticmethod
    def detectFaceInVideo(path):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        capture = cv2.VideoCapture(path)

        while True:
            _, img = capture.read()

            greyFrame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(greyFrame,
                                                  scaleFactor=1.1,
                                                  minNeighbors=5,
                                                  minSize=(30, 30),
                                                  flags=cv2.CASCADE_SCALE_IMAGE)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

            cv2.imshow('Video', img)

            key = cv2.waitKey(35) & 0xff
            if key == 27:
                break

        capture.release()

    @staticmethod
    def detectObject(image_path, area):
        area = area.lower()

        if area != "eyes" and area != "face":
            return "Please enter a valid body area to recognize"

        if image_path == ():
            print(" Not found area  in the given image!")

        def show_image(name):
            while True:
                cv2.imshow('image', name)
                key_pressed = cv2.waitKey(0)

                if key_pressed & ord('q'):
                    break
            cv2.destroyAllWindows()

        imageToCheck = cv2.imread(image_path)

        newImage = imageToCheck.copy()
        # copy imageToCheck to newImage

        # הופכים לאפור כדי לבצע איתור
        gray = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)

        face_classifier = \
            cv2.CascadeClassifier(cv2.data.haarcascades
                                + 'haarcascade_frontalface_default.xml')

        eye_classifier = \
            cv2.CascadeClassifier(cv2.data.haarcascades
                                + 'haarcascade_eye.xml')

        face = face_classifier.detectMultiScale(gray)
        eye = eye_classifier.detectMultiScale(gray)

        if (area == "face" and face ):
            print("if1")
            for (_x, _y, _w, _h) in face:
                cv2.rectangle(newImage,
                            (_x, _y),  # upper-left corner
                            (_x + _w, _y + _h),  # lower-right corner
                            (0, 255, 0),
                            10)
            show_image(newImage) 

        if (area == "eyes" and eye):
            print("if2")
            for (_x, _y, _w, _h) in eye:
                cv2.rectangle(newImage,
                            (_x, _y),  # upper-left corner
                            (_x + _w, _y + _h),  # lower-right corner
                            (0, 0, 0),
                            10)
            show_image(newImage)                        
        else:
            print("Area was not detected")
        
        return (newImage)



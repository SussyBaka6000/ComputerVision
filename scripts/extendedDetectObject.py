import cv2

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



# call the function
extendedDetectObject('./resources/faces.jpg',True,False)
extendedDetectObject('./resources/faces.jpg',True,True)
extendedDetectObject('./resources/faces.jpg',False,True)
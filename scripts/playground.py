# זה לא חלק מהעבודה פה יש את כל הערות ואיך עושים את הדברים
import cv2
import matplotlib.pyplot as plt
# pip3 install opencv-python
# pip3 install matplotlib

def show_image(name):
    while True:
        cv2.imshow('image', name)
        key_pressed = cv2.waitKey(0)  # delay of 1 sec
        if key_pressed & ord('q'):
            break
    cv2.destroyWindow('image')


cast = cv2.imread('../resources/cast.jpg')
# show_image(cast)

###################################################################################
#המרה ל RGB

# cast_rgb = cv2.cvtColor(cast, cv2.COLOR_BGR2RGB)
# plt.imshow(mayim_as_img)
# plt.show()

###################################################################################

#Face detaction כדי לעשות זיהוי פנים קודם הופכים את התמונה לאפורה


#
cast_gray = cv2.cvtColor(cast,cv2.COLOR_BGR2GRAY)
show_image(cast_gray)

###################################################################################################
#
# face_Classifire = cv2.CascadeClassifier(cv2.data.haarcascades + '/haarcascade_frontalface_default.xml')
#
# face = face_Classifire.detectMultiScale(mayim_gray)
#
# for(_x,_y,_w,_h) in face:
#     cv2.rectangle(mayim_gray,
#                   (_x,_y),
#                   (_x + _w, _y+ _h)
#                   (0,255 ,0),
#                 10  )
#
#     show_image((mayim_gray))


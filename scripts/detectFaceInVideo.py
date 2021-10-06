import cv2

# detectFaceInVideo
def detectFaceInVideo(path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    capture = cv2.VideoCapture(path)

    while True:
        _, img = capture.read()

        grayFrame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(grayFrame,
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


# calling the method
detectFaceInVideo('../resources/test.mp4')









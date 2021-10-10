import cv2


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

    if (area == "face"):
        for (_x, _y, _w, _h) in face:
            cv2.rectangle(newImage,
                          (_x, _y),  # upper-left corner
                          (_x + _w, _y + _h),  # lower-right corner
                          (0, 255, 0),
                          10)

    if (area == "eyes"):
        for (_x, _y, _w, _h) in eye:
            cv2.rectangle(newImage,
                          (_x, _y),  # upper-left corner
                          (_x + _w, _y + _h),  # lower-right corner
                          (0, 0, 0),
                          10)

    show_image(newImage)
    return (newImage)

    ## call the function


print(detectObject('./resources/faces.jpg', 'eyes'))

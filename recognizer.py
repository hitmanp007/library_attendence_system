import cv2

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/trainer.yml")

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

names = ["", "hero"]  # ID 1 = Muskan

cam = cv2.VideoCapture(0)

while True:

    ret, img = cam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(
            gray[y:y+h, x:x+w]
        )

        if confidence < 70:
            name = names[id]
        else:
            name = "Unknown"

        cv2.putText(
            img,
            str(name),
            (x+5, y-5),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255,255,255),
            2
        )

    cv2.imshow("Face Recognition", img)

    if cv2.waitKey(10) & 0xff == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
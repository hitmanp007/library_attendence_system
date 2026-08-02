import cv2
import os

path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

print(path)
print(os.path.exists(path))

face_detector = cv2.CascadeClassifier(path)

print(face_detector.empty())
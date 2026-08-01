import cv2
cam = cv2.VideoCapture(0)
count=0
while True:
    ret, frame = cam.read()
    if ret:
        cv2.imshow('opencv',frame)
        if  cv2.waitKey(100) & 0xFF == ord('q'):
            break
        cv2.imwrite(f'dataset/pranav{count}.jpg',frame)
        count+=1
        if count>=50:
            break
    else:
        print("not working")
        break
cv2.destroyAllWindows()

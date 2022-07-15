import cv2
import time
import numpy as np


cap = cv2.VideoCapture(0)
image=cv2.imread('me.jpg')

while True:
    ret,frame = cap.read()
    print(frame)
    frame= cv2.resize(frame,(640,480))
    image=cv2.resize(image,(640,480))

    lower_black = np.array([104,153,70])
    upper_black = np.array([30,30,0])
    mask_1 = cv2.inRange(frame,lower_black,upper_black)
    
    res = cv2.bitwise_and(frame,frame,mask = mask_1)

    f = frame-res
    f = np.where(f == 0,image,f)
 
    cv2.imshow("Magic",frame)
    cv2.imshow('mask',f)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()



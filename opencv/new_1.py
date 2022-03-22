import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(1):
    _, frame = cap.read()   # Take each frame
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    # Convert BGR to HSV
    (H,S,V) = cv2.split(hsv)

    lower_blue = np.array([110,50,50])    # define range of blue color in HSV
    upper_blue = np.array([130,255,255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)  #Threshold the HSV image to get only blue colors
    res = cv2.bitwise_and(frame,frame, mask= mask)   #Bitwise-AND mask and original image

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    print(H[160,120],S[160,120],V[160,120])   #print((H,S,V)[160,120])

    if 130>H[160,120]>110 or 255>S[160,120]>50 or 255>V[160,120]>50:
            print('blue')
    else : print('???')

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()

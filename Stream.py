import cv2
import numpy as np
import os
import subprocess
import pyautogui

cap=cv2.VideoCapture(0)
is_paused=0

face_cascade = cv2.CascadeClassifier('frontalfacehaarcascade.xml')

found_face=False

while True:
    ret,img=cap.read()
    if ret is not True:
        print("Frame processing error")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces)==0:
        found_face=False
    else:
        found_face=True

    if is_paused==0 and found_face==False:
        pyautogui.typewrite(['space'],0.1)
        is_paused=1
    elif is_paused==1 and found_face==True:
        pyautogui.typewrite(['space'],0.1)
        is_paused=0
    else:
        pass




cap.release()

import cv2
import time
import numpy as np
from ffpyplayer.player import MediaPlayer
import sys


videoreader=cv2.VideoCapture(sys.argv[1])
player=MediaPlayer(sys.argv[1])

cap=cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('frontalfacehaarcascade.xml')

eye_cascade = cv2.CascadeClassifier('eyeshaarcascade.xml')

pauseframe=cv2.imread('PauseFrame.png',0)
pauseframe=cv2.resize(pauseframe,(640,360))


global found_eyes
found_eyes=False

while videoreader.isOpened():
    ret,frame=videoreader.read()
    audio_frame,val=player.get_frame()
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #print(len(faces))
    if len(faces)==0:
        found_eyes=False
    else:
        found_eyes=True


    if not ret:
        print("Can't read file")

    #Pausing stuff
    if found_eyes==False:
        frame=pauseframe
    else:
        frame=frame

    cv2.imshow('Playing Video',frame)
    if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame



    if cv2.waitKey(1)==ord('q'):
        break
videoreader.release()
cap.release()
cv2.destroyAllWindows()

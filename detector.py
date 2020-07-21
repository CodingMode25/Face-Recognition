#Copyright Sitesh Sawant (sawantsitesh21.ss@gmail.com)

import cv2,os
import numpy as np
from PIL import Image
from gtts import gTTS
# Language in which you want to convert 
path = os.path.dirname(os.path.abspath(__file__))
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(path+r'\trainer\trainer.yml')
faceCascade = cv2.CascadeClassifier('C:\\Users\\Sitesh21\\Desktop\\Sitesh Sawant\\123\\Face-Recognition-master\\Classifiers\\face.xml');

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX #Creates a font 
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
        cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        if(nbr_predicted==66):
             nbr_predicted='Obama'
             
        elif(nbr_predicted==21):
             nbr_predicted='Me-Sitesh Sawant'
             
        elif(nbr_predicted==1):
             nbr_predicted='Shivani Nevgi'

             
        cv2.putText(im,str(nbr_predicted), (x,y),cv2.FONT_HERSHEY_SIMPLEX, 1, 255)#Draw the text
        cv2.imshow('im',im)
        cv2.waitKey(10)

        








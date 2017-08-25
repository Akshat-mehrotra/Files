import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('face.xml')
eye_cascade = cv2.CascadeClassifier('eye.xml')
noses = cv2.CascadeClassifier("Nariz.xml")
mouths = cv2.CascadeClassifier('Mouth.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    th = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(th, 1.2, 7)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.rectangle(th,(x,y),(x+w,y+h),(255,0,0),2)
        
        roi_gray = th[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray,1.3, 7)
        print(len(faces))
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            cv2.rectangle(roi_gray,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            
            nose = noses.detectMultiScale(roi_gray,1.3, 6)            
            for (nx,ny,nw,nh) in nose:
               cv2.rectangle(roi_color,(nx,ny),(nx+nw,ny+nh),(0,0,255),2)
               cv2.rectangle(roi_gray,(nx,ny),(nx+nw,ny+nh),(0,0,255),2)

               mouth = mouths.detectMultiScale(roi_gray, 1.3,12)
               for (mx,my,mw,mh) in mouth:
                    cv2.rectangle(roi_color,(mx,my),(mx+mw,my+mh),(0,255,255),2)
                                  
                    cv2.rectangle(roi_gray,(mx,my),(mx+mw,my+mh),(0,255,255),2)       
    cv2.imshow('img',img)
    cv2.imshow("", th)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

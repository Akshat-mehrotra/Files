import numpy as np
import cv2

car_cascade = cv2.CascadeClassifier('car.xml')


capture = cv2.VideoCapture(0)

while True:
	screen = np.zeros((512,512,3), np.uint8)

	font = cv2.FONT_HERSHEY_SIMPLEX

	cv2.putText(screen,'pump 1(as this is the first cam) - ',(30,500), font, 1,(255,255,255),2)
    
    ret, img = capture.read()
    th = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cars = face_cascade.detectMultiScale(th, 1.2, 7)
    if cars:
		print(len(cars))
		cv2.rectangle(screen, (30, 550), (130,650))
               
    #cv2.imshow('img',img)
   	#cv2.imshow("", th)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

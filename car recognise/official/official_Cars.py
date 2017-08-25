import numpy as np
import cv2
from time import sleep
from time import strftime as st
car_cascade = cv2.CascadeClassifier('cars.xml')
car_cascade2 = cv2.CascadeClassifier('cars3.xml')

def main(font, capture, pump):
	while True:
		color = (255,255,255)
		ret = True
		
		ret, img = capture.read()
	    
		
		if ret:
			th = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			
			cars = car_cascade.detectMultiScale(img, 1.06, 2)
			cars2 = car_cascade2.detectMultiScale(th, 1.4, 4)
			if len(cars) > 0 or len(cars2) > 0:
				sleep(2)
				if len(cars) > 0:
					with open('‪C:\\Users\Akshat\\Desktop\\Stoping cars.txt') as file:
						file.write('{}'.format(st("%d/%m/%Y-%X : ONE CAR FILLED ITS TANK!")))

				# for (x,y,w,h) in cars:
				# 	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
				# 	cv2.putText(img, '{}'.format(len(cars)),(0, 20), font,1 , (0,0,0), 2)

				# 	for (ex, ey, ew, eh) in cars2:
				# 		cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)


			
			#cv2.imshow("img",img) 
			k = cv2.waitKey(30) & 0xff

		else:
				cv2.putText(img, 'the cam is not responding',(0, 20), font,1 , (0,0,0), 2)
				k = cv2.waitKey(30) & 0xff	

		k = cv2.waitKey(30) & 0xff
		if k == 27:
			break
		
	capture.release()
	cv2.destroyAllWindows()	
pump = [(30, 100),(30, 145)]
capture = cv2.VideoCapture('y.avi')
main(capture=capture, font=cv2.FONT_HERSHEY_SIMPLEX, pump=pump[0])
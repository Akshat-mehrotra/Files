
import numpy as np
import cv2
from time import sleep
from time import strftime as st


car_cascade = cv2.CascadeClassifier('cars.xml')
#car_cascade2 = cv2.CascadeClassifier('cars3.xml')
						# add x_y1 and x_y2 for the roi
pump = 'yh.avi'
capture = cv2.VideoCapture(pump)

def main(font, capture, pump,height = 1080, width = 1920):
	
	
	while True:
		#roi = img[height:height from the bottom+height from the top to be cut off the screen, column:width1 from the left to be cut off from the screen+width2 from where the width1 ends]﻿
		r, i= capture.read()
		ret, img = capture.read()
		img1 = img[height:, 1:width]
		#img1=img[110:300, 145:520]
		if ret:
			
			th = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			cars = car_cascade.detectMultiScale(th, 1.04, 3)
			#cars2 = car_cascade2.detectMultiScale(th, 1.4, 4)
			if len(cars) > 0:
				sleep(2)
				if len(cars) > 0:
					with open("C:\\Users\Akshat\\Desktop\\Stoping cars.txt", "a") as file:
						date_time = st("%d/%m/%Y-%X")
						file.write('{} : pump {} is occupied\n'.format(date_time, pump))
						print('found {} cars'.format(len(cars)))

					#for (x,y,w,h) in cars:
						#cv2.rectangle(img,(x,y),(x+h,y+w),(255,0,0),2)
						#cv2.putText(img, '{}'.format(len(cars)),(0, 20), font,1 , (0,0,0), 2)

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

main(capture=capture, font=cv2.FONT_HERSHEY_SIMPLEX, pump=pump)


import numpy as np
import cv2
from time import sleep
from time import strftime as st


car_cascade = cv2.CascadeClassifier('cars.xml') # define the cascade

						
pump = '0' #the pump number i.e. the cam number
capture = cv2.VideoCapture(pump) #capture the video feed from the pump camera

def main(font, capture, pump,height = 1080, width = 1920):
	
	
	while True:
		
		# NOTHING IMPORTANT -->> r, i= capture.read()
		ret, img = capture.read()
		#roi = img[height:height from the bottom+height from the top to be cut off the screen, column:width1 from the left to be cut off from the screen+width2 from where the width1 ends]
		img1 = img[height:, 1:width] # the ROI of the image 
		# example of the DEFINING THE ROI img1=img[110:300, 145:520]
		if ret:
			
			th = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converting the colour from the orignal feed to the BLACK AND WHITE 
			cars = car_cascade.detectMultiScale(th, 1.04, 3) # detect the objects
			
			''' the next few lines will check if the cars cascade object found any objects that it recognizes 
			and then wait for 2 seconds then check again if it again sees the cars, if it does, it will append
			to the 'stoping cars.txt' file 
			'''
			if len(cars) > 0:
				sleep(2)
				if len(cars) > 0:
					try:
						with open("C:\\Users\Akshat\\Desktop\\occupied pumps.txt", "a") as file:
							date_time = st("%d/%m/%Y-%X")
							file.write('{} : pump {} is occupied\n'.format(date_time, pump))
						# this is for debuging -> print('found {} cars'.format(len(cars)))
					except:
						with open("~/Desktop/occupied pumps.txt", "a") as file:
							date_time = st("%d/%m/%Y-%X")
							file.write('{} : pump {} is occupied\n'.format(date_time, pump))
					'''in the development stage if you want to check what cars it sees
					uncoment the following lines'''
					
					#for (x,y,w,h) in cars:
						#cv2.rectangle(img,(x,y),(x+h,y+w),(255,0,0),2)
						#cv2.putText(img, '{}'.format(len(cars)),(0, 20), font,1 , (0,0,0), 2)
			
			#cv2.imshow("img",img) 
			k = cv2.waitKey(30) & 0xff # wait for the esc key to be pressed to get out of the loop

			
			k = cv2.waitKey(30) & 0xff
			if k == 27:
				break
		else:
				print("cam is not responding!!!")
				# NOTHING IMPORTANT -->>cv2.putText(img, 'the cam is not responding',(0, 20), font,1 , (0,0,0), 2)
				k = cv2.waitKey(30) & 0xff	
				if k == 27:
					break
		
	capture.release()
	cv2.destroyAllWindows()	

main(capture=capture, font=cv2.FONT_HERSHEY_SIMPLEX, pump=pump)

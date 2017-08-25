import numpy as np
import cv2

car_cascade = cv2.CascadeClassifier('cars.xml')
car_cascade2 = cv2.CascadeClassifier('cars3.xml')

def main(font, capture, pump):
	while True:
		#screen = np.zeros((1080,1920,3),np.uint8)
		color = (255,255,255)
		#screen[:] = color
		ret = True
		
		ret, img = capture.read()
		#for i in range(len(pump)):
			#cv2.putText(screen,'pump {} (as this is the cam number) - '.format(i),pump, font, 1,(0,0,0),2 )
	    
		
		if ret:
			th = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			
			cars = car_cascade.detectMultiScale(img, 1.06, 2)
			if len(cars)>0:
				for (x,y,w,h) in cars:
					cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
					cv2.putText(img, '{}'.format(len(cars)),(0, 20), font,1 , (0,0,0), 2)
					##roi_gray = gray[y:y+h, x:x+w]
					##roi_color = img[y:y+h, x:x+w]
					cars2 = car_cascade2.detectMultiScale(th, 1.4, 4)
					for (ex, ey, ew, eh) in cars2:
						cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)


			
			# if len(cars)>0:
			# 	for i in pump:
			# 		cv2.rectangle(screen, (pump[0], pump[1]+20), (pump[0]+20, pump[1]+40), (0,255,0), 2)	
			# else:
			# 	for i in pump:
			# 		cv2.rectangle(screen, (pump[0], pump[1]+20), (pump+20, pump[1]+40), (0,0,255), 2)	
			cv2.imshow("img",img) 
			k = cv2.waitKey(30) & 0xff

		else:
			
				#cv2.putText(screen,'something went wrong!', (pump[0], pump[1]+20),font, 1,(0,0,0),2)
				k = cv2.waitKey(30) & 0xff	
		#cv2.imshow("img",screen)

		k = cv2.waitKey(30) & 0xff
		if k == 27:
			break
		
	capture.release()
	cv2.destroyAllWindows()	
pump = [(30, 100),(30, 145)]
capture = cv2.VideoCapture('y.avi')
#capture = cv2.VideoCapture(0)						# change this pump[0] when doing the threading
main(capture=capture, font=cv2.FONT_HERSHEY_SIMPLEX, pump=pump[0])
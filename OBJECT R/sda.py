import cv2
import numpy as np
cap = cv2.VideoCapture(1)
while True:
    
    ret, img = cap.read()
    cv2.imshow('img',img)

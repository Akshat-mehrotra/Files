import cv2
import numpy as np

cap = cv2.VideoCapture(0)

for _ in range(1):
    ret, frame = cap.read()
    print(ret)
    cv2.imwrite("akshat.png", frame)

import numpy as np
import random
import cv2

j = 0
i = 0
height = 1000
width = 1000
blank_image = np.zeros((height,width,3), np.uint8)
while j!=999:
    
    px = blank_image[j,i]
    
    px[0] = random.randint(0,256)
    px[1] = random.randint(0,256)
    px[2] = random.randint(0,256)

    if i == 999:
        j+=1
        i=0
    i+=1    
cv2.imshow('lol',blank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

from PIL import ImageGrab
import os
import time

#nc –v –w 99999999999999999999 –p 1234 –l < C:\Users\Shannon\Desktop\technolust.txt
while True:
    screen = ImageGrab.grab()
    screen.save('F:\\junkfiles\\images\\screen.png')
    os.system('nc –v –w 99999999999999999999 –p 1234 –l < F:\\junkfiles\\images\\screen.png')
    time.sleep(10)

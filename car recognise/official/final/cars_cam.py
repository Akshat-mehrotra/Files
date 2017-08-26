import cv2
import numpy as np

from time import strftime as st

car_cascade = cv2.CascadeClassifier('cars.xml') # define the cascade


class Cam:
    def __init__(self, cam_num):
        self.feed = cv2.VideoCapture(cam_num)
        is_feed, self.img = self.feed.read()

        if is_feed:
            self.main(cam_num=cam_num)

    def main(self, cam_num):
        second_frame = 0
        frames = []
        #img1=0
        while True:

            th = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            cars = car_cascade.detectMultiScale(th, 1.04, 3)
            #print(frames)
            frames.append(cars)

            if second_frame != 2:
                second_frame += 1
            elif len(cars) > 0 and second_frame == 2:

                frame_change = self.check_cord(frames[0], frames[1])
                if not frame_change:
                    #for (x, y, w, h) in cars:
                        #img1 = cv2.rectangle(self.img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    try:
                        with open("C:\\Users\Akshat\\Desktop\\occupied pumps.txt", "a") as file:
                            date_time = st("%d/%m/%Y-%X")
                            file.write('{} : pump {} is occupied\n'.format(date_time, cam_num))
                            # this is for debugging -> print('found {} cars'.format(len(cars)))
                            print('found {} cars'.format(len(cars)))
                    except:
                        with open("~/Desktop/occupied pumps.txt", "a") as file:
                            date_time = st("%d/%m/%Y-%X")
                            file.write('{} : pump {} is occupied\n'.format(date_time, cam_num))
                    del frames[0]

            #cv2.imshow('img', img1)
    def check_cord(self, prv_frame, current_frame):
        if prv_frame.all() == current_frame.all():
            return False
        else:
            return True
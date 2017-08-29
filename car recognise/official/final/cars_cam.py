import cv2
import numpy as np

from time import strftime as st


car_cascade = cv2.CascadeClassifier('other_files/cars.xml')  # define the cascade


def init(cam_num, alt_feed, coordinates, area):
    try:
        feed = cv2.VideoCapture(cam_num)
    finally:
        feed = cv2.VideoCapture(alt_feed)
        print('YOLO')
    main(cam_num=cam_num, feed=feed, coordinates=coordinates, area=area)


def main(cam_num, feed, coordinates, area):
    second_frame = 0
    frames = []
    date_time = 0
    while True:

        is_feed, img = feed.read()
        if is_feed:
            # print(type(coordinates[0]), type(coordinates[1]), type(coordinates[2]), type(coordinates[3]))
            try:
                img1 = img[coordinates[0]: coordinates[1], coordinates[2]:coordinates[3],]
            except IndexError:
                print('there was a index error while defining the ROI of the image so the full image has been taken')
                img1 = img
            # cv2.imshow('img2', img1)
            th = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            cars = car_cascade.detectMultiScale(th, 1.04, 3)

            if len(cars) > 0 and second_frame != 2:
                frames.append(cars[0])

            if second_frame != 2 and len(cars) > 0:
                second_frame += 1
            elif len(cars) > 0 and second_frame == 2 and len(frames) == 2:
                frame_change = check_cord(prv_frame=frames[0], current_frame=frames[1])
                if not frame_change:
                    for (x, y, w, h) in cars:
                        img1 = cv2.rectangle(img1, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    try:
                        if date_time != st("%d/%m/%Y-%X"):
                            with open("C:\\Users\Akshat\\Desktop\\occupied pump {}.txt".format(area[-1]), "a") as file:
                                date_time = st("%d/%m/%Y-%X")
                                file.write('{} : pump {} is occupied\n'.format(date_time, area[-1]))
                                # this is for debugging -> print('found {} cars'.format(len(frames)))

                    except:
                        if date_time != st("%d/%m/%Y-%X"):
                            with open("~/Desktop/occupied pump {}.txt".format(area[-1])) as file:
                                date_time = st("%d/%m/%Y-%X")
                                file.write('{} : pump {} is occupied\n'.format(date_time, area[-1]))
                del frames[0]
                second_frame -= 1
            cv2.imshow('img', img1)

        else:
            print('CAM IS NOT RESPONDING OR THE VIDEO FEED ENDED')
            break
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    feed.release()
    cv2.destroyAllWindows()


def check_cord(prv_frame, current_frame):
    if prv_frame.all() == current_frame.all():
        return False
    else:
        return True

import cars_cam
import threading


def main():

    cam_object_list = []
    thread_counter = []
    cam1 = cars_cam.Cam('yh.avi')
    cam_object_list.append(1)
    for i in len(cam_object_list):
        exec('thread_counter.append(threading.Thread(target=cam{}))'.format(str(i)))

    for i in thread_counter:
        i.start()

if __name__ == '__main__':
    main()
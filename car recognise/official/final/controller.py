import cars_cam
import threading
import configparser

def main():
    config = configparser.ConfigParser()
    config.read("other_files/settings.ini")
    thread_counter = []
    sections = config.sections()

    coordinates = []

    for j in sections:
        c = config[j]
        for i in ('top left x', 'top left y', 'height', 'width'):

            try:
                coordinates.append(int(c.get(i)))
            except ValueError:
                print('hello')
                break
        cam_num = int(config[j]['cam num'])                                  # this is the cam number  the stuff bellow this
        cam_num = 'other_files/video1.avi'

        thread_counter.append(threading.Thread(target=cars_cam.init, args=(cam_num, coordinates, j,)))
    print(coordinates)
    for i in thread_counter:
        i.start()

if __name__ == '__main__':
    main()

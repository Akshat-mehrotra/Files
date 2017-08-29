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
        for i in ('row start', 'row end', 'column start', 'column end'):
            c = config[j]
            try:
                coordinates.append(int(c.get(i)))
            except ValueError:
                print('hello')
                break
        cam_num = config[j]['cam num']                                  # this is the cam number  the stuff bellow this
        print(cam_num, cam_num)
        alt_feed = 'other_files/yh.avi'
        thread_counter.append(threading.Thread(target=cars_cam.init, args=(cam_num, alt_feed, coordinates, j,)))
    print(coordinates)
    for i in thread_counter:
        i.start()

if __name__ == '__main__':
    main()

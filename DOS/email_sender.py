import time
import smtplib

def send_it():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    msg = ""
    server.login("akshatmehrotra2004@gmail.com", "my password i wont type BTW this isnt my password")
    with open("F:/detail.txt", "r") as a:

        msg += a.read()

    server.sendmail("akshatmehrotra2004@gmail.com", "captain.akshat.2004@gmail.com", msg)
    server.quit()
    time.sleep(300)

import RPi.GPIO as GPIO

class Servo:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN)

    def run(self):
        pwm = GPIO.PWM(self.pin, 50 )
        pwm.start(12)
        sleep(0.5)
        pwm.ChangeDutyCycle(4)
        sleep(0.5)

        GPIO.cleanup()

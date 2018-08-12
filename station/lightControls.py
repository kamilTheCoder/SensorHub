import RPi.GPIO as GPIO
import time

class LightControl:
    __red = None
    __green = None
    __blue = None

    def __init__(self, r, g, b, initialize = False):
        self.__red = r
        self.__green = g
        self.__blue = b

        if initialize:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)

        GPIO.setup(self.__red, GPIO.OUT)
        GPIO.setup(self.__green, GPIO.OUT)
        GPIO.setup(self.__blue, GPIO.OUT)


    def __flashLed(self, led, timer):
        GPIO.output(led, GPIO.HIGH)
        time.sleep(timer)
        GPIO.output(led, GPIO.LOW)


    def flashRed(self, timer = 0.01):
        self.__flashLed(self.__red, timer)

    def flashGreen(self, timer = 0.01):
        self.__flashLed(self.__green, timer)

    def flashBlue(self, timer = 0.01):
        self.__flashLed(self.__blue, timer)

    def flashRgb(self, timer = 0.01):
        self.__flashLed(self.__red, timer)
        self.__flashLed(self.__green, timer)
        self.__flashLed(self.__blue, timer)
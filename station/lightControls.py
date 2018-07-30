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


    def __flashLed(self, led, time):
        GPIO.output(led, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led, GPIO.LOW)


    def flashRed(self, time = 1):
        self.__flashLed(self.__red, time)

    def flashGreen(self, time = 1):
        self.__flashLed(self.__green, time)

    def flashBlue(self, time = 1):
        self.__flashLed(self.__blue, time)

    def flashRgb(self, time = 1):
        self.__flashLed(self.__red, time)
        self.__flashLed(self.__green, time)
        self.__flashLed(self.__blue, time)
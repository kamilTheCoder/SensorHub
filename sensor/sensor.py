import RPi.GPIO as GPIO
import dht11

class Sensor:
    def __init__(self, gpio):
        self.gpio = gpio
    
    def read(self):
        return None


class TempSensor(Sensor):
    instance = None

    def __init__(self, gpio):
        super().__init__(self, gpio)
        self.instance = dht11.DHT11(pin=self.gpio)

    def read(self):
        return self.instance.read()


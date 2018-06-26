import socket

class Sensor:
    def __init__(self, gpio):
        self.gpio = gpio
    
    def read(self):
        return None

class TempSensor(Sensor):
    def read(self):
        return 8
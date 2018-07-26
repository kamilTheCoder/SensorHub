import RPi.GPIO as GPIO
import DHT11_Python_master.dht11 as dht11

class Sensor:
    def __init__(self, gpio, name):
        self.gpio = gpio
        self.name = name
    
    def read(self):
        return None

    def getInfo(self):
        return (self.name, self.gpio)


class Dht11Sensor(Sensor):
    instance = None

    def __init__(self, gpio):
        super().__init__(gpio, 'DHT11')
        print("Instanciating DHT11...")
        self.instance = dht11.DHT11(pin=self.gpio)

    def read(self):
        return self.instance.read()


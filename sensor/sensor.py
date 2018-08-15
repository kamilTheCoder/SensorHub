import RPi.GPIO as GPIO
import DHT11_Python_master.dht11 as dht11

class Sensor:
    _gpio = None
    __name = None

    def __init__(self, gpio, name):
        self._gpio = gpio
        self.__name = name
    
    def read(self):
        return None

    def getInfo(self):
        return (self.__name, self._gpio)


class Dht11Sensor(Sensor):
    instance = None

    def __init__(self, gpio):
        super().__init__(gpio, 'DHT11')
        self.instance = dht11.DHT11(pin=self._gpio)

    def read(self):
        return self.instance.read()

class LDR(Sensor):

    def __init__(self, gpio):
        super().__init__(gpio, 'LDR')
        GPIO.setup(gpio,GPIO.IN)
        
    def read(self):
        print("pretending to read the photosensor...")
        return 0

class LM393Sound(Sensor):

    def __init__(self, gpio):
        super().__init__(gpio, 'LM393Sound')
        GPIO.setup(gpio,GPIO.IN)
        
    def read(self):
        readings = []
        for _ in range(0,100):
            readings.append(GPIO.input(self._gpio) == GPIO.LOW)

        return True in readings

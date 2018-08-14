import RPi.GPIO as GPIO
import DHT11_Python_master.dht11 as dht11

class Sensor:
    __gpio = None
    __name = None

    def __init__(self, gpio, name):
        self.__gpio = gpio
        self.__name = name
    
    def read(self):
        return None

    def getInfo(self):
        return (self.__name, self.__gpio)


class Dht11Sensor(Sensor):
    instance = None

    def __init__(self, gpio):
        super().__init__(gpio, 'DHT11')
        print("Instanciating DHT11...")
        self.instance = dht11.DHT11(pin=gpio)

    def read(self):
        return self.instance.read()

class LDR(Sensor):

    def __init__(self, gpio):
        super().__init__(gpio, 'LDR')
        print("Instanciating LDR...")
        GPIO.setup(gpio,GPIO.IN)
        
    def read(self):
        print("pretending to read the photosensor...")
        return 0

class LM393Sound(Sensor):

    def __init__(self, gpio):
        super().__init__(gpio, 'SOUND')
        print("Instanciating LM393 Sound Sensor...")
        GPIO.setup(gpio,GPIO.IN)
        
    def read(self):
        return GPIO.input(self.__gpio) == GPIO.LOW
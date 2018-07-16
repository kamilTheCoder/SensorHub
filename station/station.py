import RPi.GPIO as GPIO
from sensor import TempSensor
import socket
import json

class Station:

    dht11 = None

    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 1984
        self.bufferSize = 1024

        self.ip, self.port, self.bufferSize, self.sensors = self.loadConfig()
        
        self.initGpio()

    def sendData(self, message):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.send(message.encode())

        response = s.recv(self.bufferSize)
        s.close()
        
        return response

    def echo(self, msg):
        print(msg)

    def loadConfig(self):
        print("Loading configuration...")
        with open('config.json', 'r') as f:
            config = json.load(f)

        ip = config['station']['ip']
        port = config['station']['port']
        buffSize = config['station']['buffSize']

        sensors = []
        for sensor in config['sensors']:
            name = sensor['name']
            pin = sensor['pin']
            sensors.append((name, pin))

        return ip, port, buffSize, sensors

    def printConfig(self):
        print("configuration:")
        print("\tip:\t\t{}".format(self.ip))
        print("\tport:\t\t{}".format(self.port))
        print("\tbuffSize:\t{}".format(self.bufferSize))
        print("sensors:")
        for s in self.sensors:
            print("\tname: {}\tpin: {}".format(s[0], s[1]))

    def initGpio(self):
        print("Initialising GPIO...")
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()

    def initDht11(self):    
        print("Initialising DHT11...") 
        self.dht11 = TempSensor(self.sensors[0][1])

    def readDht11(self):
        if self.dht11 is None:
            print("Warning: no DHT11 found")
            return
        
        #print("Reading DHT11...")  
        read = self.dht11.read()
        print(read)
        return read



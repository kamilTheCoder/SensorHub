import RPi.GPIO as GPIO
import sensor.sensor as sensor
import socket
import json

class Station:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 1984
        self.bufferSize = 1024

        self.ip, self.port, self.bufferSize = self.loadConfig()

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
        with open('config.json', 'r') as f:
            config = json.load(f)

        ip = config['station']['ip']
        port = config['station']['port']
        buffSize = config['station']['buffSize']

        return ip, port, buffSize

    def printConfig(self):
        print("configuration:\nip:\t\t{}\nport:\t\t{}\nbuffSize:\t{}".format(self.ip, self.port, self.bufferSize))

    def initGpio(self):
        print("Initialising GPIO...")
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()

    def initDht11(self, gpio):
        self.dht11 = sensor.TempSensor(gpio)

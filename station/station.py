import RPi.GPIO as GPIO
import sensor.sensor as sensors
import socket
import json

class Station:

    dht11 = None

    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 1984
        self.bufferSize = 1024

        self.ip, self.port, self.bufferSize, sensorList = self.__loadConfig()
        self.sensors = self.__initSensors(sensorList)        
        self.__initGpio()

    def sendData(self, message):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.send(message.encode())

        response = s.recv(self.bufferSize)
        s.close()
        
        return response


    def __loadConfig(self):
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
            print("\tname: {}\tpin: {}".format(s.name, s.gpio))


    def __initGpio(self):
        print("Initialising GPIO...")
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()


    def __initSensors(self, sensorList): 
        print("Initialising sensor list")
        result = []
        for sensorConf in sensorList:
            if sensorConf[0] == 'DHT11': 
                print("\tFound DHT11 at pin {}".format(sensorConf[1]))
                result.append(sensors.Dht11Sensor(sensorConf[1]))
            else:
                print("\WARNING: Unknown sensor {}".format( sensorConf[0]))

        return result


    def readSensor(self,i):
        if len(self.sensors) < i+1:
            print("WARNING: Trying to access sensor #{}, which does not exist".format(i))
            return None

        return self.sensors[i].read()

    def readAllSensors(self):
        reads = []
        for s in self.sensors:
            reads.append(s.read())

        return reads


    def readDht11(self):
        for s in self.sensors:
            if isinstance(s, sensors.Dht11Sensor):
                return s.read()
    
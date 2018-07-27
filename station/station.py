import RPi.GPIO as GPIO
import sensor.sensor as sensors
from dbConfig import DbConfig
import json
import mysql.connector
import datetime
import time

class Station:
    __dbConfig = None
    __DHT11 = None
    __sensors = []

    def __init__(self):
        self.__dbConfig, sensorList = self.__loadConfig()
        self.__sensors = self.__initSensors(sensorList)        
        self.__initGpio()


    def __initGpio(self):
        print("Initialising GPIO...")
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()


    def __initSensors(self, sensorList): 
        print("Initialising sensor list")
        i = 0
        result = []
        for sensorConf in sensorList:
            if sensorConf[0] == 'DHT11': 
                print("\tFound DHT11 at pin {}".format(sensorConf[1]))
                result.append(sensors.Dht11Sensor(sensorConf[1]))
                self.__DHT11 = i
                i += 1
            else:
                print("\tWARNING: Unknown sensor {}".format( sensorConf[0]))

        return result


    def __formatReadings(self, time, temp, hum):
        return ("{0}-{1:02d}-{2:02d}".format(time.year, time.month, time.day),
                "{0:02d}:{1:02d}:{2:02d}".format(time.hour, time.minute, time.second),
                "main",
                temp,
                hum
            )


    def __loadConfig(self):
        print("Loading configuration...")
        with open('config.json', 'r') as f:
            config = json.load(f)
        
        dbName = config['database']['name']
        dbUSer = config['database']['user']
        dbHost = config['database']['host']
        dbTable = config['database']['table']

        dbConfig = DbConfig(dbName, dbUSer, dbHost, dbTable)

        sensors = []
        for sensor in config['sensors']:
            name = sensor['name']
            pin = sensor['pin']
            sensors.append((name, pin))

        return dbConfig, sensors


    def __readSensor(self,i):
        if len(self.__sensors) < i+1:
            print("WARNING: Trying to access sensor #{}, which does not exist".format(i))
            return None

        return self.__sensors[i].read()


    def registerReading(self):
        time, reading = self.tryRead(self.__DHT11)
        temp, hum = reading[0], reading[1]

        if time is None or temp is None or hum is None:
            # invalid reading - skip
            return None

        db = mysql.connector.connect(
            host=self.__dbConfig.getDbHost(),
            user=self.__dbConfig.getDbUser(),
            passwd=self.__dbConfig.getDbPass(),
            database=self.__dbConfig.getDbTable()
            )
        cursor = db.cursor()

        query = "INSERT INTO {} VALUES (%s, %s, %s, %s, %s)".format(self.__dbConfig.getDbTable())
        val = self.__formatReadings(time, temp, hum)

        cursor.execute(query, val)
        db.commit()        
        return val


    def printConfig(self):
        print("configuration:")
        print("sensors:")
        for s in self.__sensors:
            print("\tname: {}\tpin: {}".format(s.name, s.gpio))


    def readAllSensors(self):
        reads = []
        for s in self.__sensors:
            reads.append(s.read())

        return reads


    def tryRead(self, sensor):
        retries = 0
        maxRetries = 10
        result = None
        now = None
        while retries < maxRetries:        
            result = self.__readSensor(sensor)
            now = datetime.datetime.now()

            if result != None and result.is_valid():  
                break
            
            retries += 1

        if retries == maxRetries:
            print("Error: Finished reading after {} failed retries".format(retries))
            return now, None, None

        return now, result.temperature, result.humidity


    def initReadings(self):
        readInterval = 60 # seconds
        repeatLimit = 10
        repeat = 0

        print("Attempting to read...")
        while repeat < repeatLimit:        
            result = self.registerReading()

            if result is None:
                print("\tInvalid reading, continue")
                repeat += 1
                continue

            repeat = 0   
            print("\tTimestamp: {} {}\tTemperature: {}C\tHumidity: {}%".format(
                result[0], result[1], result[3], result[4]
            ))

            time.sleep(readInterval)

        print("\tERROR: stopped reading after {} failed attempts".format(repeatLimit))

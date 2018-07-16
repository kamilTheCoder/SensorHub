from station import Station
import datetime
import time

def main():
    s = Station()
    s.printConfig()

    retries = 0
    maxRetries = 10
    print("Attempting to read...")
    while retries < 10:        
        result = s.readSensor(0)

        if result != None and result.is_valid():
            retries = 0
            print("Data read @ " + str(datetime.datetime.now()))
            print("\tTemperature: %d C" % result.temperature)
            print("\tHumidity: %d %%" % result.humidity)
        else:
            retries += 1
        
        time.sleep(1)
    print("Finished reading after 10 failed retries")


if __name__ == '__main__':
    main()
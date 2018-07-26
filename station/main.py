import station
import datetime
import time

def main():
    s = station.Station()
    s.printConfig()

    s.registerReading()

    # retries = 0
    # maxRetries = 10
    # print("Attempting to read...")
    # while retries < maxRetries:        
    #     result = s.readDht11()

    #     if result != None and result.is_valid():
    #         retries = 0
    #         print("Data read @ " + str(datetime.datetime.now()))
    #         print("\tTemperature: %d C" % result.temperature)
    #         print("\tHumidity: %d %%" % result.humidity)
    #     else:
    #         retries += 1
        
    #     time.sleep(5)
    # print("Finished reading after 10 failed retries")


if __name__ == '__main__':
    main()
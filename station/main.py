import station
import datetime
import time

def main():
    s = station.Station()
    s.printConfig()
    initReadings(s)
    
def initReadings(s):
    readInterval = 60 # seconds
    repeatLimit = 10
    repeat = 0

    print("Attempting to read...")
    while repeat < repeatLimit:        
        result = s.registerReading()

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


if __name__ == '__main__':
    main()
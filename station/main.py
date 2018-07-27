import station
import datetime
import time

def main():
    s = station.Station()
    s.printConfig()
    readInterval = 60 # seconds

    print("Attempting to read...")
    while True:        
        result = s.registerReading()

        print("\tTimestamp: {} {}\tTemperature: {}C\tHumidity: {}%".format(
            result[0], result[1], result[3], result[4]
        ))

        time.sleep(readInterval)


if __name__ == '__main__':
    main()
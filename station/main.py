import station
import datetime
import time

def main():
    s = station.Station()
    s.printConfig()
    readInterval = 60 # seconds

    print("Attempting to read...")
    while True:        
        id, result = s.registerReading()

        print("\tId: {}\tTimestamp: {} {}\tTemperature: {}C\tHumidity: {}%".format(
            id, result[0], result[1], result[3], result[4]
        ))

        time.sleep(readInterval)


if __name__ == '__main__':
    main()
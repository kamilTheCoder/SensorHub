from station import station
import datetime
import time
import sys

def main():
    s = station.Station()
    s.printConfig()

    if len(sys.argv) < 2:
        s.initReadings()
    else:
        s.testSensor(sys.argv[1]) 
    
    
if __name__ == '__main__':
    main()
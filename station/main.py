from station import Station
import datetime
import time

def main():
    s = Station()
    s.printConfig()
    s.initDht11()
    #result = s.readDht11()

    i = 0
    print("Attempting to read...")
    while i < 10:        
        result = s.readDht11()

        if result != None and result.is_valid():
            i = 0
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: %d C" % result.temperature)
            print("Humidity: %d %%" % result.humidity)
        else:
            #print("Read failed. Attempts left: {}".format(10-i))
            i += 1
        
        time.sleep(1)
    print("Finished reading after 10 failed attempts.")



if __name__ == '__main__':
    main()
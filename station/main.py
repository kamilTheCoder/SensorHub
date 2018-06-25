from station import Station
import json


def main():
    ip, port, buffSize = loadConfig()
    
    s = Station(ip, port, buffSize)
    s.echo("hi")

    # ts = TempSensor()
    # print(ts.read())

def loadConfig():
    with open('config.json', 'r') as f:
        config = json.load(f)

    ip = config['station']['ip']
    port = config['station']['port']
    buffSize = config['station']['buffSize']

    return ip, port, buffSize

if __name__ == '__main__':
    main()
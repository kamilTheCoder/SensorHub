import socket

class Sensor:
    def __init__(self, ip = "127.0.0.1", port = 1984, bufferSize = 1024):
        self.ip = ip
        self.port = port
        self.bufferSize = bufferSize

    def sendData(self, message):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.send(message.encode())

        response = s.recv(self.bufferSize)
        s.close()
        
        return response

    def echo(self, msg):
        print(msg)

def main():
    s = Sensor()
    s.echo("hi")

main()
package connection

import (
	"SensorHub/hub/dataReading"
	"SensorHub/hub/processing"
	"bufio"
	"io"
	"log"
	"net"
	"strings"
)

func Open(addr, port string) {
	listener, err := net.Listen("tcp", addr+":"+port)
	if err != nil {
		log.Fatalln(err)
	}

	log.Println("Listening on", addr+":"+port)

	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Println(err)
			continue
		}

		log.Println("Accepted connection from", conn.RemoteAddr().String())
		go handle(conn)
	}

}

func handle(conn net.Conn) {
	reader := bufio.NewReader(conn)
	for {
		msg, err := reader.ReadString('\n')
		if err != nil {
			if err == io.EOF {
				log.Println("Connection with", conn.RemoteAddr().String(), "terminated.")
				return
			}

			log.Println(err)
			continue
		}

		msg = strings.TrimSpace(msg)
		log.Println("Read from", conn.RemoteAddr().String()+":", msg)
		reading, err := dataReading.Parse(msg)
		if err != nil {
			log.Println(err)
			continue
		}

		processing.SaveDataReading(reading)
	}
}

package connection

import (
	"SensorHub/hub/dataReading"
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
		log.Println("Reading from", conn.RemoteAddr().String())
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
		go dataReading.Parse(msg)
		log.Println("Message from", conn.RemoteAddr().String(), "'"+msg+"' passed to the data reading handler...")

	}
}

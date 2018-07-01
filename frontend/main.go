package main

import "SensorHub/hub/connection"

func main() {
	connection.Open("localhost", "1984")
}

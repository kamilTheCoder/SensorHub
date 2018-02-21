package dataReading

import (
	"encoding/json"
	"log"
)

func Handle(reading string) {
	var r Reading
	err := json.Unmarshal([]byte(reading), &r)
	if err != nil {
		log.Println("Problem unmarshalling message '"+reading+"': ", err.Error())
		return
	}

	log.Println(r)
}

type Reading struct {
	StationID  string
	Timestamp  string
	SensorType string
	Payload    string
	Err        string
}

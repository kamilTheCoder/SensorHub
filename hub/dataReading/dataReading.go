package dataReading

import (
	"encoding/json"
	"log"
)

func Handle(reading string) {
	var r DataReading
	err := json.Unmarshal([]byte(reading), &r)
	if err != nil {
		log.Println("Problem unmarshalling message '"+reading+"': ", err.Error())
		return
	}

	log.Println(r.StationID + "\t" + r.SensorType + "\t" + r.Payload + "\t" + r.Err)
}

type DataReading struct {
	StationID  string
	Timestamp  string
	SensorType string
	Payload    string
	Err        string
}

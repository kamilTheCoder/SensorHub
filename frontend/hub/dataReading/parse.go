package dataReading

import (
	"encoding/json"
	"log"
)

func Parse(reading string) (DataReading, error) {
	var r DataReading
	err := json.Unmarshal([]byte(reading), &r)
	if err != nil {
		log.Println("Problem unmarshalling message '"+reading+"': ", err.Error())
		return r, err
	}

	log.Println(r.StationID + "\t" + r.SensorType + "\t" + r.Payload + "\t" + r.Err)
	return r, err
}

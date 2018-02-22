package dataReading

import (
	"encoding/json"
	"log"
	"testing"
)

func TestHandleUnmarshallsCorrectJson(t *testing.T) {
	reading := createTestReading()
	log.Println(reading)
	data, err := json.Marshal(reading)
	if err != nil {
		t.Error(err)
	}
	log.Println(data)

	Handle(string(data))
}

func createTestReading() DataReading {
	return DataReading{"test", "20180121225932", "temperature", "20.5", ""}
}

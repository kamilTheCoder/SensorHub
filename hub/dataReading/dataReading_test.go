package dataReading

import (
	"testing"
)

func TestParseUnmarshallsCorrectJson(t *testing.T) {
	result, err := Parse(createTestReadingString())
	if err != nil {
		t.Error(err)
	}

	if result != createTestReading() {
		t.Error("Expected", createTestReading(), "got", result)
	}
}

func TestParseReturnsErrorWhenInputInvalid(t *testing.T) {
	var emptyReading DataReading
	expectedError := "invalid character 'I' looking for beginning of value"
	result, err := Parse("Invalid string")
	if err == nil {
		t.Error("Expected error to be thrown")
	} else if err.Error() != expectedError {
		t.Error("Expected error", expectedError, "got", err.Error())
	}

	if result != emptyReading {
		t.Error("Expected", emptyReading, "got", result)
	}
}

func createTestReadingString() string {
	return `{"StationID":"test","Timestamp":"20180121225932","SensorType":"temperature","Payload":"20.5","Err":""}`
}

func createInvalidTestReadingString() string {
	return `{"StationID":"test","INVALID":"INVALID","SensorType":"temperature","Payload":"20.5","Err":""}`
}

func createTestReading() DataReading {
	return DataReading{"test", "20180121225932", "temperature", "20.5", ""}
}

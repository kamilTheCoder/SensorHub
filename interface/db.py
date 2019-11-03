# import mysql.connector


def PrintReadings(reading):
    print("\tTime: {} {}\tTemp: {}C\tHum: {}%\tSound: {}".format(
                reading[0], reading[1], reading[3], reading[4], reading[5]
            ))


def SaveReadingToDb(val):
    # db = mysql.connector.connect(
    #     host=self.__dbConfig.getDbHost(),
    #     user=self.__dbConfig.getDbUser(),
    #     passwd=self.__dbConfig.getDbPass(),
    #     database=self.__dbConfig.getDbName()
    #     )
    # cursor = db.cursor()

    # query = "INSERT INTO {} VALUES (%s, %s, %s, %s, %s, %s)".format(self.__dbConfig.getDbTable())
    # cursor.execute(query, val)
    # db.commit() 
    print("unimplemented")
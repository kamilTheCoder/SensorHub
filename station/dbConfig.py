class DbConfig:
    def __init__(self, name, user, host, table):
        self.__dbUser = user
        self.__dbPass = "password"
        self.__dbHost = host
        self.__dbName = name
        self.__dbTableName = host

    
    def getDbName(self): 
        return self.__dbName

    def getDbUser(self): 
        return self.__dbName

    def getDbPass(self): 
        return self.__dbPass

    def getDbTable(self): 
        return self.__dbTableName

    def getDbHost(self): 
        return self.__dbHost
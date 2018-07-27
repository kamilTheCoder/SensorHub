import unittest
from station.dbConfig import DbConfig

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.name = "testDbName"
        self.psswd = "testPass"
        self.host = "testHost"
        self.user = "testUser"
        self.table = "testTableName"

        self.dbConf = DbConfig(self.name, self.user, self.host, self.table)

    def test_getDbName(self):
        self.assertEqual(self.name, self.dbConf.getDbName())

    def test_getDbPass(self):
        self.assertEqual(self.psswd, self.dbConf.getDbPass())

    def test_getDbHost(self):
        self.assertEqual(self.host, self.dbConf.getDbHost())
        
    def test_getDbUser(self):
        self.assertEqual(self.user, self.dbConf.getDbUser())

    def test_getDbTable(self):
        self.assertEqual(self.table, self.dbConf.getDbTable())


if __name__ == '__main__':
    unittest.main()
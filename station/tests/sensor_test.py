import unittest

class TestMyTest(unittest.TestCase):
    def test(self):        
        self.assertEqual(3, 4)
        print("hello")

if __name__ == '__main__':
    unittest.main()
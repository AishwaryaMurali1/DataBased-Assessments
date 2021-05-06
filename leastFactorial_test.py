import unittest
from leastFactorial import leastFactorial


class leastFactorial_test(unittest.TestCase):


    def test_edgeCase1(self):
        self.assertEqual(leastFactorial(1), 2)
    
    def test_edgeCase2(self):
        self.assertEqual(leastFactorial(120), 720)

    def test_example1(self):
        self.assertEqual(leastFactorial(17), 24)
    
    def test_example2(self):
        self.assertEqual(leastFactorial(5), 6)

    def test_example3(self):
        self.assertEqual(leastFactorial(106), 120)

if __name__ == "__main__":
    unittest.main()

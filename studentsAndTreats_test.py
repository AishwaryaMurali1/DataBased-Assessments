import unittest
from studentsAndTreats import getLastStudent


class recyclingLipstick_test(unittest.TestCase):


    def test_edgeCase1(self):
        self.assertEqual(getLastStudent(1000000000, 1000000005, 2), 6)

    def test_edgeCase2(self):
        self.assertEqual(getLastStudent(1000000034, 1000000567, 10000), 10532)

    def test_example1(self):
        self.assertEqual(getLastStudent(5,2,1), 2)

    def test_example2(self):
        self.assertEqual(getLastStudent(5,2,2), 3)
    
    def test_example3(self):
        self.assertEqual(getLastStudent(7,19,2), 6)
    
    def test_example4(self):
        self.assertEqual(getLastStudent(3,7,3), 3)

if __name__ == "__main__":
    unittest.main()
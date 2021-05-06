import unittest
from recyclingLipstick import getTotalNumOfLipsticks


class recyclingLipstick_test(unittest.TestCase):


    def test_edgeCase1(self):
        self.assertEqual(getTotalNumOfLipsticks(0,2), 0)

    def test_example1(self):
        self.assertEqual(getTotalNumOfLipsticks(5,2), 9)

    def test_example2(self):
        self.assertEqual(getTotalNumOfLipsticks(15,5), 18)
    
    def test_example3(self):
        self.assertEqual(getTotalNumOfLipsticks(2, 3), 2)

if __name__ == "__main__":
    unittest.main()

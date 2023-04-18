import csv
import unittest
from lab5Search import *

class Testing(unittest.TestCase):
    def test_EuclideanDist(self):
        person1 = ["Person1", 30, 178, 45]
        person2 = ["Person2", 60, 200, 46]
        self.assertEqual(37.21558813185679, EuclideanDistance(person1[1:], person2[1:]))
    
    def test_ComputeAllDistances(self):
        list_person = [["Person1", 30, 178, 45],
                       ["Person2", 60, 176, 82]]
        client = [60, 200, 46]
        self.assertEqual([37.21558813185679, 43.266615305567875], ComputeAllDistances(list_person, client))

    def test_FindMin(self):
        list_person = [1.544, 200.54, 45.222, 0.22, 89]
        self.assertEqual((0.22, 3), FindMin(list_person))

if __name__ == '__main__':
    unittest.main()
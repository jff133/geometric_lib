import unittest
from circle import *


class CircleTest(unittest.TestCase):
    def test_area_1(self):
        self.assertEqual(area(13), 530.929158456675)

    def test_area_2(self):
        self.assertEqual(area(-13), 'Doesn`t exist')
    def test_area_3(self):
        self.assertEqual(area(0), 'Doesn`t exist')

    def test_area_4(self):
        self.assertEqual(area("mv"), 'Incorrect input')

    def test_area_5(self):
        self.assertEqual(area(True), 'Incorrect input')

    def test_perimeter_1(self):
        self.assertEqual(perimeter(13), 81.68140899333463)

    def test_perimeter_2(self):
        self.assertEqual(perimeter(-13), 'Doesn`t exist')

    def test_perimeter_3(self):
        self.assertEqual(perimeter(0), 'Doesn`t exist')

    def test_perimeter_4(self):
        self.assertEqual(perimeter('mv'), 'Incorrect input')

    def test_perimeter_5(self):
        self.assertEqual(perimeter(True), 'Incorrect input')

if __name__ == '__main__':
    unittest.circle()

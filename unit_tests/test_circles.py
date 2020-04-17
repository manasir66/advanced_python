import unittest
from circles import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):

  def test_area(self):

    #test for radius >= 0
    self.assertAlmostEqual(circle_area(1), round(pi, 6))
    #pi is alomost equal to the value of area when r = 1
    #here we are checking on that to see if the test case passes

    self.assertAlmostEqual(circle_area(0), 0)
    #check if the function works for when r = 0 it should be = 0

    self.assertAlmostEqual(circle_area(3.2), round(pi * 3.2**2, 6))


  def test_values(self):

    self.assertRaises(ValueError, circle_area, -2)


  def test_types(self):

    self.assertRaises(TypeError, circle_area, 3+5j)
    self.assertRaises(TypeError, circle_area, True)
    self.assertRaises(TypeError, circle_area, "radiusstring")
    #we test for complex numbers, booleans and strings
import unittest 
import math 
import triangle, circle, rectangle, square
class RectangleTestCase(unittest.TestCase):

    def test_zero_mul(self):
       res = rectangle.area(10, 0)
       self.assertEqual(res, 0)
       
    def test_square_mul(self):
       res = rectangle.area(10, 10)
       self.assertEqual(res, 100)

    def test_negative_on_positive_mul(self):
       res = rectangle.area(10, -20)
       self.assertEqual(res, -200)

    def test_negative_on_negative_mul(self):
       res = rectangle.area(-10, -20)
       self.assertEqual(res, 200)

    def test_double_mul(self):
       res = rectangle.area(1.5, 1.5)
       self.assertEqual(res, 2.25)




    def test_zero_perimeter(self):
       res = rectangle.perimeter(10, 0)
       self.assertEqual(res, 20)
       
    def test_square_perimeter(self):
       res = rectangle.perimeter(10, 10)
       self.assertEqual(res, 40)

    def test_negative_on_positive_perimeter(self):
       res = rectangle.perimeter(10, -10)
       self.assertEqual(res, 0)

    def test_negative_on_negative_perimeter(self):
       res = rectangle.perimeter(-10, -10)
       self.assertEqual(res, -40)

    def test_float_perimeter(self):
       res = rectangle.perimeter(1.5, 1.5)
       self.assertEqual(res, 6)

class CircleTestCase(unittest.TestCase):

    def test_zero_mul(self):
       res = circle.area(0)
       self.assertEqual(res, 0)

    def test_square_mul(self):
       res = circle.area(10) / math.pi
       self.assertEqual(res, 100)

    def test_negative_on_positive_mul(self):
       res = circle.area(-10) / math.pi
       self.assertEqual(res, 100)

    def test_double_mul(self):
       res = circle.area(1.5) / math.pi
       self.assertEqual(res, 2.25)




    def test_zero_perimeter(self):
       res = circle.perimeter(0)
       self.assertEqual(res, 0)

    def test_square_perimeter(self):
       res = circle.perimeter(10) / math.pi
       self.assertEqual(res, 20)

    def test_negative_on_positive_perimeter(self):
       res = circle.perimeter(-10) / math.pi
       self.assertEqual(res, -20)

    def test_double_perimeter(self):
       res = circle.perimeter(1.5) / math.pi
       self.assertEqual(res, 3)

class SquareTestCase(unittest.TestCase):



    def test_zero_mul(self):
       res = square.area(0)
       self.assertEqual(res, 0)

    def test_negative_on_negative_mul(self):
       res = square.area(-10)
       self.assertEqual(res, 100)

    def test_double_mul(self):
       res = square.area(1.5)
       self.assertEqual(res, 2.25)




    def test_zero_perimeter(self):
       res = square.perimeter(0)
       self.assertEqual(res, 0)
       

    def test_negative_on_negative_perimeter(self):
       res = square.perimeter(-10)
       self.assertEqual(res, -40)

    def test_float_perimeter(self):
       res = square.perimeter(1.5)
       self.assertEqual(res, 6)

class TriangleTestCase(unittest.TestCase):



    def test_zero_mul(self):
       res = triangle.area(10, 0)
       self.assertEqual(res, 0)

    def test_negative_on_positive_mul(self):
       res = triangle.area(10, -20)
       self.assertEqual(res, -100)

    def test_negative_on_negative_mul(self):
       res = triangle.area(-10, -20)
       self.assertEqual(res, 100)

    def test_double_mul(self):
       res = triangle.area(1.5, 1.5)
       self.assertEqual(res, 1.125)




    def test_zero_perimeter(self):
       res = triangle.perimeter(10, 0, 10)
       self.assertEqual(res, 20)

    def test_square_perimeter(self):
       res = triangle.perimeter(10, 10, 10)
       self.assertEqual(res, 30)

    def test_negative_on_positive_perimeter(self):
       res = triangle.perimeter(10, -10, 10)
       self.assertEqual(res, 10)

    def test_negative_on_negative_perimeter(self):
       res = triangle.perimeter(-10, -10, -10)
       self.assertEqual(res, -30)

    def test_float_perimeter(self):
       res = triangle.perimeter(1.5, 1.5, 1.5)
       self.assertEqual(res, 4.5)
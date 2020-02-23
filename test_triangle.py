""" This is testing the triangle code"""
import unittest
from triangle import classify_triangle

class TestTriangles(unittest.TestCase):
    """ define multiple sets of tests as functions with names that begin"""

    def test_right_riangle_a(self):
        """ Testing a type of traingle"""
        self.assertEqual(classify_triangle(3, 4, 5), 'Right')

    def test_right_triangle_b(self):
        """ Testing a type of traingle"""
        self.assertNotEqual(classify_triangle(5, 3, 4), 'Right')

    def test_equilateral_triangles(self):
        """ Testing a type of traingle"""
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral')

    def test_equilateral_triangles_b(self):
        """ Testing a type of traingle"""
        self.assertNotEqual(classify_triangle(3, 1, 1), 'Equilateral')

    def test_scalene_triangles(self):
        """ Testing a type of traingle"""
        self.assertNotEqual(classify_triangle(10, 15, 30), "Scalene")

    def test_scalene_triangles_b(self):
        """ Testing a type of traingle"""
        self.assertNotEqual(classify_triangle(1, 1, 1), "Scalene")

    def test_isosceles_triangles_u(self):
        """ Testing a type of traingle"""
        self.assertNotEqual(classify_triangle(10, 4, 4), "Isosceles")

    def test_isosceles_triangles_o(self):
        """ Testing a type of traingle"""
        self.assertEqual(classify_triangle(5, 5, 4), "Isosceles")

    def test_isosceles_triangles_i(self):
        """ Testing a type of traingle"""
        self.assertEqual(classify_triangle(5, 4, 5), "Isosceles")

    def test_isosceles_triangles_l(self):
        """ Testing a type of traingle"""
        self.assertEqual(classify_triangle(5, 4, 4), "Isosceles")

    def test_isosceles_triangles_b(self):
        """ Testing a type of traingle"""
        self.assertNotEqual(classify_triangle(10, 15, 30), "Isosceles")

    def test_valid_input(self):
        """ Testing a type of traingle"""
        self.assertEqual(classify_triangle(200, 200, 200), "InvalidInput")
        self.assertEqual(classify_triangle(200, 50, 50), "InvalidInput")
        self.assertEqual(classify_triangle(50, 200, 28), "InvalidInput")

    def test_validinput_b(self):
        """ Testing a type of traingle"""
        self.assertNotEqual(classify_triangle(3, 4, 5), "InvalidInput")
        self.assertNotEqual(classify_triangle(10, 15, 30), "InvalidInput")
        self.assertNotEqual(classify_triangle(1, 1, 1), "InvalidInput")

    def test_not_a_triangle(self):
        """ Testing a type of traingle"""
        self.assertNotEqual(classify_triangle(0, 4, 5), "NotATriangle")
        self.assertNotEqual(classify_triangle(3, 4, 5), "NotATriangle")
        self.assertNotEqual(classify_triangle(1, 1, 1), "NotATriangle")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

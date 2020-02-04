# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle because 9+16 =25')

    def testRightTriangleB(self): 
        self.assertNotEqual(classifyTriangle(5,3,4),'Right','5,3,4 is not a right triangle because 25 + 9 != 16')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral because 1=1=1')

    def testEquilateralTrianglesB(self): 
        self.assertNotEqual(classifyTriangle(3,1,1),'Equilateral')
    
    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(10,15,30) , "Scalene")
    
    def testScaleneTrianglesB(self):
        self.assertNotEqual(classifyTriangle(1,1,1) , "Scalene")

    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(10,4,4) , "Isosceles")
    
    def testIsoscelesTrianglesB(self):
        self.assertNotEqual(classifyTriangle(10,15,30) , "Isosceles")
    
    def testValidinput(self):
        self.assertEqual(classifyTriangle(200,200,200) , "InvalidInput")
        self.assertEqual(classifyTriangle(200,50,50) , "InvalidInput")
        self.assertEqual(classifyTriangle(50,200,28) , "InvalidInput")
    def testValidinputB(self):
        self.assertNotEqual(classifyTriangle(3,4,5) , "InvalidInput")
        self.assertNotEqual(classifyTriangle(10,15,30) , "InvalidInput")
        self.assertNotEqual(classifyTriangle(1,1,1) , "InvalidInput")

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(0,4,5) , "NotATriangle")
        self.assertEqual(classifyTriangle(5,-4,5) , "NotATriangle")
        self.assertNotEqual(classifyTriangle(3,4,5) , "NotATriangle")
        self.assertNotEqual(classifyTriangle(1,1,1) , "NotATriangle")
       




       

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()


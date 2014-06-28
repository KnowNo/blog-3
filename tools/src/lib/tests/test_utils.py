import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
import unittest
import math
from utils import *

class Test_module_utils(unittest.TestCase):
    def test_P(self):
        self.assertEqual(P(1, 1), 1)
        self.assertEqual(P(2, 1), 2)
        self.assertEqual(P(2, 2), 2)
        self.assertEqual(P(3, 2), 6)
        self.assertEqual(P(3, 3), 6)
        self.assertEqual(P(5, 2), 20)
        self.assertEqual(P(5, 3), 60)
       
        self.assertEqual(P(2, 0), 1)
        
        self.assertRaises(AssertionError, P, 3, 5)
        
    def test_C(self):
        self.assertEqual(C(1, 1), 1)
        self.assertEqual(C(2, 1), 2)
        self.assertEqual(C(2, 2), 1)
        self.assertEqual(C(3, 2), 3)
        self.assertEqual(C(3, 3), 1)
        self.assertEqual(C(5, 2), 10)
        self.assertEqual(C(5, 3), 10)
        
        self.assertEqual(C(2, 0), 1)
        
        self.assertRaises(AssertionError, P, 3, 5)
        
        for n in xrange(2,100):
            for m in xrange(n):
                self.assertEqual(C(n, m), C(n, n-m))
                
        
        n = 10000
        m = 48
        self.assertEqual(C(n, m), C(n, n-m))
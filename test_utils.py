# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(0), 1)
        self.assertEqual(utils.fact(3), 6)
        with self.assertRaises(NameError):
            utils.fact(bonjour)
    
    def test_roots(self):
        self.assertEqual(utils.roots(1,2,3),("None", "None"))
        self.assertEqual(utils.roots(1 , -5, 4), (4, 1))
        self.assertEqual(utils.roots(1,2,1), (-1, -1))

    def test_integrate(self):
       self.assertEqual(utils.integrate('x ** 2 - 1', -1, 1), -1.3333)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
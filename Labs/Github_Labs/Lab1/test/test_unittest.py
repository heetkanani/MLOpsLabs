import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import calculator


class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(calculator.fun1(2, 3), 5)
        self.assertEqual(calculator.fun1(5, 0), 5)
        
        self.assertEqual(calculator.fun1(-1, 1), 0)
        self.assertEqual(calculator.fun1(-1, -1), -2)

    def test_fun2(self):
        self.assertEqual(calculator.fun2(2, 3), -1)
        self.assertEqual(calculator.fun2(5, 0), 5)
        self.assertEqual(calculator.fun2(-1, 1), -2)
        self.assertEqual(calculator.fun2(-1, -1), 0)

    def test_fun3(self):
        self.assertEqual(calculator.fun3(2, 3), 6)
        self.assertEqual(calculator.fun3(5, 0), 0)
        self.assertEqual(calculator.fun3(-1, 1), -1)
        self.assertEqual(calculator.fun3(-1, -1), 1)

    def test_fun4(self):
        self.assertEqual(calculator.fun4(2, 3, 5), 10)
        self.assertEqual(calculator.fun4(5, 0, -1), 4)
        self.assertEqual(calculator.fun4(-1, -1, -1), -3)
        self.assertEqual(calculator.fun4(-1, -1, 100), 98)

    def test_func5(self):
        self.assertEqual(calculator.func5(10, 2), 5)
        self.assertEqual(calculator.func5(12, 6), 2)
        self.assertEqual(calculator.func5(-10, 2), -5)
        self.assertEqual(calculator.func5(7, 2), 3.5)
        self.assertEqual(calculator.func5(100, 4), 25)
        
        with self.assertRaises(ZeroDivisionError):
            calculator.func5(5, 0)

    def test_func6(self):
        self.assertEqual(calculator.func6(2, 3), 8)
        self.assertEqual(calculator.func6(5, 2), 25)
        self.assertEqual(calculator.func6(3, 0), 1)
        self.assertEqual(calculator.func6(2, -1), 0.5)
        self.assertEqual(calculator.func6(4, 0.5), 2.0)
        self.assertEqual(calculator.func6(10, 2), 100)

    def test_func7(self):
        self.assertEqual(calculator.func7(2, 4, 6), 4.0)
        self.assertEqual(calculator.func7(10, 20, 30, 40), 25.0)
        self.assertEqual(calculator.func7(2, 8, 16, 32), 14.5)
        self.assertEqual(calculator.func7(5), 5.0)
        self.assertEqual(calculator.func7(-10, 10), 0.0)
        self.assertEqual(calculator.func7(1, 2, 3, 4, 5), 3.0)

    def test_func8(self):
        self.assertEqual(calculator.func8(10, 3), 1)
        self.assertEqual(calculator.func8(15, 4), 3)
        self.assertEqual(calculator.func8(10, 6), 4)
        self.assertEqual(calculator.func8(7, 7), 0)
        self.assertEqual(calculator.func8(20, 6), 2)
        
        with self.assertRaises(ZeroDivisionError):
            calculator.func8(5, 0)

    def test_func9(self):
        self.assertEqual(calculator.func9(4), 2.0)
        self.assertEqual(calculator.func9(9), 3.0)
        self.assertEqual(calculator.func9(16), 4.0)
        self.assertEqual(calculator.func9(225), 15.0)
        self.assertEqual(calculator.func9(0), 0.0)
        self.assertEqual(calculator.func9(25), 5.0)
        self.assertAlmostEqual(calculator.func9(2), 1.414, places=2)
        
        with self.assertRaises(ValueError):
            calculator.func9(-4)

if __name__ == '__main__':
    unittest.main()
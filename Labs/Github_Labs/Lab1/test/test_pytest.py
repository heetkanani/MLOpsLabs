import pytest
from src import calculator

def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5,0) == 5
    assert calculator.fun1 (-1, 1) == 0
    assert calculator.fun1 (-1, -1) == -2

def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5,0) == 5
    assert calculator.fun2 (-1, 1) == -2
    assert calculator.fun2 (-1, -1) == 0

def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5,0) == 0
    assert calculator.fun3 (-1, 1) == -1
    
    assert calculator.fun3 (-1, -1) == 1

def test_fun4():
    assert calculator.fun4(2, 3, 5) == 10
    assert calculator.fun4(5,0, -1) == 4
    assert calculator.fun4 (-1, -1, -1) == -3
    
    assert calculator.fun4 (-1, -1, 100) == 98
    
def test_func5():
    assert calculator.func5(10, 2) == 5
    assert calculator.func5(12, 6) == 2
    assert calculator.func5(-10, 2) == -5
    assert calculator.func5(7, 2) == 3.5
    assert calculator.func5(100, 4) == 25
    
    with pytest.raises(ZeroDivisionError):
        calculator.func5(5, 0)

def test_func6():
    assert calculator.func6(2, 3) == 8
    assert calculator.func6(5, 2) == 25
    assert calculator.func6(3, 0) == 1
    assert calculator.func6(2, -1) == 0.5
    assert calculator.func6(4, 0.5) == 2.0
    assert calculator.func6(10, 2) == 100

def test_func7():
    assert calculator.func7(2, 4, 6) == 4.0
    assert calculator.func7(10, 20, 30, 40) == 25.0
    assert calculator.func7(2, 8, 16, 32) == 14.5
    assert calculator.func7(5) == 5.0
    assert calculator.func7(-10, 10) == 0.0
    assert calculator.func7(1, 2, 3, 4, 5) == 3.0

def test_func8():
    assert calculator.func8(10, 3) == 1
    assert calculator.func8(15, 4) == 3
    assert calculator.func8(10, 6) == 4
    assert calculator.func8(7, 7) == 0
    assert calculator.func8(20, 6) == 2
    
    with pytest.raises(ZeroDivisionError):
        calculator.func8(5, 0)

def test_func9():
    assert calculator.func9(4) == 2.0
    assert calculator.func9(9) == 3.0
    assert calculator.func9(16) == 4.0
    assert calculator.func9(225) == 15.0
    assert calculator.func9(0) == 0.0
    assert calculator.func9(25) == 5.0
    
    with pytest.raises(ValueError):
        calculator.func9(-4)

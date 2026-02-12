def fun1(x, y):
    """
    Adds two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Sum of x and y.
        Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    
    return x + y

def fun2(x, y):
    """
    Subtracts two numbers.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Difference of x and y.
        Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x - y

def fun3(x, y):
    """
    Multiplies two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Product of x and y.
        Raises:
        ValueError: If either x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x * y

def fun4(x,y,z):
    """
    Adds three numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
        z (int/float): Third number.
    Returns:
        int/float: Sum of x, y and z.
    """
    total_sum = x + y + z
    return total_sum

# Added 5 additional functions 
# Divition function
def func5(x, y):
    """
    Divides x by y.
    Args:
        x (int/float): Numerator.
        y (int/float): Denominator.
    Returns:
        float: Result of x divided by y.
    Raises:
        ValueError: If x or y is not a no.
        ZeroDivisionError: if y oe denominator is zero.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

# power function
def func6(x, y):
    """
    Raises x to the power of y.
    Args:
        x (int/float): Base number.
        y (int/float): Exponent.
    Returns:
        int/float: Result of x raised to the power of y.
    Raises:
        ValueError: If x or y is not a no.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x ** y
    
# Average function
def func7(*args):
    """
    Calculates the average of multiple numbers.
    Args:
        *args: Variable number of numeric arguments.
    Returns:
        float: Average of all input numbers.
    Raises:
        ValueError: If no arguments are provided or if any argument is not a number.
    """
    if len(args) == 0:
        raise ValueError("At least one number is required.")
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise ValueError("All inputs must be numbers.")
    return sum(args) / len(args)

# Modulo Function
def func8(x, y):
    """
    Returns the remainder when x is divided by y.
    Args:
        x (int/float): Dividend.
        y (int/float): Divisor.
    Returns:
        int/float: Remainder of x divided by y.
    Raises:
        ValueError: If x or y is not a number.
        ZeroDivisionError: If y oe denominator is zero.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    if y == 0:
        raise ZeroDivisionError("Cannot perform modulo with zero.")
    return x % y

# Square Root function
def func9(x):
    """
    Returns the square root of x.
    Args:
        x (int/float): Number to find square root of.
    Returns:
        float: Square root of x.
    Raises:
        ValueError: If x is not a no. or is negative.
    """
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a number.")
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return x ** 0.5


# if __name__ == "__main__":
#     f1_op = fun1(2, 3)
#     f2_op = fun2(2, 3)
#     f3_op = fun3(2, 3)
#     f4_op = fun4(f1_op, f2_op, f3_op)
    
#     f5_op = func5(12, 6)
#     f6_op = func6(2, 3)
#     f7_op = func7(2, 8, 16, 32)
#     f8_op = func8(10, 6)
#     f9_op = func9(225)
    
#     print(f"fun1(2, 3) = {f1_op}")
#     print(f"fun2(2, 3) = {f2_op}")
#     print(f"fun3(2, 3) = {f3_op}")
#     print(f"fun4({f1_op}, {f2_op}, {f3_op}) = {f4_op}")
#     print(f"func5(12, 6) = {f5_op}")
#     print(f"func6(2, 3) = {f6_op}")
#     print(f"func7(2, 8, 16, 32) = {f7_op}")
#     print(f"func8(10, 6) = {f8_op}")
#     print(f"func9(225) = {f9_op}")

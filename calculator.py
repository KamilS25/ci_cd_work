"""
Calculator module

Contains basic mathematical operations used by the calculator application
"""


def add(a, b):
    """
    Return the sum of two numbers

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b
    """
    return a + b


def subtract(a, b):
    """
    Return the difference between two numbers

    Args:
        a: First number
        b: Second number

    Returns:
        Difference between a and b
    """
    return a - b


def multiply(a, b):
    """
    Return the product of two numbers

    Args:
        a: First number
        b: Second number

    Returns:
        Product of a and b
    """
    return a * b


def divide(a, b):
    """
    Divide the first number by the second

    Args:
        a: Dividend
        b: Divisor

    Returns:
        Result of dividing a by b

    Raises:
        ValueError: If b is equal to zero
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")

    return a / b

def power(a, b):
    """
    Raise a number to the specified power.

    Args:
        a: Base number.
        b: Exponent.

    Returns:
        Result of raising a to the power of b.
    """
    return a ** b

def reminder_del(a, b):
    """
    Return the result of reminder of the division
    Args:
        a: Base number.
        b: Exponent.

    Returns:
        Result of reminder of the division.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")

    return a % b
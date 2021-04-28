"""Functions for common math operations."""



def add(num1, num2):
    """Return the sum of the two inputs."""
    return num1 + num2


def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    return num1-num2


def multiply(num1, num2):
    """Multiply the two inputs together."""
    return num1*num2


def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    answer = "%.1f" %(num1/num2)
    return answer


def square(num1):
    """Return the square of the input."""
    answer = "%.1f" %(num1**2)
    return answer


def cube(num1):
    """Return the cube of the input."""
    answer = "%.1f" %(num1**3)
    return answer


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    answer = "%.1f" %(num1**num2)
    return answer


def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    answer = "%.1f" %(num1%num2)
    return answer

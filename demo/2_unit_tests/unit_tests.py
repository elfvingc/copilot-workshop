def is_even(number: int) -> bool:
    """
    Check if a number is even.

    :param number: The number to check.
    :return: True if the number is even, False otherwise.
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    return number % 2 == 0

def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    :param n: A non-negative integer.
    :return: The factorial of the given number.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def reverse_string(s: str) -> str:
    """
    Reverse a given string.

    :param s: The string to reverse.
    :return: The reversed string.
    """
    return s[::-1]

def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome.

    :param s: The string to check.
    :return: True if the string is a palindrome, False otherwise.
    """
    clean_s = ''.join(filter(str.isalnum, s)).lower()
    return clean_s == clean_s[::-1]

def max_of_three(a: int, b: int, c: int) -> int:
    """
    Find the maximum of three numbers.

    :param a: The first number.
    :param b: The second number.
    :param c: The third number.
    :return: The maximum of the three numbers.
    """
    return max(a, b, c)

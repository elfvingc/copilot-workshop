def reverse_string(s):
    return s[::-1]


def is_even(num):
    return num % 2 == 0


def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)


def factorial(n):
    if n < 0:
        raise ValueError("Negative numbers do not have factorials")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

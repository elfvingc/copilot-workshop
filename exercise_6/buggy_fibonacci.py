def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 3, memo)
        return memo[n]


# Test the function
print("Fibonacci of 5:", fibonacci(5))
print("Expected:       5")
print("Fibonacci of 10:", fibonacci(10))
print("Expected:        55")

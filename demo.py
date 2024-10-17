import random


def calculate_mean(numbers):
    total = 0
    n = len(numbers)

    for i in range(n + 1):
        total += numbers[i]

    mean = total / n
    return mean


if __name__ == "__main__":
    count = 10
    lower_bound = 1
    upper_bound = 100

    # Step 1: Generate random numbers
    random_numbers = [random.randint(lower_bound, upper_bound) for _ in range(count)]
    print(f"Random Numbers: {random_numbers}")

    # Step 2: Sort the numbers
    sorted_numbers = sorted(random_numbers)
    print(f"Sorted Numbers: {sorted_numbers}")
    # Step 3: Find the median
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]
    print(f"Median: {median}")
    # Step 4: Find the mean
    mean = calculate_mean(random_numbers)
    print(f"Mean: {mean}")

    # Step 5: Find the standard deviation

# Process a list of numbers and generate various statistics
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_numbers = 0
count = 0
minimum = float("inf")
maximum = float("-inf")

for num in numbers:
    sum_numbers += num
    count += 1
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

mean = sum_numbers / count
variance = sum((num - mean) ** 2 for num in numbers) / count
standard_deviation = variance**0.5

print(f"Sum: {sum_numbers}")
print(f"Count: {count}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {standard_deviation}")

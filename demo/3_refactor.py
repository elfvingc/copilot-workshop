from typing import List

def process_data(data: List[int]) -> List[float]:
    """
    Process a list of integers: filter out odd numbers, 
    calculate their squares, and then compute their square roots.

    :param data: A list of integers.
    :return: A list of square roots of the squares of even numbers.
    """
    # Step 1: Filter out odd numbers
    even_numbers = []
    for number in data:
        if number % 2 == 0:
            even_numbers.append(number)
    
    # Step 2: Calculate the square of each even number
    squared_numbers = []
    for number in even_numbers:
        squared_numbers.append(number ** 2)
    
    # Step 3: Calculate the square root of each squared number
    results = []
    for number in squared_numbers:
        results.append(number ** 0.5)
    
    return results

# Example usage
if __name__ == "__main__":
    sample_data = [1, 2, 3, 4, 5, 6]
    print(process_data(sample_data))

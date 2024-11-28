from typing import List, Union

def add_numbers(*args: Union[int, float]) -> Union[int, float]:
    if not args:
        raise ValueError("At least one number must be provided.")
    return sum(args)

def greet(name: str, time_of_day: str = "day") -> str:
    greetings = {
        "morning": "Good morning",
        "afternoon": "Good afternoon",
        "evening": "Good evening",
        "night": "Good night",
        "day": "Hello"
    }
    
    greeting = greetings.get(time_of_day, "Hello")
    return f"{greeting}, {name}! Welcome to the demo!"

class AdvancedCalculator:
    
    def __init__(self):
        pass

    def multiply_numbers(self, *args: Union[int, float]) -> Union[int, float]:
        if not args:
            raise ValueError("At least one number must be provided.")
        result = 1
        for number in args:
            result *= number
        return result

    def divide_numbers(self, a: Union[int, float], b: Union[int, float]) -> float:
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b

    def calculate_mean(self, numbers: List[Union[int, float]]) -> float:
        if not numbers:
            raise ValueError("The list of numbers cannot be empty.")
        return sum(numbers) / len(numbers)

# Example usage
if __name__ == "__main__":
    print(add_numbers(10, 5, 3.5))
    print(greet("Alice", "afternoon"))
    
    calc = AdvancedCalculator()
    print(calc.multiply_numbers(2, 3, 4))
    print(calc.divide_numbers(10, 2))
    print(calc.calculate_mean([1, 2, 3, 4, 5]))

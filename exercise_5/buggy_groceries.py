class GroceryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def apply_discount(self, percentage):
        self.price -= self.price * percentage / 100


def find_most_expensive_items(grocery_list):
    most_expensive = grocery_list[0]
    for item in grocery_list:
        if item.price > most_expensive.price:
            most_expensive = item
    return most_expensive


if __name__ == "__main__":
    # Test 1: Empty List Bug
    grocery_list = []
    most_expensive_items = find_most_expensive_items(grocery_list)
    assert (
        most_expensive_items == []
    ), "The list should be empty for an empty grocery list"

    # Test 2: Multiple Items with Same Price Bug
    grocery_list = [
        GroceryItem("Apples", 4.50, 10),
        GroceryItem("Bananas", 4.50, 5),
        GroceryItem("Cherries", 3.00, 2),
        GroceryItem("Dates", 4.50, 7),
    ]
    most_expensive_items = find_most_expensive_items(grocery_list)
    assert len(most_expensive_items) == 3, "There should be three most expensive items"
    assert all(
        item.price == 4.50 for item in most_expensive_items
    ), "All most expensive items should have a price of 4.50"

    # Test 3: Negative Price Bug
    try:
        grocery_list = [
            GroceryItem("Apples", -3.50, 10),
            GroceryItem("Bananas", 2.00, 5),
            GroceryItem("Cherries", 5.00, 2),
            GroceryItem("Dates", 4.50, 7),
        ]
        assert False, "Expected ValueError for negative price"
    except ValueError as e:
        assert (
            str(e) == "Price cannot be negative"
        ), "Unexpected error message for negative price"

    # Test 4: Incorrect Discount Application Bug
    grocery_list = [
        GroceryItem("Apples", 3.50, 10),
        GroceryItem("Bananas", 2.00, 5),
        GroceryItem("Cherries", 5.00, 2),
        GroceryItem("Dates", 4.50, 7),
    ]

    # Incorrectly applying a discount of 110%
    try:
        for item in grocery_list:
            item.apply_discount(110)
        assert False, "Expected ValueError for discount greater than 100"

    except ValueError as e:
        assert (
            str(e) == "Discount percentage cannot be greater than 100"
        ), "Unexpected error message"

    print("All tests passed!")

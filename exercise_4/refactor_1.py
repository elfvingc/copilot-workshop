# This script calculates the area of different shapes
shape = input(
    "Enter the shape to calculate area (circle, square, rectangle, triangle): "
)

if shape == "circle":
    radius = float(input("Enter the radius: "))
    area = 3.14 * (radius**2)
    print(f"The area of the circle is {area}")
elif shape == "square":
    side = float(input("Enter the side length: "))
    area = side**2
    print(f"The area of the square is {area}")
elif shape == "rectangle":
    length = float(input("Enter the length: "))
    breadth = float(input("Enter the breadth: "))
    area = length * breadth
    print(f"The area of the rectangle is {area}")
elif shape == "triangle":
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is {area}")
else:
    print("Invalid shape")

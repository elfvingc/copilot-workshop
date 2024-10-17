# Collect user information and print it
name = input("Enter your name: ")
age = int(input("Enter your age: "))
email = input("Enter your email: ")

if "@" not in email:
    print("Invalid email address")
else:
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")

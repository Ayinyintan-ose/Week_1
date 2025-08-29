import math

print("Welcome to your mini calculator.")
def add(numbers):
    addition = sum(numbers)
    return f"The sum of the numbers is {addition}"

def subtract(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result -= number
    return f"The answer is {result}"


def divide(x, y):
    result = x/y
    return f"When you divide {x} and {y} you get: {result}"


def power(x, y):
    result = math.pow(x, y)
    return f"{x} raised to the power of {y} is: {result}"

def root(number):
    result = math.sqrt(number)
    return f"The root of {number} is: {result}"

def multiply(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result *= number
    return f"When you multiply the numbers you get: {result}"

while True:
    # The list of operations that the user can perform
    print("Below are the available operations;")
    operation = ["addition", "subtraction", "division", "power", "square root", "multiplication", "quit"]
    for index, operation in enumerate(operation):
        print(f"{index + 1}. {operation}")
    user_operation = input("Enter the arithmetic operation you want to perform: ")

    # Add the user input
    if user_operation == "1":
        num = list(map(float, input("Enter the numbers you want to add with + sign between each number: ").split("+")))
        print(add(num))

    # Subtract the user input
    elif user_operation == "2":
        num = list(map(float, input("Enter the numbers you want to add with - sign between each number: ").split("-")))
        print(subtract(num))

    elif user_operation == "3":
        num1 = int(input("Enter the numerator: "))
        num2 = int(input("Enter the denominator: "))
        print(divide(num1, num2))

    elif user_operation == "4":
        num1 = int(input("Enter the number: "))
        num2 = int(input("Enter the power: "))
        print(power(num1, num2))

    elif user_operation == "5":
        num = int(input("Enter the number you want to get the root for: "))
        print(root(num))

    elif user_operation == "6":
        num = list(map(float, input("Enter the numbers you want to add with * sign between each number: ").split("*")))
        print(multiply(num))

    elif user_operation == "7":
        break

    else:
        print("That is not an option, kindly enter an available operation.")
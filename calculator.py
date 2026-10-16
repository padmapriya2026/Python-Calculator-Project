
import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def percentage(a, b):
    return (a / 100) * b


def square(a):
    return a * a


def square_root(a):
    if a < 0:
        return "Error: Negative numbers are not supported."
    return math.sqrt(a)


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    while True:
        print("\n===== PYTHON CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Percentage")
        print("6. Square")
        print("7. Square Root")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "8":
            print("Thank you for using the calculator!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Invalid choice. Please select 1 to 8.")
            continue

        if choice == "6" or choice == "7":
            number = get_number("Enter a number: ")

            if choice == "6":
                result = square(number)
            else:
                result = square_root(number)
        else:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == "1":
                result = add(num1, num2)
            elif choice == "2":
                result = subtract(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            elif choice == "4":
                result = divide(num1, num2)
            else:
                result = percentage(num1, num2)

        print("Result:", result)


if __name__ == "__main__":
    main()


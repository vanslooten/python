# Fixed code that will crash if the user enters something different than a number
# Try to enter text. Or a floating point number like 2.5, or 0.

input = input("Enter a number to divide 10 by: ")

try:
    # convert the text to a number
    x = int(input)
    # This line will result in an error if the user entered 0
    result = 10 / x

    print(f"The result is: {result}")
except ValueError:
    print("Oops! That was no valid number.")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")


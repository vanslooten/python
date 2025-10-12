# https://docs.python.org/3/tutorial/errors.html

while True:
    try:
        x = float(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")

# This line will result in an error if the user entered 0
result = 10 / x

print(f"The result is: {result}") 

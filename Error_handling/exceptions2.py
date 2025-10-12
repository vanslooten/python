while True:
    # Code that handles potential errors
    try:
        input_str = input("Enter a number to divide 10 by: ")
        
        # 1. Attempt to convert the input to an integer
        x = int(input_str)
        
        # 2. Attempt the division (which would crash if x is 0)
        result = 10 / x
        
        print(f"The result is: {result}")

        break
        
    # This block runs only if a ValueError occurs in the 'try' block
    except ValueError:
        print("Error: You must enter a valid whole number (integer). Please try again.")

    # This block runs only if a ZeroDivisionError occurs in the 'try' block
    except ZeroDivisionError:
        print("Error: You cannot divide by zero. Enter a non-zero number.")

# This code simulates rolling a dice by generating a random number between 1 and 6.
# The random.randint function is used to generate the number, and the result is printed to the console.
# https://www.w3schools.com/programming/prog_loops.php

import random
import os

print("roll a dice")

#random.seed()  # Initialize the random number generator
random.seed(int.from_bytes(os.urandom(8), 'big'))  # Seed with 64 bits from OS entropy

dice_numbers = ("one", "two", "three", "four", "five", "six") # tuple of dice faces; list could also be used, like dice_numbers = ["one", "two", "three", "four", "five", "six"]

def roll_dice():    
    # Generate a random number between 1 and 6
    return random.randint(1, 6)

# Call the function and print the result
if __name__ == "__main__":
    result = roll_dice()
    print(f"You rolled a {dice_numbers[result - 1]}")
    print("Thanks for playing!")


# Small example to sort a list of numbers (Bubble sort algorithm).
# This is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.
# The algorithm gets its name from the way larger elements "bubble" to the top of the list.

import random  # Import the random module to generate random numbers

# Declare a list of random numbers to be sorted in one line:
numbers = [random.randint(1, 100) for _ in range(7)]  # Generate a list of 7 random integers between 1 and 100

print(numbers)  # Print the list before the sorting process

i = 0                                                            # Start index at 0
while i < len(numbers) - 1:                                      # Loop until the second-to-last element
    if numbers[i] > numbers[i + 1]:                              # Compare current element with the next
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]  # Swap if out of order
        i = 0                                                    # Restart from the beginning after a swap
    else:
        i = i + 1                                                # Move to the next pair if no swap

print("Sorted numbers:")
print(numbers)  # Print the sorted list

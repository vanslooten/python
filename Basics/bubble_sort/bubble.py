# Bubble Sort Implementation
# This code sorts the list of numbers in ascending order using the bubble sort algorithm.

numbers = [6, 3, 8, 6, 2, 1]  # Example list of numbers

print("Original numbers:", numbers)  # Output the original list

i = 0                                                            # Start index at 0
while i < len(numbers) - 1:                                      # Loop until the second-to-last element
    if numbers[i] > numbers[i + 1]:                              # Compare current element with the next
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]  # Swap if out of order
        i = 0                                                    # Restart from the beginning after a swap
    else:
        i = i + 1                                                # Move to the next pair if no swap

print("Sorted numbers:", numbers)  # Output the sorted list

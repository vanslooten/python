# v2; The sorting process is now visualized in real-time using matplotlib.
# declare a list of random numbers, length 20
import random
import time 
import matplotlib.pyplot as plt

numbers = [random.randint(1, 100) for _ in range(20)]

# print the list
print("Original numbers:", numbers)

# now visualize the sorting process while it is happening
def visualize_sorting(numbers):
    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots()
    
    n = len(numbers)
    for passnum in range(n - 1, 0, -1):
        for i in range(passnum):
            if numbers[i] > numbers[i + 1]:
                # Swap the elements
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

            # Clear the plot and redraw
            ax.clear()
            ax.bar(range(len(numbers)), numbers, color='blue')
            ax.set_title('Bubble Sort Visualization')
            ax.set_xlabel('Index')
            ax.set_ylabel('Value')
            plt.pause(0.1)  # Pause to visualize the sorting step

    plt.ioff()  # Turn off interactive mode
    plt.show()

visualize_sorting(numbers)
# Note: The visualization will show the sorting process in real-time.

# print the sorted list
print("Sorted numbers:", numbers)

# This code generates a list of 100 random ages between 1 and 100, then prints some statistics about the ages.

# declare a list of 100 random numbers representing the ages of 100 people
import random
import os

random.seed(int.from_bytes(os.urandom(8), 'big'))  # Seed with 64 bits from OS entropy

#ages = [random.randint(1, 100) for _ in range(100)]
# Generate ages with a more realistic distribution: 
# Most people are adults, fewer are children or elderly.
ages = []
for _ in range(100):
    r = random.random()
    if r < 0.2:
        # 20% children (1-17)
        ages.append(random.randint(1, 17))
    elif r < 0.8:
        # 60% adults (18-65)
        ages.append(random.randint(18, 65))
    else:
        # 20% seniors (66-100)
        ages.append(random.randint(66, 100))

# print the ages of the people
#for age in ages:
#    print(age)  

# print the average age of the people
average_age = sum(ages) / len(ages) 
print(f"The average age is {average_age:.2f} years.")

# print the number of people older than 50
older_than_50 = sum(1 for age in ages if age > 50)
print(f"There are {older_than_50} people older than 50 years.")

# print the number of people younger than 18
younger_than_18 = sum(1 for age in ages if age < 18)
print(f"There are {younger_than_18} people younger than 18 years.")

# print the youngest and oldest ages
youngest_age = min(ages)
oldest_age = max(ages)
print(f"The youngest age is {youngest_age} years.")
print(f"The oldest age is {oldest_age} years.")

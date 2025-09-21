# open a CSV dataset using pandas
# perform basic data exploration
import pandas as pd
import matplotlib.pyplot as plt

# dataset source https://www.kaggle.com/datasets/burnoutminer/heights-and-weights-dataset/data
# read csv file that contains a dataset
df = pd.read_csv('SOCR-HeightWeight.csv')

# create a scatter plot of the data: Height vs Weight
plt.scatter(df['Height(Inches)'], df['Weight(Pounds)'], alpha=0.5)
plt.title('Height vs Weight')   
plt.xlabel('Height (Inches)')
plt.ylabel('Weight (Pounds)')

# show the plot
plt.show()


# plot Height distribution as a histogram
plt.hist(df['Height(Inches)'], bins=30, alpha=0.7, color='blue')
plt.title('Height Distribution')    
plt.xlabel('Height (Inches)')
plt.ylabel('Frequency')

# show the plot
plt.show()

"""
plot parameters explained:
alpha:
    Transparency of dots (between 0 and 1). 1 is fully opaque, 0 is fully transparent.
bins:
    When you create a histogram, pandas takes your numerical data and divides the entire range of values into a series of non-overlapping intervals,
    which are the bins. It then counts how many data points fall into each bin.
    The height of each bar in the histogram corresponds to the count (or frequency) of values within that specific bin.
"""

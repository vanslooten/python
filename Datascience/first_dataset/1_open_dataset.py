# open a CSV dataset using pandas
# perform basic data exploration
import pandas as pd

# dataset source https://www.kaggle.com/datasets/burnoutminer/heights-and-weights-dataset/data
# read csv file that contains a dataset
df = pd.read_csv('SOCR-HeightWeight.csv')

# what is the type of df?
print(type(df))

# what are the columns and
# what do the first few rows look like?
print(df.head())

def convert_to_cm(height_inches):
    """
    Convert height from inches to centimeters.
    Parameter:
        height_inches (float): Height in inches.
    Returns:
        float: Height in centimeters.
    """
    return height_inches * 2.54 

# lets investigate some information about the Height
print("Max:", convert_to_cm(df['Height(Inches)'].max()) )
print("Min:", convert_to_cm(df['Height(Inches)'].min()) )
print("Mean:", convert_to_cm(df['Height(Inches)'].mean()) )
print("Median:", convert_to_cm(df['Height(Inches)'].median()) )
print("Std Dev:", convert_to_cm(df['Height(Inches)'].std()) )
print("Variance:", convert_to_cm(df['Height(Inches)'].var()) )

# or use describe() on the Height column:
print(df['Height(Inches)'].describe())

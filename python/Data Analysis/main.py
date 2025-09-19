'''
Perform following operations on a CSV file 
a. Create a data frame from csv file, dictionary, List of tuples 
b. Operations on Data Frame Shape, head, tail 
c. Retrieving rows / columns from data frame 
d. Finding maximum and minimum values 
e. Displaying statistical information 
f. Performing queries 
g. Data Analysis using groupby()

'''


'''
a. Create a data frame from csv file, dictionary, List of tuples 
'''

import pandas as pd
import numpy as np

# Create a DataFrame from a CSV file
df = pd.read_csv('data.csv')
print(df.head())

# Create a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)


# Create a DataFrame from a list of tuples
data = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
df = pd.DataFrame(data, columns=['Name', 'Age'])

'''
b. Operations on Data Frame Shape, head, tail 
'''
print("Operations on Data Frame Shape, head, tail")

print(df.shape)  # (3, 2)
print(df.head())  # First 5 rows
print(df.tail())  # Last 5 rows


'''
c. Retrieving rows / columns from data frame 
'''

print("Retrieving rows / columns from data frame")

print(df['Name'])  # Retrieve a column
print(df[['Name', 'Age']])  # Retrieve multiple columns
print(df.iloc[0])  # Retrieve a row by index
print(df.loc[0])  # Retrieve a row by label

'''
d. Finding maximum and minimum values'
'''

print("Finding maximum and minimum values")

print(df['Age'].max())  # Maximum value in 'Age' column
print(df['Age'].min())  # Minimum value in 'Age' column

'''
e. Displaying statistical information 
'''

print("Displaying statistical information")

print(df.describe())  # Descriptive statistics

'''
f. Performing queries 
'''

print("Performing queries")

print(df[df['Age'] > 30])  # Rows where 'Age' is greater than 30
print(df[(df['Age'] > 25) & (df['Age'] < 35)])  # Rows where 'Age' is between 25 and 35

'''
g. Data Analysis using groupby()
'''

print("Data Analysis using groupby()")

grouped = df.groupby('Name')
print(grouped['Age'].mean())  # Average 'Age' by 'Name'
print(grouped['Age'].agg(['min', 'max']))  # Minimum and maximum 'Age' by 'Name'

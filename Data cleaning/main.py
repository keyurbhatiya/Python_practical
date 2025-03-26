# Handling dirty data / missing data 

import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')
print(df.head()) # no missing data
print(df.isnull().sum()) # no missing data

df['Age'].fillna(df['Age'].mean(), inplace=True) # replacing with mean
print(df.isnull().sum())

df['Age'].fillna(df['Age'].median(), inplace=True) # replacing with median
print(df.isnull().sum())

df['Age'].fillna(df['Age'].mode()[0], inplace=True) # replacing with mode
print(df.isnull().sum())

df['Age'].fillna(method='ffill', inplace=True) # replacing with forward fill
print(df.isnull().sum()) # no change

df['Age'].fillna(method='bfill', inplace=True) # replacing with backward fill

print(df.isnull().sum()) # no change
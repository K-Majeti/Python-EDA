import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/K Majeti/Desktop/Projects Data/Car Data/Automobile.csv")

data.head()

data.columns

data.info()

data.describe()

data.isna().sum()

data.dropna(inplace=True)

data.drop_duplicates(inplace=True)

data.isna().sum().sum()

data.head()

data.shape

data.to_csv("C:/Users/K Majeti/Desktop/Projects Data/Car Data/Automobile_cleaned.csv")
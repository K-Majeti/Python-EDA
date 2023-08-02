import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/K Majeti/Desktop/Projects Data/Data Science salaries Data/Latest_Data_Science_Salaries.csv")

df.head()

df.describe()

df.shape

df.info()

df.isnull().sum().sum()

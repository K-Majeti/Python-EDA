import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt #data visualizzation and charting
import missingno as msno #to visualize the missing values


#Loading the dataset
df = pd.read_csv("C:/Users/K Majeti/Desktop/Projects Data/Loan Defaulter Data/application_data.csv")
df.head()

#Understanding the dataset
df.info() 
df.describe()

#Visualizing the missing data of all columns in the dataset

# Dataset Cleaning

df.isnull().sum()
df_cleaned = df.dropna()
df_cleaned = df.dropna(axis=1)


df_cleaned.head(100)


## Rechecking the Data

df_cleaned.columns, df_cleaned.shape

df_cleaned.describe()

df_cleaned.isnull().sum()   


#Removing irrelevant columns
drop_cols = ['FLAG_DOCUMENT_2','FLAG_DOCUMENT_3', 'FLAG_DOCUMENT_4', 'FLAG_DOCUMENT_5',
             'FLAG_DOCUMENT_6', 'FLAG_DOCUMENT_7', 'FLAG_DOCUMENT_8','FLAG_DOCUMENT_9', 
             'FLAG_DOCUMENT_10', 'FLAG_DOCUMENT_11','FLAG_DOCUMENT_12', 'FLAG_DOCUMENT_13',
             'FLAG_DOCUMENT_14','FLAG_DOCUMENT_15', 'FLAG_DOCUMENT_16', 'FLAG_DOCUMENT_17',
             'FLAG_DOCUMENT_18', 'FLAG_DOCUMENT_19', 'FLAG_DOCUMENT_20','FLAG_DOCUMENT_21']

df_cleaned = df_cleaned.drop(columns=drop_cols)

df_cleaned.columns
df_cleaned.head(20)

## Exporting the cleaned data sets

df_cleaned.to_csv("C:/Users/K Majeti/Desktop/Projects Data/Loan Defaulter Data/application_data_cleaned.csv")
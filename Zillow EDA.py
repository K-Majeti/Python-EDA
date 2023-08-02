import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer

df = pd.read_csv("C:/Users/K Majeti/Desktop/Projects Data/Zillow Housing Data/Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_month.csv")

df.head()

df.isnull().sum()

df_melted = pd.melt(df, id_vars=["RegionID","SizeRank",	"RegionName","RegionType",	"StateName"], var_name="date_time", value_name="sale_price")

df_melted.head(10)

df.isnull().sum().sum()

imputer = KNNImputer(n_neighbors=4)

df_imputed = pd.DataFrame(imputer.fit_transform(df_melted), columns=df_melted.columns)

df_miss = df.isnull().sum()
df_miss.value_counts()

df_melted.dropna()


df_melted.to_csv("C:/Users/K Majeti/Desktop/Projects Data/Zillow Housing Data/Zillow Cleaned.csv")










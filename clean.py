import pandas as pd

# Loading the dataset
df = pd.read_csv('game_info.csv')

# Displaying the first few rows of the dataset
print(df.head())

# Checking the shape of the dataset
print("The shape of the dataset is - ", df.shape)

# Understanding the dataset
print(df.info())
print(df.describe())

# Looking for missing values 
print(df.isnull().sum())

# Looking for the data type of every missing value column
data_type = df.loc[:, df.isna().any()].dtypes
print(data_type)

# Inspecting
inspecting = df["metacritic"].describe()
print(inspecting)

# checking for duplicates
duplicates = df.duplicated().sum()
print("The duplicates values are - ", duplicates)

# Cleaning the dataset 
metacritic_info = df["metacritic"].isnull().sum()
print("The missing values in metacritic column are - ", metacritic_info)

drop = df.drop(columns=["metacritic","website","publishers","esrb_rating"], inplace=True)
print(drop)

# checking the values again 
print(df.isnull().sum())

# cleaning released column
print(df["released"].head())

df["released"] = pd.to_datetime(df["released"], errors='coerce')
print(df["released"])

print(df["released"].dtype)

# cleaning the platforms column
print(df["platforms"].isnull().sum())
print(df["platforms"].value_counts(dropna=False).head(20))

df["platforms"] = df["platforms"].fillna("Unknown")
print(df["platforms"])

print(df["platforms"].isnull().sum())

# cleaning the genres column
print(df["genres"].isnull().sum())

print(df["genres"].head(20))
df["genres"] = df["genres"].fillna("Unknown")
print(df["genres"].isnull().sum())

print(df.isnull().sum())

# droping some rows with missing values 
df = df.dropna(subset = ["name","slug"])
print(df.isnull().sum())

# cleaning developers 
dev = df["developers"].head(20)
print(dev)

df["developers"] = df["developers"].fillna("Unknown")
print("developers")

print(df["developers"].isnull().sum())

df = df.to_csv("Cleaned Game_info.csv", index=False)
print(df)
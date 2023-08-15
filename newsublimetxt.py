import numpy as np
import pandas as pd

data = pd.read_csv('activity-limitations-total-responses-2018-census-csv.csv', encoding = "utf-8")

print("First 5 samples:")
print("-"*100)
print(data.head())

print("Shape of dataset:", data.shape)
print("-"*100)
print(data.shape)

print("Statistical summary:")
print("-"*100)
print(data.describe())

print("Null values in the dataset:")
print("-"*100)
print(data.isnull().sum())

print("Datatypes:")
print("-"*100)
print(data.dtypes)

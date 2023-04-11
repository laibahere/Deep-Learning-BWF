import pandas as pd
import numpy as np
from numpy import nan as NA

#dropna:labels based on whether values for each label have missing data, with varying thresholds for how much missing data to tolerate.
data = pd.Series([1, NA, 3.5, NA, 7])
print(data.dropna())
#This is equivalent to:
#print(data[data.notnull()])

#With DataFrame objects
data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA], [NA, NA, NA], [NA, 6.5, 3.]])
#print(data)

cleaned = data.dropna()
#print(cleaned)

#Passing how='all' will only drop rows that are all NA:
print(data.dropna(how='all'))

#To drop columns in the same way, pass axis=1:
data[4] = NA
print (data)

print(data.dropna(axis=1, how='all'))

df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA
print(df)
print(df.dropna())
print(df.dropna(thresh=2))


#-----------Filling in Missing Data-------
#Calling fillna with aconstant replaces missing values with that value:
print(df.fillna(0))

#Calling fillna with a dict, you can use a different fill value for each column:
print(df.fillna({1: 0.5, 2: 0}))

df.fillna(0, inplace=True)
print(df)

#reindexing with fillna
df = pd.DataFrame(np.random.randn(6, 3))
df.iloc[2:, 1] = NA
df.iloc[4:, 2] = NA
print(df)
print(df.fillna(method='ffill'))
print(df.fillna(method='ffill', limit=2))

#pass the mean or median value of a Series:
data = pd.Series([1., NA, 3.5, NA, 7])
print( data.fillna(data.mean()))
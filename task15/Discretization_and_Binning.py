import numpy as np 
import pandas as pd

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
print(cats)

print(cats.codes)
print(cats.categories)
print(pd.value_counts(cats))
print(pd.cut(ages, [18, 26, 36, 61, 100], right=False))

group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
print(pd.cut(ages, bins, labels=group_names))

data = np.random.rand(20)
print(pd.cut(data, 4, precision=2))

data = np.random.randn(1000) #Normally distributed
cats = pd.qcut(data, 4) # Cut into quartiles
print(cats)
print(pd.value_counts(cats))
print(pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.]))

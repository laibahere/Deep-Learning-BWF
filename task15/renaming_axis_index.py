import pandas as pd
import numpy as np
data = pd.DataFrame(np.arange(12).reshape((3, 4)), index=['Ohio', 'Colorado', 'New York'],columns=['one', 'two', 'three', 'four'])

#the axis indexes have a map method:
transform = lambda x: x[:4].upper()
print(data.index.map(transform))

#modifying the DataFrame in-place:
data.index = data.index.map(transform)
print(data)

#create a transformed version of a dataset without modifying the origi‐nal, a useful method is rename:
print(data.rename(index=str.title, columns=str.upper))

#rename can be used in conjunction with a dict-like object providing new val‐ues for a subset of the axis labels:
print(data.rename(index={'OHIO': 'INDIANA'}, columns={'three': 'peekaboo'}))

data.rename(index={'OHIO': 'INDIANA'}, inplace=True)
print(data)
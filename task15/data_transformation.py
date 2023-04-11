import pandas as pd
import numpy as np

data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'], 'k2': [1, 1, 2, 3, 3, 4, 4]})
print(data)

#duplicated returns a boolean Series indicating whether each row is a duplicate (has been observed in a previous row) or not:
print(data.duplicated())
#drop_duplicates returns a DataFrame where the duplicated array is False:
print(data.drop_duplicates())
data['v1'] = range(7)
print(data.drop_duplicates(['k1']))
print(data.drop_duplicates(['k1', 'k2'], keep='last'))
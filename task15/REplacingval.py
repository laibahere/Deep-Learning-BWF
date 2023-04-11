import pandas as pd
import numpy as np
data = pd.Series([1., -999., 2., -999., -1000., 3.])
print(data)

#replacing one value 
print(data.replace(-999, np.nan))
#replacing more than 1 value
print(data.replace([-999, -1000], np.nan))
#To use a different replacement for each value
print(data.replace([-999, -1000], [np.nan, 0]))
print(data.replace({-999: np.nan, -1000: 0}))
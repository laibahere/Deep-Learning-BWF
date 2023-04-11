import pandas as pd
import numpy as np

string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
print(string_data) 
print(string_data.isnull())

string_data[0] = None
print(string_data.isnull())
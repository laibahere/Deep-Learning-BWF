import numpy as np
import pandas as pd

data = pd.DataFrame(np.random.randn(1000, 4))
print(data.describe())

col = data[2]
print(col[np.abs(col) > 3])
print(data[(np.abs(data) > 3).any(1)])

data[np.abs(data) > 3] = np.sign(data) * 3
print(data.describe())
print(np.sign(data).head())
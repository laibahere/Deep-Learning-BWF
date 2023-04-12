import numpy as np
import pandas as pd

#Reshaping with Hierarchical Indexing
data = pd.DataFrame(np.arange(6).reshape((2, 3)), index=pd.Index(['Ohio', 'Colorado'], name='state'),columns=pd.Index(['one', 'two', 'three'],name='number'))
print(data)

result = data.stack()
print(result)
print(result.unstack())
print(result.unstack(0))
print(result.unstack('state'))

s1 = pd.Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([4, 5, 6], index=['c', 'd', 'e'])
data2 = pd.concat([s1, s2], keys=['one', 'two'])

print(data2)
print(data2.unstack())
print(data2.unstack().stack())
print(data2.unstack().stack(dropna=False))

df = pd.DataFrame({'left': result, 'right': result + 5}, columns=pd.Index(['left', 'right'], name='side'))

print(df)
print(df.unstack('state'))
print(df.unstack('state').stack('side'))

#Pivoting “Long” to “Wide” Format
data = pd.read_csv('examples/macrodata.csv')

print(data.head())

periods = pd.PeriodIndex(year=data.year, quarter=data.quarter,name='date')
columns = pd.Index(['realgdp', 'infl', 'unemp'], name='item')
data = data.reindex(columns=columns)
data.index = periods.to_timestamp('D', 'end')
ldata = data.stack().reset_index().rename(columns={0: 'value'})
print(ldata[:10])

pivoted = ldata.pivot('date', 'item', 'value')
print(pivoted)

ldata['value2'] = np.random.randn(len(ldata))

pivoted = ldata.pivot('date', 'item')
print(pivoted[:5])
print(pivoted['value'][:5])
import numpy as np 
import pandas as pd

data = pd.Series(np.random.randn(9),index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'][1, 2, 3, 1, 3, 1, 2, 2, 3]])
print(data)
print(data.index)
print(data['b'])
print(data['b':'c'])
print(data.loc[['b', 'd']])
print(data.loc[:, 2])
print(data.unstack())
print(data.unstack().stack())


frame = pd.DataFrame(np.arange(12).reshape((4, 3)), index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]], columns=[['Ohio', 'Ohio', 'Colorado'],['Green', 'Red', 'Green']])
print(frame)

frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
print(frame)
print(frame['Ohio'])

print(frame.swaplevel('key1', 'key2'))
print(frame.sort_index(level=1))
print(frame.swaplevel(0, 1).sort_index(level=0))

print(frame.sum(level='key2'))
print(frame.sum(level='color', axis=1))


frame2 = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'], 'd': [0, 1, 2, 0, 1, 2, 3]})
print(frame2)
frame3= frame2.set_index(['c','d'])
print(frame3)


frame.set_index(['c', 'd'], drop=False)
print(frame2.reset_index())
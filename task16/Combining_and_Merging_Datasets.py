import pandas as pd
import numpy as np

#Database-Style DataFrame Joins
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],'data2': range(3)})

print(df1)
print(df2)
print(pd.merge(df1, df2))
print(pd.merge(df1, df2, on='key'))

df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],'data1': range(7)})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],'data2': range(3)})

print(pd.merge(df3, df4, left_on='lkey', right_on='rkey'))
print(pd.merge(df1, df2, how='outer'))

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'], 'data1': range(6)})
df2 = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],'data2': range(5)})

print(df1)
print(df2)
print(pd.merge(df1, df2, on='key', how='left'))
print(pd.merge(df1, df2, how='inner'))

left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'], 'key2': ['one', 'two', 'one'],'lval': [1, 2, 3]})
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],'key2': ['one', 'one', 'one', 'two'], 'rval': [4, 5, 6, 7]})

print(pd.merge(left, right, on=['key1', 'key2'], how='outer'))

print(pd.merge(left, right, on='key1'))
print(pd.merge(left, right, on='key1', suffixes=('_left', '_right')))

#Merging on Index
left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'], 'value': range(6)})
right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
print(left1)
print(right1)
print(pd.merge(left1, right1, left_on='key', right_index=True))
print(pd.merge(left1, right1, left_on='key', right_index=True, how='outer'))

lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio','Nevada', 'Nevada'],'key2': [2000, 2001, 2002, 2001, 2002],'data': np.arange(5.)})

righth = pd.DataFrame(np.arange(12).reshape((6, 2)), index=[['Nevada', 'Nevada', 'Ohio', 'Ohio','Ohio', 'Ohio'], [2001, 2000, 2000, 2000, 2001, 2002]], columns=['event1', 'event2'])

print(lefth)
print(righth)
print(pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True))
print(pd.merge(lefth, righth, left_on=['key1', 'key2'],right_index=True, how='outer'))

left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'], columns=['Ohio', 'Nevada'])

right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],index=['b', 'c', 'd', 'e'],columns=['Missouri', 'Alabama'])

print(left2)
print(right2)
print(pd.merge(left2, right2, how='outer', left_index=True, right_index=True))
print(left2.join(right2, how='outer'))
print(left1.join(right1, on='key'))

another = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]], index=['a', 'c', 'e', 'f'], columns=['New York', 'Oregon'])

print(another)
print(left2.join([right2, another]))
print(left2.join([right2, another], how='outer'))

#Concatenating Along an Axis
arr = np.arange(12).reshape((3, 4))
print(np.concatenate([arr, arr], axis=1))

s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])

print(pd.concat([s1, s2, s3]))
print(pd.concat([s1, s2, s3], axis=1))

s4= pd.concat([s1, s3])
print(s4)

print(pd.concat([s1, s4], axis=1))
print(pd.concat([s1, s4], axis=1, join='inner'))
print(pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']]))

result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])
print(result)
print(result.unstack())
print(pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three']))
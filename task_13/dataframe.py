import pandas as pd

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002, 2003],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)
print(frame.head(2))
print(pd.DataFrame(data, columns=['year', 'state', 'pop']))

frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four','five', 'six'])
print(frame2)
print(frame2.columns) # printing the name of colums 
print(frame2['state']) #printing state from frame2 
print(frame2.year) #years from frame2 
print(frame2.loc['three']) #printing row three
debto=frame2['debt'] = 16.5 # assigning value to empty debt column
print(frame2)
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
print(frame2)
frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)
del frame2['eastern'] # to del
print(frame2)

pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
print(frame3)
print(frame3.T) #Transpose
pd.DataFrame(pop, index=[2001, 2002, 2003])
print(frame3)

pdata = {'Ohio': frame3['Ohio'][:-1], 'Nevada': frame3['Nevada'][:2]}
print(pd.DataFrame(pdata))
frame3.index.name = 'year'; frame3.columns.name = 'state'
print(frame3)
print(frame3.values)
print(frame2.values)
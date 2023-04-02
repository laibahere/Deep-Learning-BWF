import pandas as pd
#indexing a series
obj = pd.Series([4, 7, -5, 3])
print(obj)
print(obj.values) 
print(obj.index) # like range 

#Series with an index identifying each data point with a label:
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
print(obj2.index)
a=obj2['a'] # to print a single value
print(a)
b=obj2['d'] = 6 #changing the value
print(obj2)
c= obj2[['c', 'a', 'd']]
print(c)

#arthimateic operations
d=obj2[obj2 > 0]
print(d)
e= obj2*2
print(e)
g='b' in obj2
print(g)
ee= 'e' in obj2
print(ee)

#Series from it by passing the dict:
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
print(obj4)

null=pd.isnull(obj4)
print(null)

ntnull=pd.notnull(obj4)
print(ntnull)

plus=obj3 + obj4
print(plus)

pop=obj4.name = 'population'
sat=obj4.name = 'state'
print(pop)
print(sat)
print(obj4)

print(obj)
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)
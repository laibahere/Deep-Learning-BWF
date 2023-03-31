import numpy as np 

a = np.array([1,2,3],dtype='int16')
print(a)

b = np.array([[9,8,7,6,5],[4,3,2,1,0]])
print(b)

#to get dimensions 
print(a.ndim)
print(b.ndim)

#to get shape
print(a.shape)
print(b.shape)

#to get type
print(a.dtype)
print(b.dtype)

#to get size
print(a.itemsize) #in bytes
print(b.itemsize) 
print(a.size) 
print(b.size) 
print(a.nbytes) # total size # itemsize *size =total size
print(b.nbytes) 

#------Accessing/ Changing specific elements, row,coloums etc-----

c = np.array([[1,2,3,4,5,6,7], [8, 9, 10, 11, 12, 13, 14]])
print (c)

#to get a specific element [r,c]
print(c[1,5])

#to get a specific row
print(c[0,:])

#to get a specific column
print(c[:,2])

#Getting a little more fancy [startindex: endindex: stepsize]
print(c[0, 1:-1:2])

#to change a element in a array
c[1,5]=20 
print(c)

#to change a row
c[:,2]=5
print(c)

c[:,2] =[1,2]
print(c)

#to change a column
c[1,:] = 3
print(c)

#3d example
d = np.array([[[1,2], [3,4]], [[5,6],[7,8]]])
print (d)

# get specific element
d[0,1,1]
print(d)
# replace
d[:,1,:] = [9,9]
print(d)

#--------Intializing different arrays---------
#All zero Matrix
e = np.zeros((2,2 ))
print(e)

#all 1 matrix 
f= np.ones((4,2,2),dtype='int32')
print(f)

#any other number 
g= np.full((2,2),99) #first shape then the number we want 
print(g)

#any other number (full like )
h= np.full(a.shape,4)
print(h)

#random decimal number 
i = np.random.rand(4,2,3)
print(i)
#Random integer values
j= np.random.randint(7,size=(3,3))
print(j)

#identity matrix
k = np.identity(3)
print(k)

# to repeat an array 
arr = np.array([1,2,3])
rl=np.repeat(arr,3) # repeat array 3 times 
print(rl)

#be careful when copying an array 
v= np.array ([1,2,3])
x = v
x[0]=100
print(x)
print(v)
#both will change so we will use copy command 
m= np.array ([1,2,3])
n = m.copy()
n[0]=100
print(m)
print(n)
 
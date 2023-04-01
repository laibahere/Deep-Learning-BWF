import numpy as np


#multiplocation of two (2,3)matrix to (3,2)matrix
a= np.ones((2,3))
print(a)
b=np.full((3,2),2)
print(b)
print(np.matmul(a,b)) #or
print(a@b)

#to find out determinant of a matrix 
#of an identity matrix 
c= np.identity(3)
print(np.linalg.det(c))


#dot product of two arrays
print(np.dot(a,b))
#For 2-D arrays(dot product)
d = [[1, 0], [0, 1]]
e= [[4, 1], [2, 2]]
print(np.dot(d, e))

#to calculate mean of an array 
xme = np.array([1, 2, 3, 4, 5])
mean_x = np.mean(xme)
print(mean_x)

#To calculate the median of an array
xn = np.array([1, 2, 3, 4, 5])
median_x = np.median(xn)
print(median_x)


# the quantiles of an array
xl= np.array([1, 2, 3, 4, 5])
q1_x = np.percentile(xl, 25)
q2_x = np.percentile(xl, 50)
q3_x = np.percentile(xl, 75)
print(q1_x, q2_x, q3_x)

 #calculate the rank of an array
h = np.random.randint(1, 11, size=10)
rank = np.linalg.matrix_rank(h)

print("Array: ", h)
print("Rank: ", rank) 
#probablity distribution
import math


def normal_distribution(xp):
    return (1/(math.sqrt(2*math.pi)))*np.exp(-(xp**2)/2)

xp = np.random.normal(0, 1, size=10)
pdf = normal_distribution(xp)
cdf = [np.sum(normal_distribution(xp[:i])) for i in range(len(xp))]

print("Random numbers: ", xp)
print("PDF: ", pdf)
print("CDF: ", cdf)
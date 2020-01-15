#Numpy Tutorial 

pip install numpy
import numpy as np 


#Mathematical Functions on Arrays in NumPy

np.subtract(a,b) #Same as a-b
np.multiply(a,b) #a*b works too
np.divide(a,b) #Same as a/b
np.sqrt(a) #Produces square root
a = np.array([[1,2],[3,4]])
np.sum(a)
np.sum(a,axis=0) #Sum of each column
np.sum(a,axis=1) #Sum of each row
a.T #Transpose

x=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])
v=np.array([9,10])
w=np.array([11,12])
v.dot(w) #Same as np.dot(v,w)


a=np.array([1,2,3])
type(a)
a.shape #dimension 
b.size #number of elements 

np.arange(7) #This is like range in Python
np.random.random((3,3)) #3 x 3 matrix with random values
np.ones((2,3)) #2 x 3 one matrix 
np.zeros((1,2)) #1 x 2 zero matrix 
np.full((3,2),7) #Matrix of constants value 7
np.linspace(1,2,4) #4 values spaced evenly between, and including, 1 and 2.

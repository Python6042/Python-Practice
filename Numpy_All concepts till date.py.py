#!/usr/bin/env python
# coding: utf-8

# In[1]:


# What is Numpy?
# Numpy is the multi-dimentional arry of same time.It is maily used in Logical,stastical , Fourier transforms. And Manily used in Data science
# Numpy array can be created using below three ways


# 1.Using Numpy functions
# 2.Using other python structures like list,tuple etc.,
# 3.Using special library function


# In[4]:


## 1 How to create Numpy array using Numpy functions?

# arange,reshape are two functions using to create an n-dimentional arry
# uses of arange
# arange function is same like range() function , Ex: arange(start,stop,step count)

import numpy as np
a1=np.arange(1,10)
print(a1)
b1=np.arange(1,10,2)
print(b1)


# In[5]:


# reshape function is used to create a single dimentional array to n-dimentional array
# Syntax: reshape(size)

r1=a1.reshape(3,3)
print(r1)


# In[9]:


# So, by combining two functions we can crate an arry of n-dimentioanl array
# NOTE: The number elements in the arrange is equals to multiply of shape( ex: 20=5*4)
e1= np.arange(20).reshape(5,4)
print(e1)


# In[ ]:


# Other numy functions to create n-d array are below functions:

# empty(),full((size),value),ones(),zeros(),eye(),linspace()
# eye() create an array of given size with digonals are 1's and other elements are zero
# linspace creates equally spaced elements(The elements we request) between the given size


# In[17]:


# linspace example
l2=np.linspace(2,8,5) # we are requesting for 5 equally spaced numbers between 2,8
print(l2)


# In[10]:


## 2 Creating arrays using python lists 

a2=np.array([1,2,3,4])  # Single dimentional array
print(a2)


# In[11]:


a3=np.array([[1,2],[3,4]]) # two dimentional array
print(a3)


# In[13]:


# Similary we can array from the tuple as well
l1=np.array((1,2,3,4)) # Single dimentional array
print(l1)


# In[16]:


l2=np.array(((1,2,3,4),(5,6,7,8))) # Two dimentional array
print(l2)


# In[19]:


## 3 Creating array using special library function called random()
# random functions is used to create an array of values of given size between 0 and 1
# we are importing random() function from random module...so below is the syntax

r2=np.random.random((3,3))
print(r2)


# In[20]:


### below ar the basic functions,attributes of Numpy arrays


# In[21]:


# One of the attribute to find the size/(total numbers) of the array is: size attribute
print(a1.size)


# In[22]:


# To Find shape of the array we use , .shape attribute
print(a1.shape)


# In[26]:


print(r2.shape)


# In[28]:


print(r1)
print()
print(r2)


# In[27]:


# used of flatten or ravel functions
# These two functions are used to create n-dimentional array to single dimentional array
r2=r1.ravel()
print(r2)
f1=r1.flatten()
print()
print(f1)


# In[30]:


# To find dimention of the array we use attribute " ndim" , to find type of the numpy array we use "dtype"
print(r1.ndim) # Prints 2 as r1 arrays is 2*2 matrix
######
print(r2.ndim) # prints 1 as r2 array is 1-dimentional matrix


# In[31]:


# Finding type of the array
print(r1.dtype)


# In[33]:


# Operations on one dimentional array
# Arthimetic operations on 1-D array. We can perform all the arthimetic operations on arrays. 
#if you add the arrays, the arithmetic operator will work element-wise

m1=np.array([1,2,3,4])
m2=np.array([4,5,6,7])
print(m1+m2)


# In[35]:


#If we try to add arrays with the same dimension but a different number of elements, we will get an value error
print(l1+r2)


# In[36]:


print(m1*2) # Multiples each element by 2


# In[37]:


print(m1**2) # Calculates the square of the array m1


# In[38]:


# If we would like to cube the individual elements, or even higher up, we can use the power function

print(pow(m1,3))


# In[40]:


###  using Numpy array using conditional expressions 
# we can use conditionals to find the values that match your criteria. Since m1 is an array, the result of a conditional operation is also an array. 
# When we perform a conditional check, the output is an array of booleans.

m3= m1>3
print(m3)


# In[42]:


# we can also pass this array of booleans to the main array to fetch the values that match criteria.
print(m1[m3])


# In[43]:


# Rather than creating a separate array of booleans, we can specify the conditional operation directly on the main array asbelow
print(m1[m1>3])


# In[45]:


### Operations on a 2D Array
# Arthimetic operations
n1=np.array([[1,2],[3,4]])
n2=np.array([[3,4],[5,6]])
print(n1)
print()
print(n2)


# In[47]:


print(n1+n2) # The elements at the respective positions in arrays are added together.


# In[49]:


# All the arithmetic operations work in a similar way. we can also multiply or divide the arrays. The operations are performed element-wise.
print(n1*n2)


# In[64]:


# Similaryly like other programming languages like C#,java  we can operators like += ,-=,*= to calucute addition,subtractio,multiplicaion,etc
print(n1)
print()
n1*=2
print(n1)


# In[65]:


### Matrix multiplication:
# we can perform matrix multiplicaion using two ways
# using dot function
# using @ operator

print(n1.dot(n2))


# In[66]:


# Above same can be achive using @ opertor as below
print(n1@n2)


# In[68]:


# Finding transpose of a matrix
# Transpose of a matrix can be achived using the opertor T
print(n1)
print("The transpose of a matrix is:")
print(n1.T)


# In[69]:


## Arthimetic functions in numpy
# There are several functions(like min(),max(),sum()) that we can use to perform arithmetic operations on this array. For example, the sum function adds all the values in the array and gives a scalar output
print(m1)
print()
print(m2)


# In[70]:


print(m1.sum())


# In[71]:


print(f"maximum value is:{m1.max()}")
#print(m1.max())
print(f"minimum values i:{m1.min()}")


# In[74]:


# Using Axis Parameter
# If we have more than one dimension in an array, we can define the axis; 
print(n1)
print(f"The maximum values in row wise is:{n1.max(axis=1)}")
print(f"The maximum values in column wise is:{n1.max(axis=0)}")


# In[75]:


## Logical Operators in Numpy
# Numpy provides logic functions like logical_and, logical_or etc., in a similar pattern to perform logical operations.
np.logical_and(True,True)


# In[76]:


np.logical_or(True,False)


# In[77]:


# we can give expression as well
np.logical_or(5>4,1<0)


# In[80]:


###  Other Functions in Numpy
# In addition to arithmetic operators, Numpy also provides functions to perform arithmetic operations. 
# we can use functions like add, subtract, multiply, divide to perform array operations

print("value of m1 is:",m1)
print("value of n1 is:\n",n1)


# In[86]:


# as these functions are numpy functions we should call using the alias name as np.function name
print(np.sum(m1)) # prints sum of values of m1 array
print(np.sum(n1)) #prints sum of values of n1 array


# In[87]:


print(np.add(n1,n2)) # Calctest the sum of the elemtns in the elemtns wise 


# In[88]:


print(np.subtract(n2,n1))


# In[90]:


# stastical functions of numpy
# The stastical functions are mean,median,mode
# mean is the sum of all values divide by total number of values
# median is the middle/centre  of all the elements



print(f"Mean of the n1 array is\n:{np.mean(n1)}")
print("Median of the n1 array is:",np.median(n1))


# In[97]:


##  Universal functions (ufunc): NumPy provides familiar mathematical functions such as sin, cos, exp, etc. 
# These functions also operate elementwise on an array, producing an array as output.

print("Exponential of m1 array is:",np.exp(m1))
print("Sin values of m1 array is:",np.sin(m1))
print("Square roots of the array n1 is:",np.sqrt(n1))


# In[98]:


## Sorting an error
## Numpy array can be sorted using the numpy methion np.sort()

print("Sorted array of n1 is:",np.sort(n1))


# In[99]:


print(n1)
print()
print("Sorted array of n1 is:",np.sort(n1,axis=1)) # To sort an array in columwise


# In[103]:


# We can even specify alogirighm to sort an array using kind is equals to "merge sort","Quick sort"etc
msort=np.array([22,33,41,21,12,61,88,11,9])
print("Sorted array is:",np.sort(msort))
print("Sorted array using merge sort is:",np.sort(msort,kind='mergesort'))
print("Sorted array using quick sort is:",np.sort(msort,kind="quicksort"))


# In[104]:


## Array indexing
## Numpy arrays can be accessed using the following three ways
# Using Slicing
# Using Integer array indexing
# Using Boolean array indexing


# In[105]:


# Accessing the elements using Slicing 
# Slicing: Just like lists in python, NumPy arrays can be sliced. 
# As arrays can be multidimensional, we need to specify a slice for each dimension of the array.
print(m1)
print()
print(n2)


# In[108]:


print(m1[2]) # prints only the values at index 2


# In[109]:


print(m1[:2]) # prints allthe values starts from index2 till the end


# In[112]:


n4=np.arange(27).reshape(3,9)
print(n4)


# In[118]:


# from the above array if we want to get subarry [4,5,6],[13,14,15],[22,23,24 ] can be achived using the slicing as below
print(n4[:,4:7])


# In[123]:


## Using Integer array indexing 

# Integer array indexing: In this method, lists are passed for indexing for each dimension. 
# One to one mapping of corresponding elements is done to construct a new arbitrary array.
temp=n4[[1,2,2,0],[3,4,7,5]] # First array represents rows and the secongd arryay represents columns,if we give out of range then we will get index error
print(temp)


# In[130]:


## Using Boolen opertions is nothing but picking an arry based on some condition
print(n4[n4>8 ]) # All the elements more than 8 are printed 


# In[132]:


### Splitting an array 

# numpy.split. If indices_or_sections is an integer, N, the array will be divided into N equal arrays along axis. 
# If such a split is not possible, an error is raised. If an index exceeds the dimension of the array along axis, an empty sub-array is returned correspondingly.
# Example demonstring above

sp=np.arange(24)
print(np.split(sp,4)) # np.split(arry,num), the number represents the number of arrays, given the n should be factor for number of elemtns in the arry
print()
print(np.split(sp,6))
print()
print(np.split(sp,8))


# In[133]:


# if the number is not factor of number of elements the array a value error will be returned.

print(np.split(sp,5))


# In[144]:


# spliting the 1-d arrays by specifing the indexes .. If an index exceeds the dimension of the array along axis, an empty sub-array is returned correspondingly.

sp1=np.arange(10)
print(np.split(sp1,[8,3,2,1])) # Noticed that the sequence should be in assending order 


# In[ ]:


## there are different kinds of splittings as listed below

''' array_split
Split an array into multiple sub-arrays of equal or near-equal size. Does not raise an exception if an equal division cannot be made.
hsplit
Split array into multiple sub-arrays horizontally (column-wise).
vsplit
Split array into multiple sub-arrays vertically (row wise).
dsplit
Split array into multiple sub-arrays along the 3rd axis (depth).
concatenate
Join a sequence of arrays along an existing axis.
stack
Join a sequence of arrays along a new axis.
hstack
Stack arrays in sequence horizontally (column wise).
vstack
Stack arrays in sequence vertically (row wise).
dstack
Stack arrays in sequence depth wise (along third dimension).'''


# In[ ]:





# In[ ]:





# In[ ]:





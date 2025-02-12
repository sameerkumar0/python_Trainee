import numpy as np

# arr=np.array([5,6,3,7,8,9,5,55])
# print(arr)


# 2-D array

arr=np.array([[1,5,4,7,8],[5,6,9,7,8]],ndmin=3)
print(arr)


# a=np.array([1,2,3],dtype=complex)
# print(a)

zr=np.zeros((3,4)) # create array of ones 
one=np.ones((2,3)) # create array of zeroes
print("Ones Array:\n",one)
print("Zeroes array: \n",zr)

idm=np.eye(3) # create identity matrix
print(idm)

random=np.random.rand(3,3)# create matrix with random value
print(random)


Range=np.arange(0,10,2)
print(Range)

print(np.linspace(0,10,5))

print(arr.shape)
print(arr.ndim)
print(arr.size)

arr=np.array([[1,5,6,4],[8,6,4,5]])
arr_reshape=arr.reshape((4,2))
arr_flatten=arr.flatten()
print(arr)
print(arr_reshape)
print(arr_flatten)


ar=np.array([[2,5,9,7],[8,9,6,4]])
print(ar)
print(ar[1,1])
print(ar[:,1]) # second column
print(ar[0,:])

arr1=np.array([1,5,6,7,8,9])
print(np.sum(arr1))
print(np.mean(arr1))
print(np.max(arr1))
print(np.min(arr1))

# # matrix operation
# a=np.array([[1,2],[4,5]])
# b=np.array([[6,7],[8,9]])
# print(np.dot(a,b)) # matrix multiplication
# print(np.transpose(a)) 

#stacking and splitting array

a=np.array([1,5,6,7])
b=np.array([5,6,4,5])
print(np.vstack((a,b)))
print(np.hstack((a,b)))

# splitting
arr = np.array([1, 2, 3, 4, 5, 6])
print(np.split(arr,2)) # split the array in two equal parts

# filter array function
arr=np.array([10,20,30,50,40,])
print(arr[arr>20])
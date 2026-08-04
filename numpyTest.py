# Topic Covered
# 1. Importing Numpy Library
# 2. creating array from list, tuple,set
# 3. checking different dimentional array 0D, 1D, 2D, 3D, 4D, 5D, etc with arr.ndim function
# 4. creating different dimentional array 0D, 1D, 2D, 3D, 4D, 5D, etc with ndmin function
# 5. Slicing array  wiht 1D or multi dimenstion array
# 6. Indexing array elemnt from 1D to multi Dimension array



# Note: 
# Row index & column index start with zero (0)


# Importing Numpy Library
# import numpy as np

# Creating Numpy Array
# arr =np.array((1,2,3,4,56,4,8,9,9,60)) #1D

# Printing Numpy Arrya
# arr =np.array(10)

# Creating 2D Numpy aray
# arr=np.array([10,12], [14,15])
# print(arr)

# Printing Numpy array type i.e. numpy.ndarray
# print(type(arr))
# print(id(arr))

# -----------------------------------------------------

# arr =np.array(10) #0 D
# arr=np.array([[10,12], [14,15]]) #2D
# arr=np.array([[[10,12], [14,15]], [[10,12], [14,15]]])    #3D
# arr =np.array( [1,2,3,4,5 ], ndmin=5) #N Dimetion
# print(arr)
# print(arr.ndim)

# arr=np.array([1,2,3,4,5])
# print(arr[0])
# print(arr[1:4])
# print(arr[-1])

# arr=np.array([[1,2,3],[4,5,6]])
# print(arr)
# print(arr[0,1])
# print(arr[1,1])
# print(arr[1,0:2])


# arr=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print(arr)
# print(arr.ndim)
# print(arr[0,0,0])
# print(arr[0,1,2]) #6
# print(arr[0,2,0])#7
# print(arr[0,0,-1])  #3
# print(arr[0,2,0:2])


# import numpy as np
# ar=np.array([[1,2,3],[4,5,6]])
# print(ar)
# print(ar.ndim)
# print(ar.shape)
# print(type(ar))

# print(np.zeros((3,3)))
# print()
# print(np.ones((3,3)))

# print complete second column from both rows
# ar=np.array([[1,2,3],[4,5,6]])
# print(ar[:, 1])
# Note : ":" means entire rows, and 1 means second column

# print(ar[1, :])  # second Rows, entire columns

# # Boolean Masking =============

# ar= np.array([1,2,3,4,5,6,7,8,9,10])
# print(ar>4)
# print(ar[ar>4])

# # Q. given a list of int, set all element greater than 5 to -1
# # expected : [1,4,-1,5,-1]
# # ls=[1,2,3,4,5,6,7,8,9,10]
# # print(ls)

# # lx =[x for x in ls if x > 5 ls[ls.index(x)]]
# # for i in ls:
# #     if i >5:
# #         ls[ls.index(i)] =-1

# # print(ls)

# ar[ar>5] = -1
# print(ar)

# # Vectorization --> element wise operations
# a=np.array([1,2,3])
# b=np.array([4,5,6])

# print(a+b)
# # concept similar to broadcasting as below
# print(a+10)
# print(a**2)

# # m=[1,2,3]
# # n=[4,5,6]
# # c=[m[i] + n[i] for i in range(len(m))]
# # print(c)


# print(np.sum(a))

# print(np.mean(a))
# print(np.median(b))

# print(np.std(b))
# print(np.max(b))
# print(np.min(b))



# print(b[np.argmax(b)])




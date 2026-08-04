# Numpy 

# EX 1
import numpy as np 

# arr =np.array([1,2,3,4,5,6])

# print(arr)


# print(type(arr))

# arr2= np.array((1,2,3,4,5))
# print(arr2)


# ar0=np.array(112)
# ar1=np.array([1,2,3])
# ar2=np.array([[1,2,3],[1,4,5]])
# ar3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[2,5,8]]])

# print(ar0.ndim)
# print(ar1.ndim)
# print(ar2.ndim)
# print(ar3.ndim)

# ar4=np.array([1,5,9],ndmin=5)
# print(ar4)
# print(ar4.ndim)

# ar5=np.array([1,2,5,8,9])
# print(ar5[3])
# print(len(ar5))
# print(ar5[:-2])
# print(ar5[-3:])
# print(ar5[2:])

# print(ar2)
# print(ar2[0,2])
# print(ar2[1,2])
# print(ar2[0,:])
# print(ar2[:,1])
# print(ar2[0,-2:-1])

# print(ar3)
# print(ar3[0,0,1])
# print(ar3[0,[0,1],0])


# Data Type in Numpy
# i-integer
# b-boolean
# u-unsigned integer
# f-float
# c-complex float
# m-timedelta
# M-datetime
# o-object
# S-string
# U-unicode string
# V-fixed chunk of memory for other type (void)


# .--------------------------
# import numpy as np

# arr=np.array([1,2,3,4])

# print(arr.dtype)

# arr2=np.array(["jdfskfl", "nakdkd","fsff"])
# print(arr2.dtype)
# # arr3=np.array([1,2,3,4], dtype="S")
# arr3=np.array([1,2,3,4], dtype="i4")
# print(arr3)
# print(arr3.dtype)

# arr4=np.array([1.1,1.2,1.3])
# # newarr=arr4.astype("i")
# # newarr=arr4.astype(int)
# newarr=arr4.astype(bool)
# print(newarr)
# print(newarr.dtype)

# --------------------
# View and Copy 
# import numpy as np

# arr =np.array([1,2,3,4,5])
# x=arr.copy()
# print(arr)
# print(x)

# arr[0]=10
# print(arr)
# print(x)

# import numpy as np

# arr =np.array([1,2,3,4,5])
# x=arr.view()
# print(arr)
# print(x)

# arr[0]=10
# print(arr)
# print(x)


# Owns the data
# import numpy as np

# arr =np.array([1,2,3,4,5])
# x=arr.copy()
# y =arr.view()
# print(x)
# print(y)

# print(x.base)
# print(y.base)

# -----------------
# Shape

# import numpy as np

# arr =np.array([[1,2,30],[4,5,6]])
# print(arr)
# print(arr.shape)


# ---------------------
# Reshaping
# import numpy as np

# arr= np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(arr)
# # print(arr.shape)
 
# newar=arr.reshape(4,3)
# print(newar)
# print()
# newar2=arr.reshape(2,3,2)
# print(newar2)
# print()
# arr2=np.array([1,2,3,4,5,6,7,8])
# # print(arr2.reshape(2,4).base)
# arrnew=arr2.reshape(2,2,-1)
# print(arrnew)
# print()

# new2=arrnew.reshape(-1)
# print(new2)

# ----------------------
# Loop

# import numpy as np

# arr =np.array([1,2,3,4,5])

# for i in arr:
#     print(i)

# print()

# arr=np.array([[1,2,3],[4,5,6]])
# # for i in arr:
# #     print(i)

# for x in arr:
#     for y in x:
#         print(y)

# print()

# arr=np.array([ [[1,2,3],[4,5,6]],[ [1,4,7],[2,5,8] ] ])
# print(arr.ndim)

# for i in arr:
#     print(i)

# for x in arr:
#     for y in x:
#         for z in y:
#             print(z)

# for i in np.nditer(arr):
#     print(i)

# -------------
# arr=np.array([1,2,3,4,5,6])

# for i in np.nditer(arr, flags=["buffered"], op_dtypes=["S"]):
#     print(i)
# # /----------

# arr=np.array([[1,2,3],[4,5,6]])
# for i in np.nditer(arr[:,::2]):
#     print(i)
# /--------
# arr=np.array([1,2,3,4,5,6])
# for idx, i in np.ndenumerate(arr):
#     print(idx,i)

# arr=np.array([ [1,2,3],[4,5,6] ])
# for idx, i in np.ndenumerate(arr):
#     print(idx, i)

# /-----------------------------------
# Join
import numpy as np

# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])

# arr=np.concatenate((arr1, arr2))
# print(arr)

arr1=np.array([ [1,2],[3,4] ])
arr2= np.array( [ [6,7],[8,9]])
arr=np.concatenate((arr1,arr2), axis=1)

print(arr)







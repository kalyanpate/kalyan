#Array in python
#  array module.
# Arrays are represented as a collection of multiple containers where each container stores one element. These containers are indexed from '0' to 'n-1', where n is the size of that particular array.
# Index starts with 0.
# Array length is 10 which means it can store 10 elements.
# Each element can be accessed via its index.




# Creating 
# import the array module and use its array() function
import array as arr

# The array() function accepts typecode and initializer as a parameter value and returns an object of array class.
# typecode − The typecode character used to speccify the type of elements in the array.

# initializer − It is an optional value from which array is initialized. It must be a list, a bytes-like object, or iterable elements of the appropriate type.

#interger array-i
arr_obj=arr.array('i',[1,2,5,3])
print(arr_obj)

#char -u
arr_obj2=arr.array('u','kalyan')
print(arr_obj2)

# Float -d
arr_obj3=arr.array('d',[1.1,2.2,3.3,4.4])
print(arr_obj3)


# Basic Operations on Python Arrays
# Following are the basic operations supported by an array −

# Traverse − Print all the array elements one by one.

# Insertion − Adds an element at the given index.

# Deletion − Deletes an element at the given index.

# Search − Searches an element using the given index or by the value.

# Update − Updates an element at the given index.

# Accessing 
arrob1=arr.array('i',[1,2,3,4,5])
print(arrob1[0])
print(arrob1[2])

# Insertion 
arrob1.insert(1,60)
print(arrob1)
print(arrob1[1])


# Deletion 
arrob1.remove(60)
print(arrob1)
print(arrob1[1])

for i in arrob1:
    print(i)

# Search 
# an array element based on its value or its index.
print (arrob1.index(4))   #  : If the value is not present in the array, it will return an error.

# Update 
arrob1[0]=100
print(arrob1[0])

# -------------Access Array Items-----------
# Using indexing
print(arrob1[2])
# Using iteration
for i in arrob1:
    print(i)
# Using enumerate() function
# The enumerate() function can be used to access elements of an array. It accepts an array and an optional starting index as parameter values and returns the array items by iterating.
# use of enumerate() function
for loc, val in enumerate(arrob1):
    print(f"Index: {loc}, value: {val}")


# Accessing a range of array items in Python
# Use the [:index] format to access elements from beginning to desired range.

# To access array items from end, use [:-index] format.

# Use the [index:] format to access array items from specific index number till the end.

# Use the [start index : end index] to slice the array elements within a range. You can also pass an optional argument after end index to determine the increment between each index.

# slicing operation
print (arrob1[2:])
print (arrob1[0:3])


# ----------Add Array Items---------

# Using append() method- at last -It accepts a single item as an argument and append it at the end of given array.
# Using insert() method - add a new element at the specified index using the insert() -It accepts two parameters which are index and value and returns a new array after adding the specified value.
# Using extend() method -merger another to sanme - It is used to add all elements from an iterable or array of same data type.


a = arr.array('i', [1, 2, 3, 4, 5])
b = arr.array('i', [6,7,8,9,10])
a.extend(b)
print (a)

# ------ Remove Array Items-------
#  remove() - accepts an element and removes it if the element is available in the array
#  pop() -removes an element at the specified index from the array and returns the element at ith position after removal.



# ------Loop Arrays---------

newArray = arr.array('i', [56, 42, 23, 85, 45])
for iterate in newArray:
   print (iterate)

# creating array
a = arr.array('i', [96, 26, 56, 76, 46])

# checking the length
l = len(a)

# loop variable
idx = 0

# while loop
while idx < l:
   print (a[idx])
   # incrementing the while loop
   idx+=1


# ---------- Copy Arrays-------------

































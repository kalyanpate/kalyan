#---------Tuple----------------
#Tuple is one of the built-in data types in Python. 
# A Python tuple is a sequence of comma separated items, enclosed in parentheses (). 
# The items in a Python tuple need not be of same data type.


tup1=("kalyan","kapil", 1,25,35)
tup2="Arjun", 12, 14, "Pate", 25,35
empty_tup=()

print(f'1st Tuple: {tup1}')
print(f'2nd Tuple: {tup2}')
print(f'empty Tuple: {empty_tup}')

#Even if there is only one object in a tuple, you must give a comma after it. Otherwise, it is treated as a string.
single_tup=("single_tuple",)

#In Python, tuple is a sequence data type. It is an ordered collection of items.
#  Each item in the tuple has a unique position index, starting from 0.

# In C/C++/Java array, the array elements must be of same type.
#  On the other hand, Python tuple may have objects of different data types.

# Python tuple and list both are sequences. 
# One major difference between the two is, Python list is mutable,
#  whereas tuple is immutable. 
# Although any item from the tuple can be accessed using its index, 
# and cannot be modified, removed or added.


#-Accessing Values in Tuples :using index
print(f'{tup1[3]} -Accessed using index value')
print(f'{tup2[1:3]}  -Accesd using index range')

#Updating Tuples
#Tuples are immutable which means you cannot update or change the values of tuple elements. 
# You are able to take portions of existing tuples to create new tuples as the following example demonstrates −

tup3=tup1 + tup2
print(tup3)

#Delete Tuple Elements
#Removing individual tuple elements is not possible. 
# There is, of course, nothing wrong with putting together another tuple with the undesired elements discarded.

#To explicitly remove an entire tuple, just use the del statement. 

print(tup3)
del tup3
# print(tup3) #NameError: name 'tup3' is not defined. Did you mean: 'tup1'?


#Python Tuple Operations

#contenation
tup4="hello", "World"
tup3=tup1+tup4
print(tup3)

#Repetation
print(tup4 * 3)

#Membership
print(25 in tup1)

#Indexing, Slicing, and Matrixes
print(tup1[2])  #indexing
print(tup1[-2]) #indexing, slicing
print(tup1[1:]) #slicing , Matrices

# No Enclosing Delimiters
#Any set of multiple objects, comma-separated, written without identifying symbols,
#  i.e., brackets for lists, parentheses for tuples, etc., 
# default to tuples

#Built-in Functions with Tuples

print(len(tup1))

#------Access Tuple Items-----

#Each element in a tuple corresponds to an index. 
#The index starts from 0 for the first element and increments by one for each subsequent element. 
#Index of the last item in the tuple is always "length-1", where "length" represents the total number of items in the tuple. 

tuple1 = ("Rohan", "Physics", 21, 69.75)
tuple2 = (1, 2, 3, 4, 5)

print ("Item at 0th index in tuple1: ", tuple1[0])
print ("Item at index 2 in tuple2: ", tuple2[2])

#Accessing Tuple Items with Negative Indexing

#Negative indexing in Python is used to access elements from the end of a tuple, with -1 referring to the last element, -2 to the second last, and so on.
print ("Item at 0th index in tuple1: ", tuple1[-1])

#Accessing Range of Tuple Items with Negative Indexing
print ("Items from index 2 to last in tup2", tuple2[2:-1])


#Access Tuple Items with Slice Operator
#[start:stop] #start is the starting index (inclusive). #stop is the ending index (exclusive).

tuple1 = ("a", "b", "c", "d")
tuple2 = (25.50, True, -55, 1+2j)
tuple3 = (1, 2, 3, 4, 5)
tuple4 = ("Rohan", "Physics", 21, 69.75)

print ("Items from index 1 to last in tuple1: ", tuple1[1:])
print ("Items from index 0 to 1 in tuple2: ", tuple2[:2])
print ("Items from index 0 to index last in tuple3", tuple3[:])

# Items from index 1 to last in tuple1:  ('b', 'c', 'd')
# Items from index 0 to 1 in tuple2:  (25.5, True)
# Items from index 0 to index last in tuple3 ('Rohan', 'Physics', 21, 69.75)


#Accessing Sub Tuple from a Tuple (#A subtuple is a part of a tuple)

tuple1 = ("a", "b", "c", "d")
tuple2 = (25.50, True, -55, 1+2j)

print ("Items from index 1 to 2 in tuple1: ", tuple1[1:3])
print ("Items from index 0 to 1 in tuple2: ", tuple2[0:2])

# Items from index 1 to 2 in tuple1:  ('b', 'c')
# Items from index 0 to 1 in tuple2:  (25.5, True)


#-------------Updating Tuples in Python--------
# tuple is an immutable sequence, meaning once a tuple is created, its elements cannot be changed, added, or removed.
#To update a tuple in Python, you can combine various operations to create a new tuple. 

#Updating Tuples Using Concatenation Operator
#When applied to tuples, the concatenation operator joins the elements of the two (or more) tuples to create a new tuple containing all the elements from both tuples.

# Original tuple
T1 = (10, 20, 30, 40)
# Tuple to be concatenated
T2 = ('one', 'two', 'three', 'four')
# Updating the tuple using the concatenation operator
T1 = T1 + T2
print(T1)
#(10, 20, 30, 40, 'one', 'two', 'three', 'four')

#Updating Tuples Using Slicing
# Syntax: sequence[start:stop:step] #step is the interval between elements 

# Original tuple
T1 = (37, 14, 95, 40)
# Elements to be added
new_elements = ('green', 'blue', 'red', 'pink')
# Extracting slices of the original tuple
# Elements before index 2
part1 = T1[:2]  
# Elements from index 2 onward
part2 = T1[2:]  
# Create a new tuple 
updated_tuple = part1 + new_elements + part2
# Printing the updated tuple
print("Original Tuple:", T1)
print("Updated Tuple:", updated_tuple)
# Original Tuple: (37, 14, 95, 40)
# Updated Tuple: (37, 14, 'green', 'blue', 'red', 'pink', 95, 40)


#Updating Tuples Using List Comprehension

T1=(10,20,30,40)

list_T1=list(T1)    # Converting the tuple to a list

update_list=[item +100 for item in list_T1] # Using list comprehension 

updated_tuple=tuple(update_list)    # Converting the updated list back to a tuple

print( "Original Tuple ",T1)
print("Updated tuple ", updated_tuple)
# Original Tuple: (10, 20, 30, 40)
# Updated Tuple: (110, 120, 130, 140)

#Updating Tuples Using append() function

T1=(10,20,30,40)

list_T1=list(T1)     # Converting the tuple to a list

new_elements=[50,60,70]
for i in new_elements:
    list_T1.append(i)

updated_tuple=tuple(list_T1)
print( "Original Tuple ",T1)
print("Updated tuple ", updated_tuple)
# Original Tuple: (10, 20, 30, 40)
# Updated Tuple: (10,20,30,40,50,60,70)


#---------Unpack Tuple Items------
#The term "unpacking" refers to the process of parsing(assigining) tuple items in individual variables.

tup1 = (10,20,30)
x, y, z = tup1
print ("x: ", x, "y: ", "z: ",z)
#x: 10 y: 20 z: 30      #That's how the tuple is unpacked in individual variables.

#ValueError While Unpacking a Tuple
tup1 = (10,20,30)
# x, y = tup1         #ValueError: too many values to unpack (expected 2)
# x, y, p, q = tup1   #ValueError: not enough values to unpack (expected 4, got 3)


#Unpack Tuple Items Using Asterisk (*)
tup1 = (10,20,30)
x, *y = tup1
print ("x: ", "y: ", y)
#x:10 y:[20,30]
# he first value in tuple is assigned to "x", and rest of items to "y" which becomes a list.

tup1 = (10,20,30, 40, 50, 60)
x, *y, z = tup1
print ("x: ",x, "y: ", y, "z: ", z)
#x:10 y:[20,30,40,50] z:60

tup1 = (10,20,30, 40, 50, 60)
*x, y, z = tup1
print ("x: ",x, "y: ", y, "z: ", z)
#x:[10,20,30,40] y:50 z:60


#------------Loop Through Tuple Items-----

# #with For Loop
# syntax:
# for item in tuple:
    # Code block to execute

# tup1=(10,20,30,40,50,60)

# for i in tup1:
#     print(i, end=" ")

#10 20 30 40 50 60

# with While Loop
#syntax: 
# while condition:
   # Code block to execute

# tup1=(10,20,30,40,50)
# i=0
# while i < len(tup1):
#      print(tup1(i))
#     i +=1

# 10
# 20
# 30
# 40
# 50

print()
#--------Joining Tuples in Python=-----------
#refers to combining the elements of multiple tuples into a single tuple.
#Joining tuples does not modify the original tuples but creates a new tuple containing the combined elements.

#Concatenation ("+") Operator

T1=(10,20,30,40)
T2=("one", "two", "three")

joined_tuple=T1+T2
print("Joined Tuple: ", joined_tuple)

#Using List Comprehension

joined_tuple2=[i for subtuple in [T1,T2] for i in subtuple]
print("joined using coprehension: ", joined_tuple2)

#Using extend() Function
#used to append elements from an iterable (such as another list) to the end of the list. This function modifies the original list in place, adding the elements of the iterable to the end of the list.

#We can join tuples using the extend() function by temporarily converting the tuples into lists, performing the joining operation as if they were lists, and then converting the resulting list back into a tuple.

L1=list(T1)
L2=list(T2)
L1.extend(L2)
T1=tuple(L1)

print("Joined using Extend :", T1)

# using sum() Function
# this method only works for tuples containing numeric elements.
# syntax : result_tuple = sum((tuple1, tuple2), ())     #empty tuple () as the starting value.

T3=sum((T1,T2), ())
print("new tuple: ",T3)

#using for Loop
# appending each element to another tuple with the "+=" operator.
# we are iterating over each element in tuple T2, and for each element, we are appending it to tuple T1, effectively joining the two tuples

for t in T2:
    T1+=(t,)

print(T1)


# ---------------Tuple Methods----------

#  built-in methods
# tuple.count(obj) #Returns count of how many times obj occurs in tuple

Tup1=(25,10,15,26,35,35,10)

print(Tup1.count(10))   
#2
print(Tup1.count(100))
#0

#Even if the items in the tuple contain expressions, they will be evaluated to obtain the count.
tup1 = (10, 20/80, 0.25, 10/40, 30, 10, 55)
print ("Tup1:", tup1)
c = tup1.count(0.25)
print ("count of 10:", c)

# Tup1: (10, 0.25, 0.25, 0.25, 30, 10, 55)
# count of 10: 3


#tuple.index(obj)   #Returns the lowest index in tuple that obj appears
#epresenting the index of the first occurrence of "obj".
Tup1=(25,10,15,26,35,35,10)
print(Tup1.index(15))
#2
print(Tup1.index(35))
#4



#-------What is NamedTuple?------
# a namedtuple() is a subclass of tuple that allows you to create tuples with named fields. 
# Meaning, you can access the elements of the tuple using fieldnames instead of just numerical indices. 
# It is part of the collections module in Python.

# Syntax: 
from collections import namedtuple
 
# # Define a namedtuple
# Point = namedtuple('typename', fieldnames )

# Type Name: The typename is the name of the namedtuple class. It is a string that represents the name of the tuple type.
# Field Names: The field names are the names of the elements in the tuple. They are defined as a list of strings.

vertex=namedtuple("Vertex",['x','y'])
v=vertex(10,200)

print(v)    #=> Vertex(x=10, y=200)

print("vertex-1", v.x)
print("vertex-2", v.y)



#Access NamedTuple Fields

# Accessing by Indexing − You can access the fields using their index, just like a regular tuple.
# Accessing by keyname − You can also access the fields using their key names, similar to a dictionary.
# Accessing Using getattr() − You can use the getattr() function to access the fields by name.

Poiny=namedtuple("Poiny", ['x', 'y'])

p=Poiny(10,20)
#index
print(p[0])
print(p[1])

#keyname
print(p.x)
print(p.y)

#getattr()
print(getattr(p,'x'))
print(getattr(p,'y'))


#--------NamedTuple Methods----------

# The _fields() method
# The_fields() method is used to access the field names of the namedtuple. It doesn't need any arguments and returns a tuple of the field names.

print(p._fields)


#The _replace() method
# used to create a new instance of the namedtuple with one or more fields replaced with new values. It takes keyword arguments where the keys are the field names and the values are the new values to be assigned.

p2=p._replace(x=23)

print(p2.x)
print(p2.y)


# The _asdict() method
# used to convert the namedtuple into a regular dictionary.

d=p._asdict()
print(d)



# The _make() method
# The _make() method is used to create a new instance of the namedtuple from an iterable (like a list or a tuple).

p3=Poiny._make([30,40])

print(p3.x)
print(p3.y)


# The ** (double star) operator
# The ** (double star) operator is used to unpack the fields of the namedtuple into keyword arguments. This can be useful when you want to pass the fields of a namedtuple to a function that accepts keyword arguments.

import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student',
                                 ['name', 'age', 'DOB'])

# Adding values
S = Student('farhan', '23', '2541997')

# initializing iterable
li = ['nishu', '19', '411997']

# initializing dict
di = {'name': "ravi", 'age': 24, 'DOB': '1391997'}

# using ** operator to return namedtuple from dictionary
print("The namedtuple instance from dict is  : ")
print(Student(**di))

# The namedtuple instance from dict is  :
# Student(name='ravi', age=24, DOB='1391997')


#exercise

# 1.Python program to find unique numbers in a given tuple −

T1 = (1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2)
T2=()

for i in T1:
   if i not in T2:
    T2=T2+(i,)

print  ("originL : ", T1)
print("NEW UNIQUE :", T2)

# 2.Python program to find sum of all numbers in a tuple −

T1=(10,50,30,10)
sumval=0
for i in T1:
   sumval+=i
print("Total Sum is : ", sumval)

# 3.Python program to create a tuple of 5 random integers −

import random

tz=()

for i in range(5):
   x=random.randint(0,100)
   tz+=(x,)

print(tz)










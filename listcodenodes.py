#--------LIST---
#1-built-in data types
#A Python list is a sequence of "comma separated items", "enclosed in square brackets [ ]".
#  The items in a Python list need not be of the same data type.
#List is an ordered collection of items. 
# Each item in a list has a unique position index, starting from 0.
#A list in Python is similar to an array in C, C++ or Java.

#A Python list is mutable. Any item from the list can be accessed using its index, and can be modified. 
# One or more objects from the list can be removed or added. 
# A list may have same item at more than one index positions.



# list1=["Kalayn", "Kapil", 45,15,147.25, True, False]
# list2=[1,2,3,4,5]

# #accessing the list using Square Bracket [] & also range operator { [start:stop] }
# print(list1[1])
# print(list1[2:4])
# print(list1[-1])
# print(list1[-4:-1])


# #Update the List using index  and Append()
# list1[2]="Arjun"
# print(list1)

# list1.append("Nachiket")
# print(list1)

# list1.insert(2, 'Chemistry')

# list1.insert(-1, 'Pass')

# list1.extend(list2)

# print("Extended list:", list1)

# Remove element in list using del list[]  and remove(element)
# del list1[-2]
# print(list1)

# list1.remove(True)  #remove true object
# print(list1)

# print(list1.pop(-2))

# #clear the list
# list1.clear()
# print(list1)

# In Python, List is a sequence. Hence, we can concatenate two lists with "+" operator and 
# concatenate multiple copies of a list with "*" operator.
#  The membership operators "in" and "not in" work with list object.

# #conctenation
# print([1,2,3] + [4,5,6])
# #repetation
# print(["HI"]*3)
# #membership
# print(3 in [1,2,3])

# #Indexing, Slicing, and Matrixes
# L=[1,2,3]

# print(L[2])     #offset start at zero
# print(L[-2])    #Negative: count stat from right
# print(L[1:])    # slcicing fetches sections


#methods


# #length of list
# print(len(list1))


##Loops in List: refers to iterating over each element within a list
 
# for i in list1:
#     print(i)

# i=0
# while i <=(len(list1)-1):
#     print(list1[i])
#     i+=1

# ind=range(len(list1))

# for i in ind:
#     print(f'list1[{i, list1[i]}]')

# #Iterate using List Comprehension
# #new_list = [expression for item in iterable if condition]
# list3=[num**2 for num in list2]
# print(list3)

# #Iterate using the enumerate() Function\
# for index, num in enumerate(list2):
#     print(index, num)

# list4=[num for num in list2 if num %2==0]
# print(list4)

# chars = [ char for char in 'TutorialsPoint' if char not in 'aeiou']
# print (chars)
# strname="my name in kalyan pate"
# vowels=[v for v in strname if v in "aeiou"]
# print(vowels)

# squrs=[xx*xx for xx in list2]
# print(squrs)

##Sorting Lists in Python
#This can be achieved using the built-in sorted() function or by calling the sort() method on the list itself, 
# both of which modify the original list or return a new sorted list depending on the method used.

# lst1=[4,9,3,7,2,1,8,99,2,4]

#sort() method :
#list_name.sort(key=None (optional), reverse=False (optional))
# lst1.sort()
# print(lst1)

#sorted() Method : returns a new sorted list, leaving the original iterable unchanged.
#sorted(iterable, key=None (optional), reverse=False (optional))
# lst2=sorted(lst1,reverse=True)
# print(lst2)

#Sorting List Items with Callback Function


#------------Copying a List in Python ----------------------------

# 1. Shallow Copy on a Python List
#A shallow copy in Python creates a new object, but instead of copying the elements recursively, 
# it copies only the references to the original elements. This means that the new object is a separate entity 
# from the original one, but if the elements themselves are mutable, 
# changes made to those elements in the new object will affect the original object as well.

# import copy
# lst1=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]  #original
# lst2=copy.copy(lst1)    #shallow copy
# lst2[0][0]=78
# print(lst1)
# print(lst2)
# # print(f'lst1:{lst1} and lst2: {lst2}')

# 2.Deep Copy on a Python List
#A deep copy in Python creates a completely new object and recursively copies all the objects referenced by the original object. 
# This means that even nested objects within the original object are duplicated,
#  resulting in a fully independent copy where changes made to the copied object do not affect the original object, and vice versa.

# lst3=copy.deepcopy(lst1)    #shallow copy
# lst3[0][0]=100
# print(lst1)
# print(lst3)

# # 3.Copying List Using Slice Notation
# lst4 =lst1[1:3]
# print(lst4)

# #4.Copying List Using the list() Function
# #The list() function in Python is a built-in function used to create a new list object. 
# lst5=list(lst1)
# print(lst5)

#-----------Join Lists in Python---------------
# It refers to combining the elements of multiple lists into a single list
#using various methods, such as concatenation, list comprehension, 
# or using built-in functions like extend() or + operator.

# L1 = [10,20,30,40]
# L2 = ['one', 'two', 'three', 'four']

# #1. "+" Concatenation
# # create a new list containing all the elements from both lists.
# Lst1=L1+L2
# print(Lst1)

# #2. Using List Comprehension :
# # Generate new lists by applying an expression to each item in an existing iterable, such as a list, tuple, or range.
# lst2=[n*2 for n in L1]
# print(lst2)

# #3. Using append() Function
# for i in L2:
#     lst2.append(i)
# print(lst2)

# # 4 Using extend() Function
# # This function modifies the original list in place, adding the elements of the iterable to the end of the list.

# L1.extend(L2)
# print(L1)


#--------------Python List Methods------------------

# print(dir([]))
# print(help([].append))

# ------------Python List Exercise ---------
# 1.Python program to find unique numbers in a given list.
L1 = [1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2]
#1
L2=[]
# L3=[L2.append(i) for i in L1 if i not in L2]
# print(L3)

#2.
# for i in L1:
#     L2.append(i)
# print(L2)

# Exercise 2 :Python program to find sum of all numbers in a list.
# sum=0
# for i in L1:
#     sum +=i
# print(sum)

# Exercise 3:Python program to create a list of 5 random integers.
import random

for i in range(5):
    x =random.randint(0,100)
    L2.append(x)
print(L2)








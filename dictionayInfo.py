#Dictionay:
# a dictionary is a built-in data type that stores data in key-value pairs.
# It is an unordered, mutable, and indexed collection. 
#  Each key in a dictionary is unique and maps to a value. 
# Each key-value pair is separated by a comma and enclosed within curly braces {}. 
# The key and value within each pair are separated by a colon (:), forming the structure key:value.



rto_no={"MH":"Maharashtra", "BH":"Bharat", "TN":"Telanganga","KA":"Karnataka"}
print(rto_no)
# Only a number, string or tuple can be used as key. All of them are immutable. You can use an object of any type as the value. 
relation_var={("india", "USA"):"Countries", ("Delhi", "New York"):"Capitals"}
print(relation_var)

# python doesn't accept mutable objects such as list as key, and raises TypeError.
# list_var={[1,2,3]:"Numbers"}
# print(list_var)

# You can assign a value to more than one keys in a dictionary, but a key cannot appear more than once in a dictionary.
d2 = {"Fruit":"Banana","Flower":"Rose", "Fruit":"Mango", "Flower":"Lotus"}
print (d2)


# Creating a Dictionary
# by placing a comma-separated sequence of key-value pairs within curly braces {}, with a colon : separating each key and its associated value. 
# Alternatively, you can use the dict() function.

tup_Var =dict (name="kalyan", age=21, area="Pune")
print(tup_Var)


# Accessing Dictionary Items
# You can access the value associated with a specific key using square brackets [] or the get() method −

print(d2["Flower"])
print(tup_Var["name"])

# get()
print(tup_Var.get("age"))


# Modifying Dictionary Items
# You can modify the value associated with a specific key or add a new key-value pair

tup_Var["name"]="Kapil"
tup_Var["Comany"]="Pharma"
tup_Var["Month"]="Feb"
print(tup_Var)


# Removing Dictionary Items
# You can remove items using the del statement, the pop() method, or the popitem() method

del tup_Var["age"]
print(tup_Var)

tup_Var.pop("Comany")
print(tup_Var)

tup_Var.popitem()
print(tup_Var)



# terating Through a Dictionary
# You can iterate through the keys, values, or key-value pairs in a dictionary using loops 

# Iterating through keys
for key in rto_no:
    print(f"key: {key} = Value : {rto_no[key]}")

# Iterating through values
for value in rto_no.values():
    print(f"Value : {value}")


# Iterating through key-value pairs
for key, value in rto_no.items():
    print(f"{key}: {value}")

# Properties of Dictionary Keys
# Dictionary values have no restrictions. They can be any arbitrary Python object, either standard objects or user-defined objects. 
# no duplicate key is allowed.

# Keys must be immutable. Which means you can use strings, numbers or tuples as dictionary keys but something like ['key'] is not allowed.

# Python Dictionary Operators

# Access Dictionary Items

# [key]
print(rto_no["BH"])

# get()
# We can access dictionary items using the get() method by specifying the key as an argument.
#  If the key exists in the dictionary, the method returns the associated value; otherwise, 
# it returns a default value, which is often None unless specified otherwise.


print(rto_no.get("MH"))
#  the get() method doesn't raise error if the key is not found; it return None −
print(rto_no.get("UP"))
# Default value provided if key is not found
print(rto_no.get("UP", "Uttar Pradesh"))

# Access Dictionary Keys
# They must be of an immutable data type, such as strings, numbers, or tuples.
# keys() method, which returns a view object containing all the keys in the dictionary.

print(rto_no.keys())


# Access Dictionary Values
# []
# get()
# values
print(rto_no.values())

# Access Dictionary Items Using the items() Function
#  return a view object that displays a list of a dictionary's key-value tuple pairs.
print(rto_no.items())

# using loop 
for key, value in rto_no.items():
    print(f"{key}:{value}")

# -------------Change Dictionary Items-------------
# This can involve updating the value of an existing key, adding a new key-value pair, or removing a key-value pair from the dictionary.
person={'name':'kalyen', 'age':21, 'city':'Pune'}
print(person)
# Modifying 
person["age"]=26
print(person)

# Updating Multiple Dictionary Values
# The update() method adds the key-value pairs from the provided dictionary or iterable to the original dictionary, overwriting any existing keys with the new values if they already exist in the original dictionary.
person.update({'age':27, 'city':'Delhi'})
print(person)

# Adding New Key-Value Pairs
person['dept']="HR"
print(person)

# setdefault()
#  setdefault() method to add a new key-value pair to a dictionary if the key does not already exist.
person.setdefault('role',"developer")
print(person)


# Removing 
# 1.del
del person["age"]
print(person)
# 2.pop()
person.pop("role")
print(person)
# 3. popitem() :popitem() method as well to remove the last key-value
person.popitem()
print(person)


# --------------Add Dictionary Items-----------
# Using square brackets
# Using the update() method
# Using a comprehension
# Using unpacking
# Using the Union Operator
# Using the |= Operator
# Using setdefault() method
# Using collections.defaultdict() method

# -----------Remove Dictionary Items----------

# using the del keyword
# using the pop() method
# using the popitem() method

# using the clear() method  :to remove all items from a dictionary. It effectively empties the dictionary, leaving it with a length of 0.
person.clear()
print(f"After Clear():{person}")
# using dictionary comprehension

student_info = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}

# Removing items based on conditions
keys_to_remove = ["age", "major"]
for key in keys_to_remove:
    student_info.pop(key, None)

print(student_info)  

# --------View Objects--------------
#  items(), keys(), and values() methods of dict class return view objects.


# -----------Loop Through Dictionaries--------
# Using a for Loop
# Using dict.items() method
# Using dict.keys() method
# Using dict.values() method

# ----------------------Copy Dictionaries------------
# Copying dictionaries in Python refers to creating a new dictionary that contains the same key-value pairs as the original dictionary.

# Shallow Copy
# When you perform a shallow copy, a new dictionary object is created, but it contains references to the same objects that the original dictionary references.

# This is useful when you want to duplicate the structure of a dictionary without duplicating the nested objects it contains.

# This can be done using the copy() method or the dict() function as shown below −

# Example: Using the copy() Method
# In the following example, we can see that changing the "age" in the shallow copy does not affect the original.

# However, modifying the list in the shallow copy also affects the original because the list is a mutable object and only a reference is copied

original_dict = {"name": "Alice", "age": 25, "skills": ["Python", "Data Science"]}
shallow_copy = original_dict.copy()

# Modifying the shallow copy
shallow_copy["age"] = 26
shallow_copy["skills"].append("Machine Learning")

print("Original dictionary:", original_dict)
print("Shallow copy:", shallow_copy)


# Similar to the copy() method, the dict() method creates a shallow copy as shown in the example below −
original_dict = {"name": "Bob", "age": 30, "skills": ["Java", "C++"]}
shallow_copy = dict(original_dict)

# Modifying the shallow copy
shallow_copy["age"] = 31
shallow_copy["skills"].append("C#")

print("Original dictionary:", original_dict)
print("Shallow copy:", shallow_copy)


# Deep Copy:using the deepcopy() function in the copy module.
# A deep copy creates a new dictionary and recursively copies all objects found in the original dictionary. 
# As a result, changes made to the deep copy do not affect the original dictionary and vice versa.
import copy

original_dict = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Data Science"],
    "education": {
      "degree": "Bachelor's",
      "field": "Computer Science"
   }
}

# Creating a deep copy
deep_copy = copy.deepcopy(original_dict)

# Modifying the deep copy
deep_copy["age"] = 26
deep_copy["skills"].append("Machine Learning")
deep_copy["education"]["degree"] = "Master's"

# Retrieving both dictionaries
print("Original dictionary:", original_dict)
print("Deep copy:", deep_copy)


# --------Nested Dictionaries--------

student={'id':1001, 'name':'kalyan', 'subjects':{'Eng':'English', 'Math':'Mathematics'}}

# Accessing 
print(student["id"])
print(student['subjects']['Eng'])

# Adding 
# Adding a new key-value pair to Alice's nested dictionary
student["subjects"]["BIO"] = "Biology"

# get() Method
# Deleting 
# Iterating 



# ------------Methods--------


# ------------Exercises--------
# 1.Python program to create a new dictionary by extracting the keys from a given dictionary.

# 2.Python program to convert a dictionary to list of (k,v) tuples.

# 3.Python program to remove keys with same values in a dictionary.

# Dictionary Exercise Programs
# Python program to sort list of dictionaries by values

# Python program to extract dictionary with each key having non-numeric value from a given dictionary.

# Python program to build a dictionary from list of two item (k,v) tuples.

# Python program to merge two dictionary objects, using unpack operator.

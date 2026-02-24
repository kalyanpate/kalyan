#set
# unordered collection of unique elements
# Unlike lists or tuples, sets do not allow duplicate values i.e. each element in a set must be unique. 
# Sets are mutable, meaning you can add or remove items after a set has been created.
# Sets are defined using curly braces {} or the built-in set() function
# 
# 

my_set={1,2,5,3,5}
print(my_set)

#set conversion
my_list=[1,2,5,6,8]
my_set1=set(my_list)
print(my_set1)


# Sets in Python are unordered collections of unique elements. If you try to create a set with duplicate elements, duplicates will be automatically removed
my_set={1,2,8,6,32,1,4,8,62,1,4}
print(my_set)

# Sets can contain elements of different data types, including numbers, strings, and even other sets (as long as they are immutable) 
my_set={1,2,5,"hello", 1.011}
print(my_set)

# ets support various basic operations that is used to manipulate their elements. These operations include adding and removing elements, checking membership, and performing set-specific operations like union, intersection, difference, and symmetric difference.

# Adding using add() function
my_set.add(14621)
print(my_set)

#Remove  using the remove() function

my_set.remove("hello")
print(my_set)


#  discard() function to remove an element from the set if it is present. Unlike remove(), discard() does not raise an error if the element is not found in the set −
# my_set.remove("Kalyan")
my_set.discard("Kalyan")
print(my_set)

# Membership 
print(2 in my_set)
print("hello" not in my_set)

# Set Operations
# Union − It combine elements from both sets using the union() function or the | operator.

# Intersection − It is used to get common elements using the intersection() function or the & operator.

# Difference − It is used to get elements that are in one set but not the other using the difference() function or the - operator.

# Symmetric Difference − It is used to get elements that are in either of the sets but not in both using the symmetric_difference() method or the ^ operator.

# Set Comprehensions

my_set={x*2 for x in my_set if x %2==0}

print(my_set)

# Nested Set Comprehensions
my_set={(x,y) for x in range(1,3) for y in range(1,3)}
print(my_set)

# Frozen Sets
# a frozen set is an immutable collection of unique elements
# using the frozenset() functio

my_set1=frozenset(my_list)
# my_set1.add(12)
print(my_set1)


#Access element
# 1. using loop, comprehsnsion
for i in my_set:
    print(i)

org_set={1,2,3,4,5,6,7,8,9}
is_sub={1,2,3}.issubset(org_set)
print(is_sub)

# Adding element
# 1. Add(elemtn) -for single elemtn
org_set.add(152)
print(f"add(): {org_set}")

# 2. update(obj) -for multiple element
org_set.update([100,200])
print(f"update(): {org_set}")

# 3.Union Operator (|)
lang1={"java", "Python"}
lang2={"HTML", "CSS", "JS"}
lang3=lang1.union(lang2)
print(lang3)

# Remove elemtnet
# 1. remove
lang3.remove("java")
# 2.discard
lang3.discard("Kalyan")
# 3. pop()
lang3.pop()
print(lang3)
# 4. clear() -empty the set]
lang3.clear()
print(lang3)

# 5. difference_update()- remove items that exist in both sets
s1={1,2,3,4,5}
s2={2,4,5,6}
s1.difference_update(s2)
print(s1)

# 6. ^ or symmetric_difference()-remove items that exist in either of two sets,
s1={1,2,3,4,5}
s2={2,4,5,6}
s3= s1 ^ s2
print(s3)

# 7. intersection_update() -remove uncommon items between two sets
s1={1,2,3,4,5}
s2={2,4,5,6}
s1.intersection_update(s2)
print(s1)

# 8. intersection() -it returns a new set object that consists of items common to existing sets
s1={1,2,3,4,5}
s2={2,4,5,6}
s3=s1.intersection(s2)

# 9. symmectric_difference_update()
s1={1,2,3,4,5}
s2={2,4,5,6}
s1.symmetric_difference_update(s2)
print(s1)

# 10. symmetric_difference()-returns a new set object that holds all the items from two sets minus the common items.
s1={1,2,3,4,5}
s2={2,4,5,6}
s3=s1.symmetric_difference(s2)
print(s3)

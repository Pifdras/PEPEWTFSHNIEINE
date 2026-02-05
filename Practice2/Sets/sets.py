# A set is a collection which is unordered, unchangeable*, and unindexed.
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Sets cannot have two items with the same value.
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# True and 1/False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2, False, 0}
print(thisset)

# To determine how many items a set has, use the len() function.
print(len(thisset))

# Set items can be any data type and even mix it
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}
print(set1), print(set2), print(set3), print(set4)

# From Python's perspective, sets are defined as objects with the data type 'set':
myset = {"apple", "banana", "cherry"}
print(type(myset))

#It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
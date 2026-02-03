mylist = ["apple", "banana", "cherry"]

thislist = ["apple", "banana", "cherry"]
print(thislist)

# allow duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# len() to determine how many elements in list
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# Lists can be any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# And also can contain different data types
list1 = ["abc", 34, True, 40, "male"]

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# We can also create list using list()
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

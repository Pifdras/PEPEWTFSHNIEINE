#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#Example:
#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
#Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#With list comprehension you can do all that with only one line of code:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#The syntax
#newlist = [expression for item in iterable if condition == True]

#The condition is like a filter that only accepts the items that evaluate to True.

newlist = [x for x in fruits if x != "apple"]

#You can use the range() function to create an iterable:

newlist = [x for x in range(10)]
newlist = [x for x in range(10) if x < 5]

#The expression is the current item in the iteration, but it is also the outcome, 
#which you can manipulate before it ends up like a list item in the new list:
newlist = [x.upper() for x in fruits]

newlist = ['hello' for x in fruits]

newlist = [x if x != "banana" else "orange" for x in fruits]
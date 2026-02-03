# Membership operators are used to test if a sequence is presented in an object:

# Operator      Description                                                         Example
# in            Returns True if a sequence with the specified                       x in y
#               value is present in the object
# not in        Returns True if a sequence with the specified                       x not in y
#               value is not present in the object


fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)


fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)


text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)
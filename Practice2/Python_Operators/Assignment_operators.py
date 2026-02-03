#Assignment operators are used to assign values to variables:

#Opeartor   Example 

# =         x = 3  mean  x = 3 

x = 5
print(x)

# +=        x += 3  mean  x = x + 3

x = 5
x += 3
print(x)

# -=        x -= 3  mean  x = x - 3

x = 5
x -= 3
print(x)

# *=        x *= 3  mean  x = x * 3

x = 5
x *= 3
print(x)

# /=        x /= 3  mean  x = x / 3

x = 5
x /= 3
print(x)

# %=        x %= 3  mean  x = x % 3

x = 5
x//=3
print(x)

# //=       x //= 3  mean  x = x // 3

x = 5
x//=3
print(x)

# **=       x **= 3  mean  x = x ** 3

x = 5
x **= 3
print(x)

# &=        x &= 3  mean  x = x & 3 AND

x = 5
x &= 3
print(x)

# |=        x |= 3  mean  x = x | 3 OR

x = 5
x |= 3
print(x)

# ^=        x ^= 3  mean  x = x ^ 3 XOR

x = 5
x ^= 3
print(x)

# >>=       x >>= 3  mean  x = x >> 3  Right bit shift by 3  division by 2^3 

x = 5
x >>= 3
print(x)

# <<=       x <<= 3  mean  x = x << 3  Left bit shift by 3  multiplication by 2^3

x = 5
x <<= 3
print(x)

# :=        print(x := 3)  mean  x = 3
#                                print(x)

#The count variable is assigned in the if statement, and given the value 5:

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")
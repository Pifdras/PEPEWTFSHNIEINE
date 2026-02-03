# Bitwise operators are used to compare (binary) numbers:

# Operator   Name                  Description                                              Example
# &          AND                   Sets each bit to 1 if both bits are 1                    x & y
# |          OR                    Sets each bit to 1 if one of two bits is 1               x | y
# ^          XOR                   Sets each bit to 1 if only one of two bits is 1          x ^ y
# ~          NOT                   Inverts all the bits                                     ~x
# <<         Zero fill left shift  Shift left by pushing zeros in from the right and        x << 2
#                                  let the leftmost bits fall off
# >>         Signed right shift    Shift right by pushing copies of the leftmost bit        x >> 2
#                                  in from the left, and let the rightmost bits fall off

print(6 & 3)
#The binary representation of 6 is 0110
#The binary representation of 3 is 0011
#Then the & operator compares the bits and returns 0010, which is 2 in decimal.



print(6 | 3)
#The binary representation of 6 is 0110
#The binary representation of 3 is 0011
#Then the | operator compares the bits and returns 0111, which is 7 in decimal.



print(6 ^ 3)
#The binary representation of 6 is 0110
#The binary representation of 3 is 0011
#Then the ^ operator compares the bits and returns 0101, which is 5 in decimal.
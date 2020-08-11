"""
write a program  that takes an integer and
sets the n-th bit in the binary representation of
that integer

For instance, the binary representation of 6 is:
    110

The least significant bit is the bit on the far right
of the binary representation and the most significant
bit is the bit on the far left. We order the bits as

b2, b1, b0
1   1   0

For our function, if we set the 0th bit, we should obtain
the binary representation:
    1 1 1

==============

Set (make ==1 ) 0th bit of 6 (in binary representation 110)
Expected result: 111

1 1 0 |   # 6
0 0 1     # 1 << 0
-----
1 1 1



"""

def set_bit(num, n):
    return bin(num | 1 << n)

print(set_bit(6, 0))
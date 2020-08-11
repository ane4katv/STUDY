"""
write a program  that takes an integer and
unsets the n-th bit in the binary representation of
that integer

For instance, the binary representation of 6 is:
    110

The least significant bit is the bit on the far right
of the binary representation and the most significant
bit is the bit on the far left. We order the bits as

b2, b1, b0
1   1   0

For our function, if we unset the 1st bit, we should obtain
the binary representation:
    1 0 0
~ "not operation", turns 0 -> 1, 1 -> 0

(1 << 0) 0   0   0   0   0   0   0   1
(1 << 2) 0   0   0   0   0   1   0   0

~(1 << 0) 1  1   1   1   1   1   1   0
~(1 << 2) 1  1   1   1   1   0   1   1

=======================================

1 1 0    # 6
1 0 1 &    # ~(1 << 1) AND-ing all 1s and only one 0 (n-th position)
-----
1 0 0

"""

# mask with 00000001 where 1 shifted to nth position
# given int & mask (will have 0 only on nth position, so it is guarantee to be UNSET!)


def unset_bit(num, n):
    # return num & ~(1 << n) # this will AND num and flipped 00000001 with 1 shifted to n position!
    print("original", bin(num))
    return num ^ (1 << n)


print('6, 0', bin(unset_bit(6,0)))
print('6, 1', bin(unset_bit(6,1)))
print('6, 2', bin(unset_bit(6,2)))








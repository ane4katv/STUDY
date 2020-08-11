"""
write a program that takes an integer and tests whether the n-th bit
in the binary representation of that integer
is set or not.

bit set means == 1
not set means == 0

For instance, the binary representation of 6 is: 110

The least significant bit is the bit on the far right
of the binary representation and the most significant
bit is the bit on the far left.

So we order the bits from right to left

b2, b1, b0
1   1   0

For our function, if we check the 0th bit, we should obtain
"False" as the binary value at b0 is 0.

Alternatively, if we check the 1st bit, we should obtain
"True" as the binary value at b1 is 1.
=============================================================
Shift Operator

num 1
0   0   0   0   0   0   0   1

shifting it 1 time left 1 << 1:
0   0   0   0   0   0   1   0

shifting it 2 times left 1 << 2:
0   0   0   0   0   1   0   0

Ex.: Is the 2nd bit set? ***** 1 << 2 (1 shifted left 2 times) ****
6:  1   1    0
    1   0    0   (represents 1 << 2 (1 shifted over by 2) counting from right, starting with 0, all other nums are zeros)
    ----------
    1   0   0   (we got 1, it means second bit is set)

Ex.: Is the 0th bit set? ***** 1 << 0 (1 shifted left 0 times) ****
6:  1   1    0
    0   0    1   (represents 1 << 0 (1 shifted over by 0)
    ----------
    0   0   0   (we got 0, it means 0th bit is NOT set)

shifted by n result AND  given number => 0 or anything else
0   : n-th bit is NOT set
anything else   : n-th bit IS set

"""

def is_nth_bit_set(num, n):

    if num & (1 << n): # if num and mask (where 1 shifted to n position)
        return True
    else:
        return False

print(is_nth_bit_set(6,2))

print(is_nth_bit_set(6,0))
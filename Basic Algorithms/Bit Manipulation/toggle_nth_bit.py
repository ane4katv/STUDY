"""
write a program  that takes an integer and toggles the n-th bit
in the binary representation of that integer

For instance, the binary representation of 6 is: 110
The least significant bit is the bit on the far right of the binary representation
and the most significant bit is the bit on the far left.
We order the bits as
b2, b1, b0
1   1   0
For our function, if we toggle the 0th bit,
we should obtain the binary representation: 1 1 1
If we again toggle the 0th bit from the above representation we obtain 1 1 0
"""

# 110
# 001

def toggle_bin(num, n):
    return num ^ (1 << n)

print(bin(10))
print(bin(toggle_bin(10,0)))
print(bin(toggle_bin(10,1)))
print(bin(toggle_bin(10,2)))


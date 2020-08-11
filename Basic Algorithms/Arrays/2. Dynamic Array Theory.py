# Dynamic Array Theory

"""A dynamic array is an array with a big improvement: automatic resizing.
 One limitation of arrays is that they're fixed size,
 meaning you need to specify the number of elements
 your array will hold ahead of time.
 A dynamic array expands as you add more elements"""

# NO need to specify array size beforehand
# That extra space eventually runs out if keep adding elements

import sys
#set n
n = 10
# set empty list
data = []
for i in range(n):

# number of elements
    a = len(data)
#actual size of bytes
    b = sys.getsizeof(data)
    print(f' *** Length: {a} & Size of bytes: {b} ***')
#Increase length by one so
    data.append(n)


# Theoretical Implementation
# 1. Given array A
# 2. Create array B with higher capacity (common rule is to double capacity of existing array)
# 3. Store elements of A in B (set references)
# 4. Reassign reference A to new array (B became A now)

""" """


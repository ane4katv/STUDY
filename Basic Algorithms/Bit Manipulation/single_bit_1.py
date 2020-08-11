"""
Given a number, write a function that determines
if the number has exactly one bit set.

Return True if number has exactly one bit set to 1;
False if it has any other number of bits set to 1.

Sometimes, you'll hear this problem framed in terms of powers of two:
"Write a function that determines if a number is a power of two."
All powers of two have exactly one bit set, so these questions are identical.

1. extract 1 from number. It will:
                        - clear least significant bit (reverse it)
                        - change all bits to the right to '1' (reverse it)
                        - leave all bits to the left unchanged

   - 0010 0000
     0000 0001
     ----------
     0001 1111

2. number & (number - 1) will give us all zeros in changed part
    if there are no more '1' in unchanged part it will be == 0 too,
    so there was only one bit set (== 1)

    & 0010 0000
      0001 1111
      ----------
      0000 0000

"""


def single_bit_set(number):
    if number == 0:
        return False
    return number & (number - 1) == 0


print((single_bit_set(17)))

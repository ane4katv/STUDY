"""
Write a program to determine if a given number is even or odd.
Do not use Modulo Operator (%)

==============================================================

    4   2   1
1   0   0   1
2   0   1   0
3   0   1   1
4   1   0   0
5   1   0   1
6   1   1   0
7   1   1   1

- All even numbers above end with "1"
- Adding 1 to even number will result an odd number
- Adding any number of even numbers will result even number


Adding (ANDing) number "1" gives "0" or "1":
    0: 1 was added to even
    1: 1 was added to odd

ex. odd
1:  0   0   1   &
    0   0   1
    ---------
    0   0   1
ex. even
6:  1   1   0   &
    0   0   1
    ---------
    0   0   0



 """

def is_even_odd(num):
    if num & 1 == 0:
        return "even"
    else:
        return "odd"

print(is_even_odd(-2))




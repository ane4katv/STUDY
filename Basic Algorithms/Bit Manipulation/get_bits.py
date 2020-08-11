# Pull out 4,5,6 bits from the integer number
# input the integer number
number = int(input('Input number: '))
print(bin(number))

# filter for 4,5,6 bits
number &= 0b1110000
print(bin(number))

# shift 4 digits to the right
number >>= 4
print(bin(number))
print('number = ', number)



# Multiply 0-5 bits of the first number by 0-7 bits of the second number
x = int(input('x = '))
y = int(input('y = '))

# filter for 0-5 bits
x &= 0b11111

# filter for 0-7 bits
y &= 0b1111111

# multiply
z = x*y

print('x = ', x, bin(x))
print('y = ', y, bin(y))
print('z = ', z, bin(z))
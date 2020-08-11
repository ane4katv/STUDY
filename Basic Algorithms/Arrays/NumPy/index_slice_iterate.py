"""
Index, Slice and Iterate

Index rules are same as for list

Three dimensional arrays
-------------------------

my_array = np.arange(70)
my_array.shape = (2,7, 5) # Two 2-dimensional arrays 7x5
[[[ 0  1  2  3  4]
  [ 5  6  7  8  9]
  [10 11 12 13 14]
  [15 16 17 18 19]
  [20 21 22 23 24]
  [25 26 27 28 29]
  [30 31 32 33 34]]

 [[35 36 37 38 39]
  [40 41 42 43 44]
  [45 46 47 48 49]
  [50 51 52 53 54]
  [55 56 57 58 59]
  [60 61 62 63 64]
  [65 66 67 68 69]]]

  print(my_array[0,3,4]) # [2-dim array, line, num]
  19

Boolean Mask Array
__________________

my_vector = np.array([-17, -4, 0, 2, 21, 37, 105])
zero_mod_mask = 0 == (my_vector % 7)
sub_array = my_vector[zero_mod_mask] # values from "sub_array"
                                     # that are "True" in "zero_mod_mask"

print(sub_array[sub_array>0]) # prints new array with values > 0

mod_test = 0 == (my_vector % 7) # bool of values from my vector (True or False: num/7 with or with remainer)
positive_test = my_vector > 0 # bool of values from my vector ((True or False: num > 0)

combined_mask = np.logical_and(mod_test, positive_test) # combines both requirements, returns True only
                                                        # if both true and all other False
print(combined_mask)

print(my_vector[combined_mask]) # prints values of my_vector that are True in combined_mask


Broadcasting
-------------
# Attributes:

# shape:
> my_3d_array.shape
(2, 7, 5)

# number of dimensions:
> print(my_3d_array.ndim)
3

# size, number of elements:
> print(my_3d_array.size)
70

# data type for each element:
> print(my_3d_array.dtype)
int64


5 * my_3d_array -2 # will multiplicate each element by 5 and subtract 2

numpy.dot(a, b)
Dot product of two arrays.

a = np.arange(12).reshape(4,3)
b = np.arange(12).reshape(3,4)
# num of columns in a has to be equal num of lines in b
# first raw of a * first column of b, one element at the time
# then first row of a * second column of b
# etc

my_3d_array.sum(axis=0) # sum each element one by one
my_3d_array.sum(axis=1) # sum of each column for each 2-dimensional sub array
my_3d_array.sum(axis=2) # sum of each line for each 2-dimensional sub array
"""



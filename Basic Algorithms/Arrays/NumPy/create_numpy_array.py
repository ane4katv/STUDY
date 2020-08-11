"""
NUMPY is a library for the Python,
adding support for large, multi-dimensional arrays and matrices
along with a large collection of high-level mathematical functions
to operate on these arrays.

Advantages of using Numpy Arrays Over Python Lists:

- consumes less memory.
- fast as compared to the python List.
- convenient to use.

Ways of  creating arrays:
--------------------------
1. From  Python structures
x = np.array([2, 3, 1, 0])

2. Intrinsic numpy array creation objects (e.g., arange, ones, zeros, etc.)

numpy.arange([start, stop, step)

half-open interval (interval including start but excluding stop)
_______________________________________________
np.arange(0, 26, 6)
np.arange(26, step=6)
np.arange(10)

np.arange(0, 26, 6).size
len(np.arange(10,23))

my_range_array = np.arange(10,23)
my_range_array.size

3. Inspace, zeros, ones, data types

np.linspace()
-------------
numpy.linspace(start, stop, num=50)

returns equally-spaced samples from start to stop
closed interval (value of 'stop' is included to the output array)

num (optional) is number of steps generated
Return evenly spaced numbers over a specified interval


# >>>np.linspace(5,15,9)
[ 5.    6.25  7.5   8.75 10.   11.25 12.5  13.75 15.  ]

# >>>my_linstep = np.linspace(5,15,9, retstep = True)
(array([ 5.  ,  6.25,  7.5 ,  8.75, 10.  , 11.25, 12.5 , 13.75, 15.  ]), 1.25)
1.25 is the step size (return when "retstep = True")


Zeros, ones
_______________
# >>>np.zeros(5)
array([0., 0., 0., 0., 0.])

# >>>np.zeros((3,2)) # Returns 2 dimensional array
array([[0., 0.],
       [0., 0.],
       [0., 0.]])

# >>> np.zeros((4,3,2)) # Returns 3 dimensional array
array([[[0., 0.],
        [0., 0.],
        [0., 0.]],

       [[0., 0.],
        [0., 0.],
        [0., 0.]],

       [[0., 0.],
        [0., 0.],
        [0., 0.]],

       [[0., 0.],
        [0., 0.],
        [0., 0.]]])

np.ones() # same az np.zeros()

Data types
----------
Array scalar type       Related Python type

int_                    IntType (Python 2 only)

float_                  FloatType

complex_                ComplexType

bytes_                  BytesType

unicode_                UnicodeType

more https://numpy.org/doc/stable/reference/arrays.scalars.html#arrays-scalars-built-in

# >>> np.zeros(11, dtype='float')
array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
"""

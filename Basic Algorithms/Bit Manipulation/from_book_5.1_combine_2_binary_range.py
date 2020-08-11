def insert_bin_to_another(N, M, i, j):
   left_border = ~((1 << j) - 1)
   right_border = (1 << i) - 1

   mask = left_border | right_border

   obnulenie = N & mask

   result = obnulenie | M << i

   return bin(result)

print(insert_bin_to_another(221, 10, 2, 6))


"""
N, M 32 bit nums
i, j bit positions
Insert M between  i and j of  N

N		1101 1101
M		  10  10
        -------------
res:	1110  1001

1. Unset i to j in N: 
            1101 1101 ->
            1100 0001
    
    a. Create a mask out of ones that has ‘0’ from i to j and rest are ‘1’: 1100 0011

        - left border:	    1100 0000
		    ~ (1 << j) - 1

        - right border: 	0000 0011
            (1 << i) - 1 

        - combining borders
            left | right:
            1100 0000 |
            0000 0011
            --------------
            1100 0011

    b. created mask & N = obnulenie:
            1101 1101 &
            1100 0011
            --------------
            1100 0001

2. obnulenie | M << i = result:
            1100 0001 |
            0010 1000
            ---------------
            1110  1001



# unsigned_int = signed_int + 2**32


"""

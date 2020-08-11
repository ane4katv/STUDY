# ===== O(log n) ===== #

# Examples:
# - Binary Search:
# In every iteration the search group will become half of the original value.
#
# - Finding largest/smallest number in a binary search tree:
# In every iteration, we will drop any half tree either left or right.

# n = 100
# while n != 0:
#     n = n//2
#     print(n)

# ===== O(nlog n) ===== #

n = 100
for i in range(0,100):
    while n != 0:
        n = n//2
        i += 1
        print(n)

# * Now the process of logn need to be executed n times.
# ------------------------------------------------------
# Examples of O(nlogn):
#
# - Merge Sort: The Merge Sort use the Divide-and-Conquer approach
#   to solve the sorting problem. First, it divides the input in half
#   using recursion. After dividing, it sort the halfs and merge them into one sorted output.

# - Quick Sort
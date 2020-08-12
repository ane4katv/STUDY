"""Given a sorted array, return True if element present, False if not"""

def binary_search(array, num, start, end):
    mid_point = end // 2

    # Base case
    if start == end:
        if array[start] == num:
            return True
        else:
            return False

    while start < end:
        if num == mid_point:
            return True

        if num > mid_point:
            binary_search(array[start:end], num, start=mid_point+1, end=end)









a = [2, 4, 6, 8, 9, 12, 18]

print(binary_search(a, num=18, start=0, end=len(a)-1))
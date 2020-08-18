def binarySearch(array, l, r, num):
    if r >= l:
        mid_point = l + (r - l) // 2
        if array[mid_point] == num:
            return True
        elif array[mid_point] > num:
            return binarySearch(array, l, mid_point - 1, num)
        else:
            return binarySearch(array, mid_point + 1, r, num)
    else:
        return False
    
    
a = [4, 6, 8, 9, 12, 18]

print(binarySearch(a, 0, len(a) - 1, 5))
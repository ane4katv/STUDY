"""Given a sorted array, return True if element present, False if not"""


def binary_search(array, num):

    start = 0
    end = len(array) - 1
    # mid_point = (start+end) // 2
    mid_point = start + (end - start) // 2

    if start <= end:

        if num == array[mid_point]:
            return True

        if num > array[mid_point]:
            start = mid_point + 1
            return binary_search(array[start:end+1], num)

        if num < array[mid_point]:
            end = mid_point - 1
            return binary_search(array[start:end+1], num)

    else:
        return False






a = [4, 6, 8, 9, 12, 18]


print(binary_search(a, 19))
print(binary_search(a, 20))
print(binary_search(a, 21))
print(binary_search(a, 4))
print(binary_search(a, 6))
print(binary_search(a, 8))
print(binary_search(a, 9))
print(binary_search(a, 12))
print(binary_search(a, 18))

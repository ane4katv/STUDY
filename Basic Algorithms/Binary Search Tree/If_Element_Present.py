"""Given a sorted array, return True if element present, False if not"""


def binary_search(array, num):
    start = 0
    end = len(array) - 1
    mid_point = len(array) // 2

    # Base case
    if start == end:
        if array[0] == num:
            return True
        else:
            return False

    if num > array[mid_point]:
        start = mid_point + 1
        print(f'start: {array[start]}, end: {array[end]}, mid_point: {array[mid_point]}')
        binary_search(array[start:end+1], num)

    if num < array[mid_point]:
        end = mid_point - 1
        binary_search(array[start:end], num)

    return array



a = [4, 6, 8, 9, 12, 18]

print(binary_search(a, 5))
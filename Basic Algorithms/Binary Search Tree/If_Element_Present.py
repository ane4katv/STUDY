"""Given a sorted array, return True if element present, False if not"""


def binary_search(array, num):
    start = 0
    end = len(array) - 1
    mid_point = len(array) // 2
    print(mid_point)
    print(start, end)
    if num > array[mid_point]:
        start = mid_point + 1
        print(f'start: {array[start]}, end: {array[end]}, mid_point: {array[mid_point]}')
        return binary_search(array[start:end+1], num)

    if num < array[mid_point]:
        end = mid_point - 1
        if end == start:
            if array[0] == num:
                return True
            else:
                return False
        else:
            return binary_search(array[start:end], num)


#l + (r-l)//2


a = [4, 6, 8, 9, 12, 18]

print(binary_search(a, 4))
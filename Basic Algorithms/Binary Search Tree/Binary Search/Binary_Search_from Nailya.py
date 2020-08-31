def binary_search(array, left, right, num):
    if right >= left:
        mid = (left + right) // 2

        if array[mid] == num:
            return True

        elif array[mid] > num:
            return binary_search(array, left, mid-1, num)

        else:
            return binary_search(array, mid+1, right, num)

    else:
        return False

a = [4, 6, 8, 9, 12, 18]

print(binary_search(a, 0, len(a)-1, 2))
# print(binary_search(a, 0, len(a)-1, 3))
# print(binary_search(a, 0, len(a)-1, 4))
# print(binary_search(a, 0, len(a)-1, 6))
# print(binary_search(a, 0, len(a)-1, 8))
# print(binary_search(a, 0, len(a)-1, 9))
# print(binary_search(a, 0, len(a)-1, 12))
# print(binary_search(a, 0, len(a)-1, 18))
# print(binary_search(a, 0, len(a)-1, 19))


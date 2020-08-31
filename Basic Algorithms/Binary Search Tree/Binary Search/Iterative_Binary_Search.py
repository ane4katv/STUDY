def binary_search_iter(array, num):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid_point = (left + right) // 2
        print(array[mid_point])

        if array[mid_point] == num:
            return True

        if array[mid_point] > num:
            right = mid_point - 1

        if array[mid_point] < num:
            left = mid_point + 1

    return False


a = [4, 6, 8, 9, 12, 18]

print(binary_search_iter(a, 20))




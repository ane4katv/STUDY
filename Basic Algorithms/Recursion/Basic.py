# def sum_elem(array):
#     if len(array) == 0:
#         return 0
#     return array[0] + sum_elem(array[1:])

# def fact(array):
#     if len(array) == 0:
#         return 0
#     if len(array) == 1:
#         return array[0]
#     # print(array[1:]) * fact(array[1:])
#     return array[0] * fact(array[1:])

# def count_elems(array):
#     if not array:
#         return 0
#     return 1 + count_elems(array[1:])

# def max_num(array):
#     if len(array) == 2:
#         if array[0] > array[1]:
#             return array[0]
#         else:
#             return array[1]
#     sub_max = max_num(array[1:])
#     if array[0] > sub_max:
#         return array[0]
#     else:
#         return sub_max

# def divide_land(length, width):
#     if length % width == 0:
#         smallest_side = min(length, width)
#         return smallest_side
#     return divide_land(width, length % width)


def binary_search(array, fst, lst, x):

    if lst >= fst:
        mid_point = (fst + lst) // 2

        if array[mid_point] == x:
            return f'midpoint_index: {mid_point}, midpoint_value: {array[mid_point]}'

        elif array[mid_point] < x:
            return binary_search(array, mid_point + 1, lst, x)

        elif array[mid_point] > x:
            return binary_search(array, fst, mid_point, x)

    else:
        return "Element is not present"


a = [2,4,6,10,18]
print(binary_search(a, 0, len(a)-1, 6))
print(binary_search(a, 0, len(a)-1, 25))
print(binary_search(a, 0, len(a)-1, 18))
print(binary_search(a, 0, len(a)-1, 2))



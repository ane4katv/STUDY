def insertion_sort(array):
    for i in range(1, len(array)):
        while array[i] < array[i-1] and i > 0:
            swap(i, i-1)
            i -= 1


def swap(i, j):
    array[i], array[j] = array[j], array[i]



array = [9,8]
insertion_sort(array)
print(array)
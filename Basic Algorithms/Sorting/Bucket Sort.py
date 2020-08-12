import math


def bucket_sort(array):

    max_elem = max(array)
    min_elem = min(array)
    output = []

    buckets = [[] for i in array]

    bucket_range = math.ceil((max_elem - min_elem) / len(array))

    for i in range(len(array)):
        buckets[(array[i] - min(array)) // bucket_range].append(array[i])

    for i in range(len(buckets)):
        if len(buckets[i]) > 1:
            insertion_sort(buckets[i])
        print(buckets[i])
        if len(buckets[i]) > 0:
            output.extend(buckets[i])

    return output


def insertion_sort(array):
    for i in range(1, len(array)):
        while array[i] < array[i-1] and i > 0:
            swap(i, i-1)
            i -= 1
    return array


def swap(i, j):
    array[i], array[j] = array[j], array[i]


array = [11,9,21,8,17,19,13]
print(bucket_sort(array))


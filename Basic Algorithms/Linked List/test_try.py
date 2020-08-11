def radix_sort(array):
    max_elem = max(array)
    place = 1

    while max_elem // place > 0:
        count_sort(array, place)
        place *= 10


def count_sort(array, place):

    count = [0] * 10
    output = [0] * len(array)

    for i in range(len(array)):
        count[array[i] // place % 10] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(output)-1, -1, -1):
        count[array[i] // place % 10] -= 1
        output[count[array[i] // place % 10]] = array[i]


    for i in range(len(output)):
        array[i] = output[i]

    print(output)



radix_sort([11, 2, 13, 25, 326, 8])

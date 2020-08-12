def shrink(gap):
    gap /= 1.3

    if gap < 1:
        return 1
    else:
        return int(gap)


def swap_it(i, j):
    array[i], array[j] = array[j], array[i]


def comb_sort(array):
    gap = len(array)
    swapped = True

    while swapped is True or gap != 1:
        gap = shrink(gap)
        swapped = False

        for i in range(0, len(array) - gap):
            if array[i] > array[i + gap]:
                swap_it(i, i + gap)
                swapped = True


array = [8, 4, 1, 3, -44]
comb_sort(array)
print(array)

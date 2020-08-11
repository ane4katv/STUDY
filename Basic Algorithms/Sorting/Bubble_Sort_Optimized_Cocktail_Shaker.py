def cocktail_shaker_sort(array):

    def swap(i, j):
        array[i], array[j] = array[j], array[i]

    upper = len(array) - 1
    lower = 0

    no_swap = False

    while no_swap is False and upper - lower > 1:
        no_swap = True

        for j in range(lower, upper):
            if array[j + 1] < array[j]:
                swap(j + 1, j)
                no_swap = False
        upper = upper - 1

        for j in range(upper, lower, -1):
            if array[j - 1] > array[j]:
                swap(j - 1, j)
                no_swap = False
        lower = lower + 1


alist = [5,4,3,2,1]
cocktail_shaker_sort(alist)

print(alist)
def selection_sort(array):
    n = 0

    while n < len(array):
        min_elem = array[n]
        min_index = n
        count = n

        for i in range(n+1, len(array)):
            count += 1

            if array[i] < min_elem:
                min_elem = array[i]
                min_index = count

            if min_elem != array[n]:
                array[min_index], array[n] = array[n], array[min_index]

        n += 1

    return array


array = [5, 8, 3, 0, 6, 12]
print(selection_sort(array))


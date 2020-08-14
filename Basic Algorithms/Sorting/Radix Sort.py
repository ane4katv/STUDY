def radix_sort(array):
    max_num = max(array)
    place = 1

    while max_num // place > 0:
        counting_sort(array, place)
        place *= 10

    print(array)

def counting_sort(array, place):
    count = [0 for i in range(0,10)]
    output = [0] * len(array)

    for i in range(len(array)):          # nums of array -> indices of count
        count[array[i]//place % 10] += 1

    for i in range(1, len(count)):       # accumulate nums in count
        count[i] += count[i-1]

    for i in range(len(array)-1, -1, -1): # fill up output
        count[array[i] // place % 10] -= 1
        output[count[array[i] // place % 10]] = array[i]

    for i in range(len(array)):
        array[i] = output[i]


radix_sort([410,1,1,0,6])

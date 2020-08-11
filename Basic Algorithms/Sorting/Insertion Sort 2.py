def insertion_sort(array):
    for i in range(1, len(array)):
        cur_index = i
        cur_value = array[i]
        while cur_index > 0 and array[cur_index - 1] > cur_value:
            array[cur_index] = array[cur_index - 1]
            cur_index -= 1
        array[cur_index] = cur_value

    return array


input_array = [6,5,1,4,8,2]
print(insertion_sort(input_array))

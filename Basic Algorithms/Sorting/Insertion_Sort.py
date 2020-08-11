def insertion_sort(a):

    for i in range(1, len(a)):
        while a[i] < a[i-1] and i > 0:
            a[i], a[i - 1] = a[i-1], a[i]
            i -= 1

    return a


a = [5,4,3,2,1]

print(insertion_sort(a))


"""
Alternative:

def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        cur_elem = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than cur, to one position ahead
        # of their current position
        prev_index = i - 1
        while prev_index >= 0 and cur_elem < arr[prev_index]:
            arr[prev_index + 1] = arr[prev_index] # cur gets same value as prev!
            prev_index -= 1
        arr[prev_index + 1] = cur_elem # ???

    return arr

a = [5,4,3,2,1]

print(insertionSort(a))

"""

def heap_sort():
    last_parent = len(array) // 2 -1

    for i in range(last_parent, -1, -1):
        heapify(len(array), i)

    for i in range(len(array)-1, 0, -1):
        swap(i, 0)
        heapify(i, 0)


def heapify(length, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i +2

    if left < length and array[left] > array[largest]:
        largest = left

    if right < length and array[right] > array[largest]:
        largest = right

    if largest != i:
        swap(i, largest)
        heapify(length, largest)


def swap(i,j):
    array[i], array[j] = array[j], array[i]


array = [5,8,12,0,-3,6,4]
heap_sort()
print(array)
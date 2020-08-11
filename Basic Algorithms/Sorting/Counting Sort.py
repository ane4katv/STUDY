# mine

def counting_sort(nums):
    output = [0] * len(nums)
    count = [0 for i in range(min(nums),len(nums)+1)]

    for i in nums:
        count[i] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]

    for i in range(len(nums)):
        output[count[nums[i]]-1] = nums[i]
        count[nums[i]] -= 1

    return output


nums = [1, 2, 3, 2, 2, 1, 3, 3]
print(counting_sort(nums))



def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]

        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]

    print(output, '\n')
    print(array, '\n')


data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)

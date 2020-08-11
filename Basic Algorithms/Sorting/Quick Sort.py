# Quick Sort


def qsort(nums, fst, lst):

    if fst >= lst:
        return

    i, j = fst, lst
    pivot = nums[fst]


    while i <= j:
        while nums[i] < pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1

        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1

    qsort(nums, fst, j)
    qsort(nums, i, lst)

    return nums


nums = [4,2,1,3,9]
print(qsort(nums, 0, len(nums)-1))
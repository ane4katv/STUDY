def counting_sort(nums):
    count = [0 for _ in range(0, max(nums)+1)]
    output = [0] * len(nums)

    for i in range(len(nums)):
        count[nums[i]] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]

    for i in range(len(nums)):
        count[nums[i]] -= 1
        output[count[nums[i]]] = nums[i]








nums = [2, 0, 0, 1, 3]
counting_sort(nums)


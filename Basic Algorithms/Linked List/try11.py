def counting_sort(nums):
    output = [0] * len(nums)
    count = [0 for i in range(0, max(nums)+1)]

    print(count)
    for i in nums:
        count[i] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]
        print(count)

    for i in range(len(nums)):
        output[count[nums[i]]-1] = nums[i]
        count[nums[i]] -= 1
    return output

nums = [48,1,1,0,600]
print(counting_sort(nums))
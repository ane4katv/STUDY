def k_largest(nums, k):
    max_elem = max(nums)

    count = [0 for i in range(0, max_elem+1)]
    result = []

    for i in range(0, len(nums)):
        count[nums[i]] += 1

    while k > 0:
        max_index = 0
        max_num = count[0]
        for i in range(1, len(count)):
            if count[i] > max_num:
                max_num = count[i]
                max_index = i

        result.append(max_index)
        count[max_index] = 0
        k -= 1

    return result


a = [1,1,1,2,2,3]
print(k_largest(a, 2))
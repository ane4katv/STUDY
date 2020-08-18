def k_largest(nums, k):
    max_elem = max(nums)
    min_num = min(nums)
    shift = 0

    if min_num < 0:
        shift = - min_num  # it makes it positive ;)

    count = [0 for i in range(0, max_elem+1 + shift)]

    result = []

    for i in range(0, len(nums)):
        count[nums[i]+shift] += 1

    print(count)

    while k > 0:
        max_index = 0
        max_num = count[0]
        for i in range(1, len(count)):
            if count[i] > max_num:
                max_num = count[i]
                max_index = i

        result.append(max_index - shift)
        count[max_index] = 0
        k -= 1

    return result


a = [-5,-8, -8]
print(k_largest(a, 2))
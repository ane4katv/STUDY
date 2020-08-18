def k_largest(nums, k):
    max_elem = max(nums)
    min_num = min(nums)
    shift = 0

    if min_num < 0:
        shift = - min_num  # it makes it positive ;)

    count = [0 for i in range(0, max_elem+1 + shift)]

    for i in range(0, len(nums)):
        count[nums[i]+shift] += 1

    print(count)

    ''' while k > 0:
        max_index = 0
        max_num = count[0]
        for i in range(1, len(count)):
            if count[i] > max_num:
                max_num = count[i]
                max_index = i

        result.append(max_index - shift)
        count[max_index] = 0
        k -= 1'''
    output = [0] * len(count)
    o = [0] * len(count)
    c = [0 for i in range(min(count),len(count)+1)]
    for i in count:
        c[i] += 1

    for i in range(1, len(c)):
        c[i] += c[i-1]

    for i in range(len(count)):
        output[c[count[i]]-1] = count[i]
        o[c[count[i]]-1] = i - shift
        c[count[i]] -= 1
    return o[-k:]


a = [-5,-8, -8, -8, -5, -1,-3]
print(k_largest(a, 2))
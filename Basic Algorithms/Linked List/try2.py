def k_largest(nums, k):
    max_elem = max(nums)
    min_num = min(nums)
    shift = 0


    if min_num < 0:
        shift = - min_num

    count = [0 for i in range(0, max_elem+1 + shift)]

    if len(count) == 1:
        return [nums[0]]

    for i in range(0, len(nums)):
        count[nums[i]+shift] += 1

    print(count)

    o = [0] * len(count)
    c = [0 for i in range(min(count), len(count)+1)]

    for i in count:
        pass
        c[i] += 1

    for i in range(1, len(c)):
        c[i] += c[i - 1]

    for i in range(len(count)):
        c[count[i]] -= 1
        o[c[count[i]]] = i - shift

    return o[-k:]

a = [1,1,1,2,2,33333333]
print(k_largest(a, 2))

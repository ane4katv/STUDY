# Array_refferal
# Slices, extend just refer to element (shallow copy)
# Append etc will keep hard copy of original array

counters = [1,2,3]

new_counters = counters[1]

counters = [5,6,7]


print(new_counters)


# a = counters.copy()
#
# shallow = list(counters)

# counters.append(new_counters)
# counters.extend(new_counters)
#
# print(f"{counters}\n{new_counters}")
#
#
# new_counters.pop()
#
# print(f"{counters}\n{new_counters}")
#

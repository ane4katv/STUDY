# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/

# From Nailya (pretty cool, no need of string use)


def reverse_num(x):
    reverse = 0
    if x > 0:
        while x > 0:
            end = x % 10
            reverse = reverse * 10 + end
            x = x // 10

        if reverse < 2 ** 31:
            return reverse

        else:
            return 0

    elif x < 0:
        while abs(x) > 0:
            dig = abs(x) % 10
            reverse = reverse * 10 + dig
            x = abs(x) // 10

        if -reverse > -2 ** 31:
            return -reverse

        else:
            return 0

    else:
        return x

# Mine:

# def reverse_num(x):
#     x = list(str(x))
#
#     if len(x) == 0:
#         return 0
#
#     if len(x) == 1:
#         return x[0]
#
#     while x[-1] == '0':
#         x.pop()
#     print(x)
#     if x[0] == '-':
#         return - reverse_poz(x[1:])
#     else:
#         return reverse_poz(x)
#
#
# def reverse_poz(num):
#     start = 0
#     end = len(num) - 1
#     while end > start:
#         num[start], num[end] = num[end], num[start]
#         start += 1
#         end -= 1
#
#     num_to_int = int("".join(num))
#
#     if num_to_int < - 2 ** 31 or num_to_int > 2 ** 31:
#         return 0
#
#     num_to_str = ''
#     return int(num_to_str.join(num))


x = =153
print(reverse_num(x))

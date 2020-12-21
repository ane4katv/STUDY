# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/

def reverse_num(x):
    x = list(str(x))

    if len(x) == 0:
        return 0

    if len(x) == 1:
        return x[0]

    while x[-1] == '0':
        x.pop()
    print(x)
    if x[0] == '-':
        return - reverse_poz(x[1:])
    else:
        return reverse_poz(x)


def reverse_poz(num):
    start = 0
    end = len(num) - 1
    while end > start:
        num[start], num[end] = num[end], num[start]
        start += 1
        end -= 1

    num_to_str = ''
    return int(num_to_str.join(num))


x = -12300
print(reverse_num(x))

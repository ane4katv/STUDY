# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/


def first_unique_char(s):
    my_dict = {}
    for i in s:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1

    print(my_dict)

    for i in range(len(s)):
        if my_dict[s[i]] == 1:
            return i
    return -1

input_str = 'loveleetcode'
print(first_unique_char(input_str))

# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/


def str_to_int(s):
    alist = []

    no_spaces = s.lstrip()

    if len(no_spaces) == 0:
        return 0

    if no_spaces[0] == "-" or no_spaces[0] == "+":
        if no_spaces[0] == "-":
            alist.append("-")

        if no_spaces[0] == "+":
            alist.append("+")

        if len(no_spaces) > 1:
            no_spaces = no_spaces[1:]
        else:
            return 0

    start = 0

    while no_spaces[start].isdigit():
        alist.append(no_spaces[start])
        start += 1
        if start == len(no_spaces):
            break

    if len(alist) == 0 or len(alist) == 1 and ((alist[0] == "-") or alist[0] == "+"):
        return 0
    else:
        no_spaces = int("".join(alist))
        if no_spaces < - 2 ** 31:
            return -2147483648

        elif no_spaces > 2 ** 31 - 1:
            return 2147483647
        else:
            return no_spaces

str1 = "   +0 123"
str2 = "   -42"
str3 = "4193 with words"
str4 = "words and 987"
str5 = "-91283472332"

print(str_to_int(str1))
print(str_to_int(str2))
print(str_to_int(str3))
print(str_to_int(str4))
print(str_to_int(str5))

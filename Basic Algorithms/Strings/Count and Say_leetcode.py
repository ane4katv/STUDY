# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/886/

def split_string(astr):
    if len(astr) == 0:
        return []

    elif len(astr) == 1:
        return [astr[0]]

    else:
        substr = astr[0]
        result = []
        for i in range(1, len(astr)):
            if astr[i] != astr[i-1]:
                result.append(substr)
                substr = astr[i]
            else:
                substr += astr[i]

        result.append(substr)

    return result

def count_say(input_string):
    substrings = split_string(input_string)
    count_say_list = []

    for substr in substrings:
        count_say_list.append(str(len(substr)))
        count_say_list.append(substr[0])

    result = ""

    return result.join(count_say_list)

def count_say_nth(n):
    num = '1'
    result = ['1']
    while len(result) < n:
        new_num = count_say(num)
        result.append(new_num)
        num = new_num
    return num

astr = "33222511"

print(count_say_nth(4))

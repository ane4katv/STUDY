# 1. Вводится строка. Удалить из нее все пробелы. После этого определить, является ли она палиндромом.


def if_palindrome(input_string):
    new_string = input_string.replace(" ", "").lower()

    punctuations = '!()-[]{};:"\,<>./?@#$%^\'&*_~'
    for i in new_string:
        if i in punctuations:
            new_string = new_string.replace(i, "")

    print(new_string)

    start = 0
    end = len(new_string) - 1

    while start < end:
        if new_string[start] != new_string[end]:
            return False
        start += 1
        end -= 1
    return True

    # if new_string == new_string[::-1]:
    #     return True
    # else:
    #     return False

print(if_palindrome("anj!()-[]{};:'na"))

# 2. Вводится строка слов, разделенных пробелами. Найти самое длинное слово и вывести его на экран.


def longest_word(input_string):
    string_to_list = input_string.split()
    longest_len = 0
    longest_word = None

    for i in string_to_list:
        if len(i) > longest_len:
            longest_len = len(i)
            longest_word = i

    print(longest_word)


input_string = "some words divided by spaces"
longest_word(input_string)

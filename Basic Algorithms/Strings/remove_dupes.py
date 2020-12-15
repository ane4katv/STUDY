# 3. Вводится строка. Требуется удалить из нее повторяющиеся символы.


def remove_dupes(a_string):

    unique_symbols = ""

    for i in a_string:
        if i in unique_symbols and i != " ":
            continue
        else:
            unique_symbols += i

    print(unique_symbols)


input_string = "abba gaaga boobs left right"
remove_dupes(input_string)



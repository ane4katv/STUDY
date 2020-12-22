def first_unique_char(s):
    unique_chars = []
    repeated_chars = []
    for i in s:
        if i not in unique_chars:
            unique_chars.append(i)
        else:
            if i not in repeated_chars:
                repeated_chars.append(i)

    print(unique_chars)
    print(repeated_chars)

    if sorted(unique_chars) == sorted(repeated_chars):
        return -1

    for i in unique_chars:
        if i not in repeated_chars:
            return s.find(i)


input_str = 'adaccdcda'
print(first_unique_char(input_str))

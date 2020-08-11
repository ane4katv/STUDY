# Sort the given string letters in alphabetical order

def counting_sort(letters):
    output = [0] * len(letters)
    count = [0] * 256

    for i in letters:
        count[ord(i)] += 1

    for i in range(256):
        count[i] += count[i-1]

    for i in range(len(letters)):
        output[count[ord(letters[i])] - 1] = letters[i]
        count[ord(letters[i])] -= 1

    return "".join(output)

letters = "tryit"
print(counting_sort(letters))

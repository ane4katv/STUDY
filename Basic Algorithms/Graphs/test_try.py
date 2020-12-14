a = {"*": "*"}

word = "waiter"

for i in word:
    if i not in a:
        a[i] = {}
    a = a[i]

print(a)
def lower_cased(word):
    return word.lower()

print(lower_cased("Some"))

print(sorted(['Some', 'words', 'sort', 'differently']))
print(sorted(['Some', 'words', 'sort', 'differently'], key=lower_cased))

print(sorted(['Some', 'words', 'sort', 'differently'], key=lambda word: word.lower()))


points = [(1,9), (2,3), (4,1),(3,7), (5,4), (6,8), (7,2), (8,8), (7,9), (9,6)]
axis = 1

print(sorted(points, key=lambda point: point[axis]))

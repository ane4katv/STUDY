a = [(0, 3, 7), (0, 1, 3), (1, 2, 2), (1, 0, 8), (2, 0, 5), (2, 3, 1), (3, 0, 2)]

inf = float('inf')

distance = [
    [inf, inf, inf, inf],
    [inf, inf, inf, inf],
    [inf, inf, inf, inf],
    [inf, inf, inf, inf]]

for i in range(len(distance)):
    distance[i][i] = 0

print(distance)



for i in a:
    distance[i[0]][i[1]] = i[2]

print(distance)
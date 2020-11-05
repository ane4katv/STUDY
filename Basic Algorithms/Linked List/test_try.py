new_edges = [('A', 'B', 2), ('A', 'C', 4)]
min_edge = float('inf')
for i in new_edges:
    if i[2] < min_edge:
        min_edge = i[2]
        edge = i

print(edge, min_edge)

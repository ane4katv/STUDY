
graph_1 = {
           "B": ["A", "E"],
           "C": ["A", "B", "E", "F"],
           "E": ["B", "C"],
           "F": ["F"]}

if "A" not in graph_1:
    graph_1["A"]= [10]
else:
    graph_1["A"].append(10)

print(graph_1)






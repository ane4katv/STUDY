from pprint import pprint


def adjacency_matrix(graph):
    keys = sorted(graph)  # returns sorted list() of graph's keys!
    adj_matrix = [[0] * len(keys) for _ in range(len(keys))]

    for key in keys:
        for value in graph[key]:
            start_vertex_index = keys.index(key)
            end_vertex_index = keys.index(value)

            adj_matrix[start_vertex_index][end_vertex_index] = 1

    return adj_matrix


if __name__ == "__main__":
    graph_1 = {"E": ["B", "C"],
               "A": ["B", "C"],
               "B": ["A", "E"],
               "C": ["A", "B", "E", "F"],
               "F": ["F"]}

    pprint(adjacency_matrix(graph_1))
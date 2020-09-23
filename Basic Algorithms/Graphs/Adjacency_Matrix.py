from pprint import pprint


def adjacency_matrix(graph):
    keys = sorted(graph)
    adj_matrix = [[0] * len(keys) for _ in range(len(keys))]
    edges = []

    for key in keys:
        for value in graph[key]:
            edges.append((key, value))

    for edge in edges:
        start_vertex_index = keys.index(edge[0])
        end_vertex_index = keys.index(edge[1])

        adj_matrix[start_vertex_index][end_vertex_index] = 1

    return adj_matrix


if __name__ == "__main__":
    graph_1 = {"A": ["B", "C"],
               "B": ["A", "E"],
               "C": ["A", "B", "E", "F"],
               "E": ["B", "C"],
               "F": ["F"]}

    pprint(adjacency_matrix(graph_1))
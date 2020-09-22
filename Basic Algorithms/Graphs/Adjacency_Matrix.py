from pprint import pprint


def adjacency_matrix(graph):
    matrix_elements = sorted(graph.keys())
    size = len(matrix_elements)

    adjacency_matrix = [[0]*size for i in range(size)]
    edges_list = []

    for i in matrix_elements:
        for j in graph[i]:
            edges_list.append((i,j))

    for edge in edges_list:
        index_of_first_vertex = matrix_elements.index(edge[0])
        index_of_second_vertex = matrix_elements.index(edge[1])
        adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1

    return adjacency_matrix


graph_1 = {0: [1, 2, 3],
         1: [0, 2],
         2: [0, 1, 4],
         3: [0],
         4: [2]}

pprint(adjacency_matrix(graph_1))
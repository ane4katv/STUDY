def dijkstra(graph, start, end):
    shortest_distance = {}
    predecessor = {}
    unseen_nodes = list(graph.keys())
    infinity = float("inf")
    path = []

    # set all vertices besides of start to "infinity"
    # shortest_distance = {'a': 0, 'b': inf, 'c': inf, 'd': inf, 'e': inf}
    for node in unseen_nodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseen_nodes:
        min_node = None

        for node in unseen_nodes:
            if min_node is None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node

        # Main part of algorithm
        for child_node, weight in graph[min_node].items():
            if weight + shortest_distance[min_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_node]

                predecessor[child_node] = min_node

        unseen_nodes.remove(min_node)

        # go backwards from goal to start and insert each step to beginning of path
    current_node = end
    while current_node != start:
        try:
            path.insert(0, current_node)
            current_node = predecessor[current_node]
        except KeyError: # in directed graph not every node can reach another node
            print('Path not reachable')
            break
    path.insert(0, start)

    # if shortest_distance[end] != infinity:
    print(f'Shortest distance is {shortest_distance[end]}')
    print(f'And the path is {path}')


graph = {'a': {'b': 10, 'c': 3},
         'b': {'c': 1, 'd': 2},
         'c': {'b': 4, 'd': 8, 'e': 2},
         'd': {'e': 7},
         'e': {'d': 9}}

dijkstra(graph, 'a', 'd')

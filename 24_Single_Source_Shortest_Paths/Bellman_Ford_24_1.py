from DAG_Shortest_Paths_24_2 import Vertex


def bellman_ford(graph, s):

    # Loop V-1 times
    for i in range(len(graph) - 1):
        # Loop through each edge
        for vertex_id, vertex in graph.items():
            print(f'Main vertex: {vertex_id} Distance: {vertex.distance}')
            for adj_vertex_id, weight in vertex.adj_dict.items():
                adj_vertex = graph[adj_vertex_id]
                print(f'   Adj vertex: {adj_vertex_id} Distance: {adj_vertex.distance}')
                if adj_vertex.distance > vertex.distance + weight:
                    adj_vertex.distance = vertex.distance + weight
                    print(f'      Adj vertex: {adj_vertex_id} Distance: {adj_vertex.distance}')

    # Check for negative cycles. Loop through each edge
    for vertex_id, vertex in graph.items():
        for adj_vertex_id, weight in vertex.adj_dict.items():
            adj_vertex = graph[adj_vertex_id]

            if adj_vertex.distance > vertex.distance + weight:
                return False

    return True


if __name__ == '__main__':

    # # Define the graph (Chapter 24.1 in CLRS)
    # s = Vertex('s', {'t': 6, 'y': 7})
    # t = Vertex('t', {'x': 5, 'y': 8, 'z': -4})
    # y = Vertex('y', {'z': 9, 'x': -3})
    # x = Vertex('x', {'t': -2})
    # z = Vertex('z', {'s': 2, 'x': 7})
    # s.distance = 0
    # graph = {'x': x, 'y': y, 'z': z, 's': s, 't': t}


    s = Vertex('s', {'x': 1, 'y': 2})
    x = Vertex('x', {'y': -1})
    y = Vertex('y', {'s': -1})
    s.distance = 0
    graph = {'s': s, 'x': x, 'y': y}

    all_positive_cycles = bellman_ford(graph, s)

    if all_positive_cycles:
        print("All Positive Cycles")
    else:
        print("Has Negative Cycles")
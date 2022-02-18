import heapq

class Vertex:
    def __init__(self, an_id, an_adj_dict):
        self.id = an_id
        self.parent = None
        self.distance = float('inf')
        self.visited = False
        self.adj_dict = an_adj_dict  # key=id : val=weight

    def add_adj_vertex(self, id, weight):
        self.adj_dict[id] = weight

    def __lt__(self, other):
        return self.id < other.id

    def __le__(self, other):
        return self.id <= other.id


def dijkstra_heap(graph, root):
    root.d = 0

    priority_queue = [(root.d, root)]

    while priority_queue:
        current_distance, vertex = heapq.heappop(priority_queue)

        # Update the distance values of the adjacent vertices if the current distance is greater than the new distance
        for adj_vertex_id, weight in vertex.adj_dict.items():
            adj_vertex = graph[adj_vertex_id]

            if adj_vertex.distance > vertex.distance + weight:
                adj_vertex.distance = vertex.distance + weight
                adj_vertex.parent = vertex
                heapq.heappush(priority_queue, (adj_vertex.distance, adj_vertex))


def dijkstra(graph, root):
    root.distance = 0

    frontier_vertices = {root}

    while frontier_vertices:
        vertex = find_closest_vertex(frontier_vertices)

        # Update the distance values of the adjacent vertices if the current distance is greater than the new distance
        for adj_vertex_id, weight in vertex.adj_dict.items():
            adj_vertex = graph[adj_vertex_id]

            if adj_vertex.distance > vertex.distance + weight:
                adj_vertex.distance = vertex.distance + weight
                adj_vertex.parent = vertex
                frontier_vertices.add(adj_vertex)

        # Remove the vertex from the frontier_vertices
        frontier_vertices.remove(vertex)


def find_closest_vertex(frontier_vertices):
    min_dist = float('inf')
    closest_vertex = None

    for vertex in frontier_vertices:
        if vertex.distance < min_dist:
            min_dist = vertex.distance
            closest_vertex = vertex

    return closest_vertex

# # Example 1
# # Define the graph (Chapter 24.3 in CLRS)
# s = Vertex('s', {'t': 10, 'y': 5})
# t = Vertex('t', {'x': 1, 'y': 2})
# y = Vertex('y', {'t': 3, 'z': 2, 'x': 9})
# x = Vertex('x', {'z': 4})
# z = Vertex('z', {'s': 7, 'x': 6})
# graph = {'x': x, 'y': y, 'z': z, 's': s, 't': t}
#
# dijkstra_heap(graph, s)
# # dijkstra(graph, s)

# # Example 2
# # Another graph
# a = Vertex('a', {'b': 2, 'c': 3})
# b = Vertex('b', {'d': 3, 'e': 1})
# c = Vertex('c', {'f': 2})
# d = Vertex('d', {})
# e = Vertex('e', {'f': 1})
# f = Vertex('f', {})
# graph = {'d': d, 'e': e, 'f': f, 'c': c, 'a': a, 'b': b}
#
# dijkstra_heap(graph, a)
# # dijkstra(graph, a)

# Example 3
# Another graph
a = Vertex('a', {'d': 10, 'b': 1})
b = Vertex('b', {'c': 1})
c = Vertex('c', {'d': 1})
d = Vertex('d', {})
graph = {'d': d, 'c': c, 'a': a, 'b': b}

# dijkstra_heap(graph, a)
dijkstra(graph, a)

# Print the results
for vertex in graph.values():
    if vertex.parent is None:
        print(f'id:{vertex.id}, parent:None, distance:{vertex.distance}')
    else:
        print(f'id:{vertex.id}, parent:{vertex.parent.id}, distance:{vertex.distance}')
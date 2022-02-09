class Vertex:
    def __init__(self, an_id, an_adj_dict):
        self.id = an_id
        self.parent = None
        self.distance = float('-inf')
        self.visited = False
        self.adj_dict = an_adj_dict  # key=id : val=weight

    def add_adj_vertex(self, id, weight):
        self.adj_dict[id] = weight

    def __lt__(self, other):
        return self.id < other.id

    def __le__(self, other):
        return self.id <= other.id


def dag_longest_paths(graph):

    sorted_vertices = sort_topologically(graph)

    for vertex in sorted_vertices:

        for adj_vertex_id in vertex.adj_dict:
            adj_vertex = graph[adj_vertex_id]

            if adj_vertex.distance < vertex.distance + vertex.adj_dict[adj_vertex_id]:
                adj_vertex.distance = vertex.distance + vertex.adj_dict[adj_vertex_id]
                adj_vertex.parent = vertex



def sort_topologically(graph):

    sorted_vertices = list()

    # Loop thru vertices
    for vertex_id in graph:
        vertex = graph[vertex_id]

        if not vertex.visited:
            sorted_vertices = dfs(vertex, sorted_vertices, graph)

    return sorted_vertices


def dfs(vertex, sorted_vertices, graph):

    vertex.visited = True

    # Loop thru adjacent vertices
    for adj_vertex_id in vertex.adj_dict:
        adj_vertex = graph[adj_vertex_id]

        if not adj_vertex.visited:
            dfs(adj_vertex, sorted_vertices, graph)

    sorted_vertices.insert(0, vertex)

    return sorted_vertices


if __name__ == '__main__':
    # Define the graph (Chapter 24.2 in CLRS)
    a = Vertex('a', {'b': 2, 'c': 2, 'e': 3})
    b = Vertex('b', {})
    c = Vertex('c', {})
    d = Vertex('d', {'e': 1})
    e = Vertex('e', {'b': 4})
    graph = {'e': e, 'c': c, 'd': d, 'a': a, 'b': b}

    # Set the root vertex
    a.distance = 0

    dag_longest_paths(graph)

    # Print the results
    for vertex in graph.values():
        if vertex.parent is None:
            print(f'id:{vertex.id}, parent:None, distance:{vertex.distance}')
        else:
            print(f'id:{vertex.id}, parent:{vertex.parent.id}, distance:{vertex.distance}')
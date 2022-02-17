class Vertex:
    def __init__(self, an_id, an_adj_dict):
        self.id = an_id
        self.parent = None
        self.d = float('-inf')  # the length of the longest path to this vertex seen so far
        self.visited = False
        self.adj_dict = an_adj_dict  # key=id : val=weight

        self.max_length = 0  # Length of the longest path when starting from this vertex
        self.child = None

    def add_adj_vertex(self, id, weight):
        self.adj_dict[id] = weight

    def __lt__(self, other):
        return self.id < other.id

    def __le__(self, other):
        return self.id <= other.id

# --------------------------- Begin - Dynamic Programming Version ---------------------------
def dfs_dp(vertex, graph, dp):
    vertex.color = True

    # Loop thru adjacent vertices
    for adj_vertex_id in vertex.adj_dict:
        adj_vertex = graph[adj_vertex_id]

        if not adj_vertex.color:
            dfs_dp(adj_vertex, graph, dp)

        if vertex.max_length < adj_vertex.max_length + vertex.adj_dict[adj_vertex_id]:
            vertex.max_length = adj_vertex.max_length + vertex.adj_dict[adj_vertex_id]
            vertex.child = adj_vertex


def dag_longest_paths_dp(graph):

    for vertex_id in graph:
        vertex = graph[vertex_id]

        if not vertex.color:
            dfs_dp(vertex, graph)

    longest_path = 0

    for vertex_id in graph:
        vertex = graph[vertex_id]

        if longest_path < vertex.max_length:
            longest_path = vertex.max_length

    return longest_path
# --------------------------- End - Dynamic Programming Version ---------------------------


def dag_longest_paths(graph):

    sorted_vertices = sort_topologically(graph)

    for vertex in sorted_vertices:

        for adj_vertex_id in vertex.adj_dict:
            adj_vertex = graph[adj_vertex_id]

            if adj_vertex.d < vertex.d + vertex.adj_dict[adj_vertex_id]:
                adj_vertex.d = vertex.d + vertex.adj_dict[adj_vertex_id]
                adj_vertex.parent = vertex

    d_max = float('-inf')
    last_vertex = None
    for vertex_id, vertex in graph.items():
        if d_max < vertex.d and vertex_id != 'd0':
            d_max = vertex.d
            last_vertex = vertex

    return d_max, last_vertex


def sort_topologically(graph):

    sorted_vertices = list()

    # Loop thru vertices
    for vertex_id in graph:
        vertex = graph[vertex_id]

        if not vertex.color:
            sorted_vertices = dfs(vertex, sorted_vertices, graph)

    return sorted_vertices


def dfs(vertex, sorted_vertices, graph):

    vertex.color = True

    # Loop thru adjacent vertices
    for adj_vertex_id in vertex.adj_dict:
        adj_vertex = graph[adj_vertex_id]

        if not adj_vertex.color:
            dfs(adj_vertex, sorted_vertices, graph)

    sorted_vertices.insert(0, vertex)

    return sorted_vertices


if __name__ == '__main__':
    d0 = Vertex('d0', {'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1, 'f': -1})
    a = Vertex('a', {'b': -2, 'c': -2, 'e': -3})
    b = Vertex('b', {})
    c = Vertex('c', {})
    d = Vertex('d', {'f': -10})
    e = Vertex('e', {'b': -4, 'd': -1})
    f = Vertex('f', {})
    graph = {'e': e, 'd0': d0, 'c': c, 'd': d, 'a': a, 'b': b, 'f': f}

    d0.d = 0

    d_max, last_vertex = dag_longest_paths(graph)

    # dag_longest_paths_dp(graph)

    v = last_vertex
    longest_path = []

    while v:
        longest_path.insert(0, v.id)
        v = v.parent

    print(longest_path)
    print(f'Longest Path Length: {d_max}')
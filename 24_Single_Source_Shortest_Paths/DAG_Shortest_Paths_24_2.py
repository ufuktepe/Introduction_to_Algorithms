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


def dag_shortest_paths(graph):
    """
    Determines the parent and distance properties of each vertex in a DAG.
    First topologically sorts the vertices. Then iterates over each vertex in topological order and relaxes the edges.
    :param graph: the given graph dictionary
    :return: None
    """
    sorted_vertices = sort_topologically(graph)

    # Loop thru vertices in topological order
    for vertex in sorted_vertices:
        # Loop thru adjacent vertices
        for adj_vertex_id in vertex.adj_dict:
            adj_vertex = graph[adj_vertex_id]

            if adj_vertex.d > vertex.d + vertex.adj_dict[adj_vertex_id]:
                # Relax the edges
                adj_vertex.d = vertex.d + vertex.adj_dict[adj_vertex_id]
                adj_vertex.parent = vertex


def sort_topologically(graph):
    """
    Uses DFS to sort vertices of a given graph.
    :param graph: The given graph dictionary.
    :return: list of vertices sorted in topological order
    """

    sorted_vertices = list()

    # Loop through vertices
    for vertex_id in graph:
        vertex = graph[vertex_id]

        if not vertex.color:
            sorted_vertices = dfs(vertex, sorted_vertices)

    return sorted_vertices


def dfs(vertex, sorted_vertices):
    """
    Populates sorted_vertices in topological order.
    :param vertex: vertex object
    :param sorted_vertices: list of vertices sorted in topological order
    :return: sorted_vertices
    """

    vertex.color = True
    # Loop thru adjacent vertices
    for adj_vertex_id in vertex.adj_dict:
        adj_vertex = graph[adj_vertex_id]

        if not adj_vertex.color:
            dfs(adj_vertex, sorted_vertices)

    sorted_vertices.insert(0, vertex)

    return sorted_vertices


if __name__ == '__main__':
    # Define the graph (Chapter 24.2 in CLRS)
    r = Vertex('r', {'s': 5, 't': 3})
    s = Vertex('s', {'t': 2, 'x': 6})
    t = Vertex('t', {'x': 7, 'y': 4, 'z': 2})
    x = Vertex('x', {'y': -1, 'z': 1})
    y = Vertex('y', {'z': -2})
    z = Vertex('z', {})
    graph = {'x': x, 'y': y, 'z': z, 's': s, 't': t, 'r': r}

    # Set the root vertex
    s.distance = 0

    # Run the DAG Shortest Path Algorithm
    dag_shortest_paths(graph)

    # Print the results
    for vertex in graph.values():
        if vertex.parent is None:
            print(f'id:{vertex.id}, parent:None, distance:{vertex.distance}')
        else:
            print(f'id:{vertex.id}, parent:{vertex.parent.id}, distance:{vertex.distance}')













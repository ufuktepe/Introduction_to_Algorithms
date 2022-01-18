import sys

sys.setrecursionlimit(2 ** 17)


class Vertex:

    def __init__(self, id,  adj_vertices):
        self.id = id
        self.adj_vertices = adj_vertices
        self.visited = False

    def add_adj_vertex(self, v):
        self.adj_vertices.add(v)


class Graph:

    def __init__(self, vertices):
        self.vertices = vertices  # key:id, val:Vertex

    def get_vertex(self, id):
        try:
            return self.vertices[id]
        except KeyError:
            return None

    def reverse_graph(self):

        rev_vertex_dict = dict()

        for orig_vertex in self.vertices.values():

            # Crete the reversed vertex if it does not exist
            if orig_vertex.id not in rev_vertex_dict:
                rev_vertex_dict[orig_vertex.id] = Vertex(orig_vertex.id, set())

            for adj_vertex in orig_vertex.adj_vertices:
                # Create the reversed adjacent vertex if it does not exist
                if adj_vertex.id not in rev_vertex_dict:
                    rev_vertex_dict[adj_vertex.id] = Vertex(adj_vertex.id, set())

                rev_vertex_dict[adj_vertex.id].add_adj_vertex(rev_vertex_dict[orig_vertex.id])

        return Graph(rev_vertex_dict)

    def dfs(self, vertex, stack):

        vertex.visited = True

        for adj_vertex in vertex.adj_vertices:
            if not adj_vertex.visited:
                self.dfs(adj_vertex, stack)

        stack.append(vertex.id)

    def print_scc(self):
        stack = list()

        # First Pass. Populate the stack from the leaves to the root.
        for vertex in self.vertices.values():
            if not vertex.visited:
                self.dfs(vertex, stack)

        # Create a reversed graph
        g_rev = self.reverse_graph()

        # Second Pass.
        scc_list = list()

        while stack:
            vertex_id = stack.pop()

            # Get the vertex from the reversed graph
            vertex = g_rev.get_vertex(vertex_id)

            if not vertex.visited:
                scc = list()
                g_rev.dfs(vertex, scc)
                scc_list.append(scc)

        print(scc_list)

# Input Graph
adj_vertex_dict = {
                7: {1},
                4: {7},
                1: {4},
                9: {3, 7},
                6: {9},
                8: {5, 6},
                2: {8},
                5: {2},
                3: {6}
}

# Create a vertex dictionary
vertex_dict = dict()
for main_vertex_id, adj_vertices in adj_vertex_dict.items():
    # Create the main vertex if it does not exist
    if main_vertex_id not in vertex_dict:
        vertex_dict[main_vertex_id] = Vertex(main_vertex_id, set())

    # Iterate over each adjacent vertex
    for adj_vertex_id in adj_vertices:
        # Create the adjacent vertex if it does not exist
        if adj_vertex_id not in vertex_dict:
            vertex_dict[adj_vertex_id] = Vertex(adj_vertex_id, set())

        # Add the adjacent vertex to the main vertex
        vertex_dict[main_vertex_id].add_adj_vertex(vertex_dict[adj_vertex_id])

g = Graph(vertex_dict)

g.print_scc()











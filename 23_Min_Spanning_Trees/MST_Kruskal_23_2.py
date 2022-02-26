class Vertex:
    def __init__(self, id):
        self.id = id
        self.parent = None
        self.rank = 0


class Edge:
    def __init__(self, u, v, w):
        self.vertex_1 = u
        self.vertex_2 = v
        self.weight = w

    def __str__(self):
        return f'{self.vertex_1.id}-{self.vertex_2.id} (weight:{self.weight})'


class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = set()

    def add_edge(self, e):
        """
        Adds an edge to the graph. Also, adds the vertices of the edge to the graph if they are
        not already in the graph.
        :param e: Edge to be added
        :return: None
        """
        # Add the vertex_1 to the graph if it's not in the graph already
        if e.vertex_1 not in self.vertices:
            self.vertices.add(e.vertex_1)

        # Add the vertex_2 to the graph if it's not in the graph already
        if e.vertex_2 not in self.vertices:
            self.vertices.add(e.vertex_2)

        # Add the edge
        self.edges.add(e)

    def mst_kruskal(self):
        """
        Sorts the edges of the tree in non-decreasing order by weight. Then loops through each edge. If the vertices of
        the edge are in different trees merges the two trees and adds the edge to the minimum spanning tree.
        :return: minimum spanning tree
        """
        # Place each vertex in its own set
        for vertex in self.vertices:
            self.make_set(vertex)

        # Create a list of edges
        edge_list = list(self.edges)

        # Sort the edges in non-decreasing order by weight
        edge_list.sort(key=lambda x: x.weight)

        # Create the output mst graph
        mst = Graph()

        i = 0

        # Loop through each edge until the mst graph has n-1 edges where n is the number of vertices in the original
        # graph
        while len(mst.edges) < len(self.vertices) - 1:
            edge = edge_list[i]
            vertex_1 = edge.vertex_1
            vertex_2 = edge.vertex_2

            # If vertex_1 and vertex_2 are in different trees, merge the vertices to create a single tree. Then, add
            # the edge to the mst graph.
            if self.find_set(vertex_1) != self.find_set(vertex_2):
                self.union(vertex_1, vertex_2)
                mst.add_edge(edge)

            i += 1

        return mst

    def make_set(self, v):
        """
        Sets the parent of the given vertex to itself and its rank to zero. This is essentially a tree with one vertex.
        :param v: the given vertex
        :return: None
        """
        v.parent = v
        v.rank = 0

    def union(self, u, v):
        """
        Finds the roots of the sets containing vertices u and v and combines the two sets. The root with higher rank
        becomes the parent of the root with lower rank. If the two roots have equal rank, one of the roots is chosen
        arbitrarily as the parent and its rank is incremented.
        :param u: first given vertex
        :param v: second given vertex
        :return: None
        """
        u_root = self.find_set(u)
        v_root = self.find_set(v)

        if u_root == v_root:
            return

        if u_root.rank > v_root.rank:
            v_root.parent = u_root
        else:
            u_root.parent = v_root
            if u_root.rank == v_root.rank:
                v_root.rank += 1

    def find_set(self, v):
        """
        Recursively finds the root of the tree containing vertex v. Note that this method is a two-pass method and
        implements 'Path Compression'. It makes one pass to find the root, and as the recursion unwinds, it makes a
        second pass back down to update each vertex to point directly to the root.
        :param v: the given vertex
        :return: the root of the tree containing vertex v
        """
        if v.parent != v:
            v.parent = self.find_set(v.parent)
        return v.parent

    def __str__(self):
        str_repr = 'Edges:\n'
        for edge in self.edges:
            str_repr += f'{edge}\n'
        return str_repr


if __name__ == '__main__':
    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')
    f = Vertex('f')
    g = Vertex('g')
    h = Vertex('h')
    i = Vertex('i')
    vertices = {a, b, c, d, e, f, g, h, i}

    graph = Graph()
    graph.add_edge(Edge(a, b, 4))
    graph.add_edge(Edge(a, h, 8))
    graph.add_edge(Edge(b, h, 11))
    graph.add_edge(Edge(b, c, 8))
    graph.add_edge(Edge(h, i, 7))
    graph.add_edge(Edge(i, c, 2))
    graph.add_edge(Edge(h, g, 1))
    graph.add_edge(Edge(i, g, 6))
    graph.add_edge(Edge(g, f, 2))
    graph.add_edge(Edge(c, f, 4))
    graph.add_edge(Edge(f, e, 10))
    graph.add_edge(Edge(e, d, 9))
    graph.add_edge(Edge(d, f, 14))
    graph.add_edge(Edge(c, d, 7))

    mst = graph.mst_kruskal()
    print(mst)

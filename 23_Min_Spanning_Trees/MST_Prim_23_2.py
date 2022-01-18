from copy import deepcopy
from Min_Heapify import *
import sys


class Vertex:
    def __init__(self, id):
        self.id = id
        self.parent = None
        self.key = sys.maxsize
        self.adj = {}  # key=adj_vertex : val=edge weight

    def add_adj_vertex(self, other, weight):
        self.adj[other] = weight
        other.adj[self] = weight

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key


class Graph:
    def __init__(self, v):
        self.vertices = v
        
    def add_edge(self, vertex_1, vertex_2, weight):
        vertex_1.add_adj_vertex(vertex_2, weight)

    def mst_prim(self):
        min_pq = list(deepcopy(self.vertices))
        root = min_pq[0]
        root.key = 0

        build_min_heap(min_pq)

        mst = Graph(set())

        while min_pq:
            u = extract_min(min_pq)
            mst.vertices.add(u)

            # Loop through u's adjacent vertices
            for v, weight in u.adj.items():
                if v in min_pq and v.key > weight:
                    v.key = weight
                    v.parent = u

        return mst

    def __str__(self):
        str_repr = 'Edges:\n'
        for vertex in self.vertices:
            if vertex.parent is not None:
                str_repr += f'{vertex.id}-{vertex.parent.id} (weight:{vertex.key})\n'
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

    graph = Graph(vertices)
    graph.add_edge(a, b, 4)
    graph.add_edge(a, h, 8)
    graph.add_edge(b, h, 11)
    graph.add_edge(b, c, 8)
    graph.add_edge(h, i, 7)
    graph.add_edge(i, c, 2)
    graph.add_edge(h, g, 1)
    graph.add_edge(i, g, 6)
    graph.add_edge(g, f, 2)
    graph.add_edge(c, f, 4)
    graph.add_edge(f, e, 10)
    graph.add_edge(e, d, 9)
    graph.add_edge(d, f, 14)
    graph.add_edge(c, d, 7)

    mst = graph.mst_prim()
    print(mst)
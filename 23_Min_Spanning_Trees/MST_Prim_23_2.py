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

    # NOTE: Implement Fibonacci Heap to efficiently decrease the key of an item in the priority queue
    def mst_prim(self):
        """
        Creates a min priority queue from vertices based on the vertices' key attribute. The key attribute of a vertex
        is the minimum weight of any edge connecting that vertex to another vertex. All vertices that are not in the MST
        are in the min priority queue.
        :return:
        """
        # Deep copy the vertices
        min_pq = list(deepcopy(self.vertices))

        # Set the root of the MST to the first item of the min_pq
        root = min_pq[0]
        root.key = 0

        # Create a minimum priority queue
        build_min_heap(min_pq)

        # Create the output mst graph
        mst = Graph(set())

        # Extract the vertex that has the minimum key value from the heap one by one
        while min_pq:

            for n in min_pq:
                print(f'{n.id}{n.key}', end=' ')
            print('')

            u = extract_min(min_pq)
            print(f'Extracted : {u.id}')

            # Add the extracted vertex to the output mst graph
            mst.vertices.add(u)

            # Loop through u's adjacent vertices
            for v, weight in u.adj.items():
                print(f'Checking {v.id}{v.key} edge={weight}')
                # If v is not yet added to mst and if its key value is larger than the weight of the edge (u,v)
                # set its key to the weight of the edge (u,v) parent to u
                if v in min_pq and v.key > weight:
                    v.key = weight
                    v.parent = u
                    # Decrease the key of v in min_pq. This needs to be implemented using Fibonacci heaps for better
                    # performance!!!!

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
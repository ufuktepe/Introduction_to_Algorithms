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
        :return: the MST and its total cost
        """
        # Deep copy the vertices
        vertex_list = list(deepcopy(self.vertices))

        # Set the root of the MST to the first item of the min_pq
        root = vertex_list[0]
        root.key = 0

        # Create a minimum priority queue
        min_pq = MinHeap(vertex_list)

        # Create the output mst graph
        mst = Graph(set())

        # Total cost of the MST
        total = 0

        # Extract the vertex that has the minimum key value from the heap one by one
        while min_pq.lst:

            for n in min_pq.lst:
                print(f'{n.id}{n.key}', end=' ')
            print('')

            # Extract the root, takes O(log(n)) time
            u = min_pq.extract_min()
            print(f'Extracted : {u.id}')

            # Update the total cost
            total += u.key

            # Add the extracted vertex to the output mst graph
            mst.vertices.add(u)

            # Loop through u's adjacent vertices
            for v, weight in u.adj.items():
                print(f'Checking {v.id}{v.key} edge={weight}')
                # If v is not yet added to mst and if its key value is larger than the weight of the edge (u,v)
                # set its key to the weight of the edge (u,v) parent to u
                if v in min_pq.lst and v.key > weight:
                    v.key = weight
                    v.parent = u
                    # Find the index of v in the heap and decrease its key value.
                    v_idx = min_pq.idx_dict[v]
                    min_pq.heap_decrease_key(v_idx, weight)

        return mst, total

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
    vertices = [a, b, c, d, e, f, g, h, i]

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

    mst, total = graph.mst_prim()
    print(mst)
    print(f'Total Cost: {total}')
import copy
import networkx as nx
import random

class Vertex:
    def __init__(self, id):
        self.id = id
        self.key = float('-inf')
        self.parent = None
        self.adj = {}  # key=adj vertex : val=edge weight

    def add_adj_vertex(self, other, weight):
        self.adj[other] = weight
        other.adj[self] = weight

class Graph:
    def __init__(self, v):
        self.vertices = v
        self.edges = set()

    def add_edge(self, vertex_1, vertex_2, weight):
        vertex_1.add_adj_vertex(vertex_2, weight)
        self.edges.add((vertex_1.id, vertex_2.id))

    def find_max_vertex(self, max_st):
        max_dist = float('-inf')
        max_vertex= None

        for v in self.vertices:
            if v.key > max_dist and v not in max_st.vertices:
                max_dist = v.key
                max_vertex = v

        return max_vertex

    def remove_max_spanning_tree(self, root, edges):
        # Num of vertices
        n = len(self.vertices)

        root.key = 0

        # Create the output max spanning tree
        max_st = Graph(set())

        # Total cost of the MST
        total = 0

        for i in range(n):
            u = self.find_max_vertex(max_st)

            # Add the vertex to the max spanning tree
            max_st.vertices.add(u)
            total += u.key

            if u.parent:
                edge1 = (u.id, u.parent.id)
                edge2 = (u.parent.id, u.id)

                if edge1 in edges:
                    edges.remove(edge1)
                else:
                    edges.remove(edge2)

            # Loop through u's adjacent vertices
            for v, weight in u.adj.items():
                if v not in max_st.vertices and v.key < weight:
                    v.key = weight
                    v.parent = u

        return max_st, total

    def max_spanning_tree_edges(self, root):
        # Num of vertices
        n = len(self.vertices)

        root.key = 0

        # Create the set of vertices seen so far
        s = set()

        # Create the set of vertices seen so far
        m = set()

        for i in range(n):
            max_dist = float('-inf')
            u = None

            for v in self.vertices:
                if v.key > max_dist and v not in s:
                    max_dist = v.key
                    u = v

            # Add the vertex to the max spanning tree
            s.add(u)

            if u.parent:
                m.add((u.id, u.parent.id))

            # Loop through u's adjacent vertices
            for v, weight in u.adj.items():
                if v not in s and v.key < weight:
                    v.key = weight
                    v.parent = u

        return m

    def __str__(self):
        str_repr = 'Edges:\n'
        for vertex in self.vertices:
            if vertex.parent is not None:
                str_repr += f'{vertex.id}-{vertex.parent.id} (weight:{vertex.key})\n'
        return str_repr


def select(arr, k):
    """
    Select a pivot corresponding to the kth largest element in the array
    :param arr: Input array
    :param k: cardinality that represents the kth largest element in the array
    :return: The value of the kth largest elm
    """

    # Divide array into chunks of 5
    # chunks by taking i from 0 to 4, 5 to 9, 10 to 14, etc
    chunks = [arr[i : i+5] for i in range(0, len(arr), 5)]

    # sort each chunk
    sorted_chunks = [sorted(chunk) for chunk in chunks]

    # take the median of each chunk
    medians = [chunk[len(chunk) // 2] for chunk in sorted_chunks]

    # find the median of medians
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) // 2 - 1]
    else:
        pivot = select(medians, len(medians) // 2 - 1)

    # get the index of the pivot and create low and high arrays
    p, arr_low, arr_high = partition(arr, pivot)

    if k - 1 == len(arr_low):
        #select that pivot
        return pivot

    elif k - 1 < len(arr_low):
        #select a new pivot by looking on the left side of the partioning
        return select(arr_low, k)
    else:
        #select a new pivot by looking on the right side of the partioning
        return select(arr_high, k - (len(arr) - len(arr_high)))


def partition(arr, pivot):
    idx = 0
    arr_low = []
    arr_high = []
    found_pivot = False
    for i in range(len(arr)):
        if pivot > arr[i]:
            idx += 1
            arr_low.append(arr[i])
        elif pivot < arr[i]:
            arr_high.append(arr[i])
        elif found_pivot:
            arr_low.append(arr[i])
        else:
            found_pivot = True

    return idx, arr_low, arr_high



if __name__ == '__main__':
    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')
    vertices = [a, b, c, d, e]
    vertex_dict = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e}

    graph = Graph(vertices)
    graph.add_edge(a, b, 4)
    graph.add_edge(a, c, 3)
    graph.add_edge(a, d, 2)
    graph.add_edge(a, e, 1)
    graph.add_edge(b, c, 6)
    graph.add_edge(b, d, 7)
    graph.add_edge(b, e, 5)
    graph.add_edge(d, c, 12)
    graph.add_edge(e, c, 10)
    graph.add_edge(e, d, 11)

    edges = copy.deepcopy(graph.edges)

    # mst, total = graph.remove_max_spanning_tree(a, edges)
    mst = graph.max_spanning_tree_edges(a)
    print(mst)
    # print(f'Total Cost: {total}')

    edge_weights = []
    for edge in edges:
        v1_id = edge[0]
        v2_id = edge[1]

        v1 = vertex_dict[v1_id]
        v2 = vertex_dict[v2_id]
        w = v1.adj[v2]
        edge_weights.append(w)

    print(edge_weights)

    threshold = select(edge_weights, 5)

    for edge_weight in edge_weights:
        if edge_weight <= threshold:
            print(edge_weight)




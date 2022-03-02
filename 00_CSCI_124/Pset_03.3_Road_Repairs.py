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

    # # Create My graph
    # graph = Graph(set())
    # vertices = []
    #
    # # Create Networkx graph
    # G = nx.Graph()
    #
    # n = 400
    #
    # # Create vertices
    # for i in range(n):
    #     G.add_node(i)
    #     v = Vertex(str(i))
    #     graph.vertices.add(v)
    #     vertices.append(v)
    #
    # # Create edges
    # for i in range(n-1):
    #     for j in range(i+1, n):
    #         w = random.uniform(0, 1)
    #         G.add_edge(i, j, weight=w)
    #         graph.add_edge(vertices[i], vertices[j], w)
    #
    # # Networkx
    # mst = nx.algorithms.maximum_spanning_edges(G, algorithm="prim", data=True)
    # sum = 0
    # for edge in mst:
    #     sum += edge[2]['weight']
    # print(f'Networknx total cost: {sum}')

    mst, total = graph.remove_max_spanning_tree(a, edges)
    # print(mst)
    print(f'Total Cost: {total}')

    edge_weights = []
    for edge in edges:
        v1_id = edge[0]
        v2_id = edge[1]

        v1 = vertex_dict[v1_id]
        v2 = vertex_dict[v2_id]
        w = v1.adj[v2]
        edge_weights.append(w)

    print(edge_weights)

    treshold =




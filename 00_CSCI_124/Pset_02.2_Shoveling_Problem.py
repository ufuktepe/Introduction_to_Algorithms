class Vertex:
    def __init__(self, an_id):
        self.id = an_id
        self.visited = False
        self.d = None   # discovery time - timestamp for turning from White to Gray
        self.f = None   # finishing time - timestamp for turning from Gray to Black
        self.parent = None
        self.adj_edges = None

    def get_edge_to_vertex(self, other_vertex):
        for edge in self.adj_edges:
            if edge.v2 == other_vertex:
                return edge
        return None


class Edge:
    def __init__(self, v1, v2):
        self.id = v1.id + '-' + v2.id
        self.visited = 0
        self.v1 = v1
        self.v2 = v2

    def __str__(self):
        return self.v1.id + '-' + self.v2.id



def dfs(g):
    edges = []
    for vertex in g:
        if not vertex.color:
            print(1)
            edges = visit(vertex, edges)

    return edges


def visit(vertex, edges):
    vertex.color = True

    for edge in vertex.adj_edges:

        # Get the adjacent vertex
        if edge.v1 == vertex:
            adj_vertex = edge.v2
        else:
            adj_vertex = edge.v1

        opposite_edge = adj_vertex.get_edge_to_vertex(vertex)

        if opposite_edge.color == 0:
            edges.append(str(edge))
            edge.color = 1

            if not adj_vertex.color:
                edges = visit(adj_vertex, edges)

            edges.append(str(opposite_edge))
            opposite_edge.color = 1

    return edges


def visit_alt(vertex, edges):
    vertex.color = True

    for edge in vertex.adj_edges:

        # Get the adjacent vertex
        if edge.v1 == vertex:
            adj_vertex = edge.v2
        else:
            adj_vertex = edge.v1

        opposite_edge = adj_vertex.get_edge_to_vertex(vertex)

        if not adj_vertex.color:
            edges.append(str(edge))
            edge.color = 1
            edges = visit_alt(adj_vertex, edges)
            edges.append(str(opposite_edge))
            opposite_edge.color = 1

        elif edge.color == 0:
            edges.append(str(edge))
            edge.color = 1
            edges.append(str(opposite_edge))
            opposite_edge.color = 1


    return edges

if __name__ == '__main__':
    v1 = Vertex('v1')
    v2 = Vertex('v2')
    v3 = Vertex('v3')
    v4 = Vertex('v4')


    e12 = Edge(v1, v2)
    e13 = Edge(v1, v3)
    e14 = Edge(v1, v4)
    e21 = Edge(v2, v1)
    e23 = Edge(v2, v3)
    e24 = Edge(v2, v4)
    e31 = Edge(v3, v1)
    e32 = Edge(v3, v2)
    e34 = Edge(v3, v4)
    e41 = Edge(v4, v1)
    e42 = Edge(v4, v2)
    e43 = Edge(v4, v3)


    v1.adj_edges = [e12, e13, e14]
    v2.adj_edges = [e21, e23, e24]
    v3.adj_edges = [e31, e32, e34]
    v4.adj_edges = [e41, e42, e43]

    g = [v1, v3, v2, v4]

    print(dfs(g))
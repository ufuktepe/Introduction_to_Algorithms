class Vertex:
    def __init__(self, id):
        self.id = id
        self.p = self
        self.rank = 0
        self.circle = False


class Graph:
    def __init__(self):
        self.edges = set()

    def add_edge(self, edge):
        v1 = edge[0]
        v2 = edge[1]

        if (v1, v2) in self.edges or (v2, v1) in self.edges:
            return

        self.union(v1, v2)
        self.edges.add((v1, v2))

    def request_squad_name(self, v):
        v_root = self.find(v)

        if v_root.circle:
            return v_root.id + ' circle'
        return v_root.id

    def union(self, v1, v2):
        v1_root = self.find(v1)
        v2_root = self.find(v2)

        if v1_root == v2_root:
            if not v1_root.circle:
                v1_root.circle = True
            return

        if v1_root.rank > v2_root.rank:
            v2_root.p = v1_root
        else:
            v1_root.p = v2_root

            if v1_root.rank == v2_root.rank:
                v2_root.rank += 1

        return

    def find(self, v):
        if v.p != v:
            v.p = self.find(v.p)
        return v.p


if __name__ == '__main__':
    a = Vertex('A')
    b = Vertex('B')
    c = Vertex('C')
    d = Vertex('D')
    e = Vertex('E')
    f = Vertex('F')
    g = Vertex('G')
    h = Vertex('H')

    vertices = [a, b, c, d, e, f, g, h]
    graph = Graph()

    edges = [(a, b), (d, e), (e, c), (f, e), (d, c), (b, f), (h, g), (h, a)]

    for edge in edges:
        graph.add_edge(edge)

        for v in vertices:
            name = graph.request_squad_name(v)
            print(f'{v.id}: name:{name}')
        print(' ')
        print(' ')

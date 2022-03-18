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

        self.edges.add((v1, v2))

        return self.union(v1, v2)


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
            return False

        if v1_root.rank > v2_root.rank:
            v2_root.s = v1_root
            if v2_root.circle:
                v1_root.circle = True
        else:
            v1_root.s = v2_root
            if v1_root.rank == v2_root.rank:
                v2_root.rank += 1
            if v1_root.circle:
                v2_root.circle = True

        return True

    def find(self, v):
        if v.s != v:
            v.s = self.find(v.s)
        return v.s


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

    edges = [(a, b), (b, c), (c, a), (d, e), (c, d), (f, g), (h, f), (f, a)]

    count = 0

    for edge in edges:
        if graph.add_edge(edge):
            count += 1
            print(f'Count:{count}')

        if count == len(vertices) - 1:
            print('All vertices are connected')

        for v in vertices:
            name = graph.request_squad_name(v)
            print(f'{v.id}: name:{name}')
        print(' ')
        print(' ')


class Vertex:
    def __init__(self, an_id):
        self.id = an_id
        self.parent = None
        self.distance = float('inf')
        self.visited = False
        self.adj_dict = {}  # key=vertex : val=weight


def dfs(g, s):
    s.distance = 0
    dfs_visit(s)

    # add the missing edges
    c.adj_dict[d] = 1
    c.adj_dict[e] = 7

    # Relax each edge
    for v in g:
        for adj_v, weight in v.adj_dict.items():
            if adj_v.distance > v.distance + weight:
                print(f'Relaxed vertex {adj_v.id} using edge {v.id}-{adj_v.id}')


def dfs_visit(v):
    v.color = True

    for adj_v, weight in v.adj_dict.items():
        if not adj_v.color:
            adj_v.distance = v.distance + weight
            dfs_visit(adj_v)


if __name__ == '__main__':
    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')

    a.adj_dict[b] = 1
    a.adj_dict[c] = 2
    b.adj_dict[d] = 5
    d.adj_dict[e] = 2

    g = [b, c, a, d, e]

    dfs(g, a)


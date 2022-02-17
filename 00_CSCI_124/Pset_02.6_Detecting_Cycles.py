class Vertex:
    def __init__(self, an_id, an_adj_dict):
        self.id = an_id
        self.parent = None
        self.d = float('-inf')  # the length of the longest path to this vertex seen so far
        self.color = 'w'
        self.adj_dict = an_adj_dict  # key=id : val=weight

        self.max_length = 0  # Length of the longest path when starting from this vertex
        self.child = None



def dfs(graph):
    for v_id, v in graph.items():
        if v.color == 'w':
            if dfs_visit(v, graph):
                return True
    return False


def dfs_visit(v, graph):
    v.color = 'g'
    print(f'main vertex {v.id} {v.color}')

    for adj_v_id in v.adj_dict:
        adj_v = graph[adj_v_id]

        print(f'adj vertex {adj_v.id} {adj_v.color}')

        if adj_v.color == 'w':
            if dfs_visit(adj_v, graph):
                return True

        elif adj_v.color == 'g':
            return True

    v.color = 'b'

    return False





if __name__ == '__main__':
    a = Vertex('a', {'c': -2, 'e': -3})
    b = Vertex('b', {})
    c = Vertex('c', {})
    d = Vertex('d', {'f': -10})
    e = Vertex('e', {'b': -4, 'd': -1})
    f = Vertex('f', {})
    graph = {'e': e, 'c': c, 'd': d, 'a': a, 'b': b, 'f': f}

    print(dfs(graph))




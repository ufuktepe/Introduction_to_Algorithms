class Node:
    def __init__(self, i):
        self.id = i
        self.parent = None
        self.rank = 0
        self.visited = False
        self.adj_nodes = set()

    def add_adj_node(self, other):
        self.adj_nodes.add(other)
        other.adj_nodes.add(self)


class Graph:
    def __init__(self, v):
        # Set of vertices
        self.vertices = v

    def add_edge(self, u, v):
        """
        Adds an undirected edge between nodes u and v
        :param u: Node to be connected to v
        :param v: Node to be connected to u
        :return: None
        """
        u.add_adj_node(v)

    def dfs_visit_adj_nodes(self, v):
        """
        Recursively visits adjacent nodes in a DFS manner and combines the sets that contain v and adj_node by
        calling the union method.
        :param v: the given main node
        :return: None
        """
        v.color = True

        for adj_node in v.adj_nodes:
            if not adj_node.color:
                self.dfs_visit_adj_nodes(adj_node)
            if self.find_set(v) != self.find_set(adj_node):
                self.union(v, adj_node)

    def connected_components(self):
        """
        Initially places each node in its own set. Then for each node that is not visited calls dfs_visit_adj_nodes
        method to unite sets.
        :return: None
        """

        # Place each node in its own set
        for v in self.vertices:
            self.make_set(v)

        for v in self.vertices:
            if not v.color:
                self.dfs_visit_adj_nodes(v)

    def make_set(self, v):
        """
        Sets the parent of the given node to itself and its rank to zero. This is essentially a tree with one node.
        :param v: the given node
        :return: None
        """
        v.parent = v
        v.rank = 0

    def union(self, x, y):
        """
        Finds the roots of the sets containing nodes x and y and combines the two sets. The root with higher rank
        becomes the parent of the root with lower rank. If the two roots have equal rank, one of the roots is chosen
        arbitrarily as the parent and its rank is incremented.
        :param x: first given node
        :param y: second given node
        :return: None
        """
        x_root = self.find_set(x)
        y_root = self.find_set(y)

        if x_root == y_root:
            return

        if x_root.rank > y_root.rank:
            y_root.parent = x_root
        else:
            x_root.parent = y_root
            if x_root.rank == y_root.rank:
                y_root.rank += 1

    def find_set(self, x):
        """
        Recursively finds the root of the tree containing node x. Note that this method is a two-pass method and
        implements 'Path Compression'. It makes one pass to find the root, and as the recursion unwinds, it makes a
        second pass back down to update each node to point directly to the root.
        :param x: the given node
        :return: the root of the tree containing node x
        """
        if x.parent != x:
            x.parent = self.find_set(x.parent)
        return x.parent


if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')
    i = Node('i')
    j = Node('j')

    vertices = {a, b, c, d, e, f, g, h, i, j}
    graph = Graph(vertices)
    graph.add_edge(a, c)
    graph.add_edge(a, b)
    graph.add_edge(c, b)
    graph.add_edge(b, d)
    graph.add_edge(e, g)
    graph.add_edge(e, f)
    graph.add_edge(h, i)

    graph.connected_components()

    for node in graph.vertices:
        print(f'{node.id} parent:{node.parent.id} rank:{node.rank}')

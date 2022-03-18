class Vertex:
    def __init__(self, id):
        self.id = id
        self.adj = {}  # key=adj_vertex : val=dist

    def add_edge(self, other, dist):
        self.adj[other] = dist
        other.adj[self] = dist


def apsp(V):
    n =len(V)

    dp = [[0 if x==y else float('inf') for y in range(n)] for x in range(n)]

    # This is to reconstruct the paths
    r = [[None for y in range(n)] for x in range(n)]

    # Initialize dp for k=0 (0 intermediate nodes)
    for vertex in V:
        i = vertex.id
        for adj_vertex, dist in vertex.adj.items():
            j = adj_vertex.id
            dp[i][j] = dist

    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Distance between vertex i and j using vertex k
                ik = dp[i][k]
                kj = dp[k][j]
                new_dist = ik + kj

                current_dist = dp[i][j]

                if current_dist > new_dist:
                    dp[i][j] = new_dist
                    r[i][j] = k

    return dp, r


def print_path(r, i, j):
    mid = r[i][j]

    if mid is not None:
        print(mid)
        print_path(r, i, mid)


if __name__ == '__main__':
    v0 = Vertex(0)
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    v4 = Vertex(4)

    v0.add_edge(v1, 2)
    v0.add_edge(v2, 5)
    v1.add_edge(v2, 1)
    v1.add_edge(v3, 5)
    v2.add_edge(v3, 1)

    v4.add_edge(v0, 10)
    v4.add_edge(v2, 6)
    v4.add_edge(v3, 1)
    v4.add_edge(v1, 7)

    V = [v0, v1, v2, v3, v4]

    dp, r = apsp(V)

    print_path(r, 1, 4)
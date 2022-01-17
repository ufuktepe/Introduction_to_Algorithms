class Vertex:
    def __init__(self, an_id):
        self.id = an_id
        self.color = 'White'
        self.d = None   # discovery time - timestamp for turning from White to Gray
        self.f = None   # finishing time - timestamp for turning from Gray to Black
        self.parent = None
        self.adj = None


def dfs(g):
    """
    Loops through each vertex of graph g and if its color is White calls the dfs_visit method.
    @param g: given graph
    @return: None
    """
    # Define time
    time = 0
    # Loop through each vertex in the graph
    for vertex in g:
        if vertex.color == 'White':
            time = dfs_visit(vertex, time)


def dfs_visit(u, time):
    """
    Recursively visits each vertex
    @param u: the given source vertex.
    @param time: timestamp to identify the discovery and finishing times
    @return: time
    """

    # Increment time and record it as the discovery time for u
    time += 1
    u.d = time
    u.color = 'Gray'

    # Explore edges (u, v)
    for v in u.adj:
        if v.color == 'White':
            v.parent = u
            # Recursively visit deeper vertices
            time = dfs_visit(v, time)
            
    # Record the finishing time
    time += 1
    u.f = time
    u.color = 'Black'

    return time


# See the following tree in Chapter 22.2 of CLRS
v = Vertex('v')
r = Vertex('r')
s = Vertex('s')
w = Vertex('w')
t = Vertex('t')
u = Vertex('u')
x = Vertex('x')
y = Vertex('y')

v.adj = [r]
r.adj = [s, v]
s.adj = [r, w]
w.adj = [s, x, t]
t.adj = [w, x, u]
x.adj = [w, t, y, u]
u.adj = [t, x, y]
y.adj = [x, u]

g = [v, r, s, w, t, u, x, y]

dfs(g)

for vertex in g:
    if vertex.parent is None:
        print(f'ID:{vertex.id}, Discovery:{vertex.d}, Finish:{vertex.f}, Color:{vertex.color}, Parent:None')
    else:
        print(f'ID:{vertex.id}, Discovery:{vertex.d}, Finish:{vertex.f}, Color:{vertex.color}, Parent:{vertex.parent.id}')

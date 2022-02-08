class Vertex:
    def __init__(self, an_id):
        self.id = an_id
        self.color = 'White'
        self.distance = None
        self.parent = None
        self.adj = None


def print_path(s, v):
    """
    Prints the path from s to v
    @param s: source vertex
    @param v: destination vertex
    @return: None
    """
    if s == v:
        print(s.id)
    elif v.parent is None:
        print('No path exists.')
    else:
        print_path(s, v.parent)
        print(v.id)


def bfs(s):
    """
    Finds the distance and parent of each vertex wrt the given root vertex using breadth-first search.
    Initially the color property of the vertices are set to White (meaning they are not discovered yet)
    When they are discovered they are turned into 'Gray' meaning they might have undiscovered (White) adjacent vertices
    Once all adjacent vertices of a vertex are discovered, that vertex is turned into 'Black' (all neighbors are
    discovered)

    @param s: root (source) vertex
    @return: None
    """
    s.color = 'Gray'
    s.distance = 0

    # Queue of vertices. Invariant: includes only gray vertices
    queue = list()

    queue.append(s)

    while queue:

        # Pop the first vertex in the queue (FIFO)
        u = queue.pop(0)

        # Loop through adjacent vertices of u
        for v in u.adj:
            # If the adjacent vertex is White that means it has not been discovered yet
            if v.color == 'White':
                v.color = 'Gray'
                v.distance = u.distance + 1
                v.parent = u
                queue.append(v)
        u.color = 'Black'


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

bfs(s)

# vertices = [v, r, s, w, t, u, x, y]
#
# for vertex in vertices:
#     if vertex.parent is None:
#         print(f'ID:{vertex.id}, Dist:{vertex.distance}, Color:{vertex.color}, Parent:None')
#     else:
#         print(f'ID:{vertex.id}, Dist:{vertex.distance}, Color:{vertex.color}, Parent:{vertex.parent.id}')


print_path(s, v)

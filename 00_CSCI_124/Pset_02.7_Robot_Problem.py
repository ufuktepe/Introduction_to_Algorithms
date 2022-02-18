import heapq
from random import randint


class Robot:
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y


def get_next_pos(u, grid, dest):

    x_max = len(grid) - 1
    y_max = len(grid[0]) - 1

    positions_set = set()

    x1, y1, x2, y2 = u[0], u[1], u[2], u[3]

    r1_at_dest = False
    r2_at_dest = False

    # Check if robot 1 reached destination
    if x1 == dest[0] and y1 == dest[1]:
        r1_at_dest = True

    # Check if robot 2 reached destination
    if x2 == dest[2] and y2 == dest[3]:
        r2_at_dest = True

    # 1 moves right 2 moves up
    if x1 + 1 <= x_max and grid[x1 + 1][y1] and not r1_at_dest:
        x1_1 = x1 + 1
    else:
        x1_1 = x1
    if y2 + 1 <= y_max and grid[x2][y2 + 1] and not r2_at_dest:
        y2_1 = y2 + 1
    else:
        y2_1 = y2

    pos_1 = (x1_1, y1, x2, y2_1)

    # 1 moves up 2 moves left
    if y1 + 1 <= y_max and grid[x1][y1 + 1] and not r1_at_dest:
        y1_2 = y1 + 1
    else:
        y1_2 = y1
    if x2 - 1 >= 0 and grid[x2 - 1][y2] and not r2_at_dest:
        x2_2 = x2 - 1
    else:
        x2_2 = x2

    pos_2 = (x1, y1_2, x2_2, y2)

    # 1 moves left 2 moves down
    if x1 - 1 >= 0 and grid[x1 - 1][y1] and not r1_at_dest:
        x1_3 = x1 - 1
    else:
        x1_3 = x1
    if y2 - 1 >= 0 and grid[x2][y2 - 1] and not r2_at_dest:
        y2_3 = y2 - 1
    else:
        y2_3 = y2

    pos_3 = (x1_3, y1, x2, y2_3)

    # 1 moves down 2 moves right
    if y1 - 1 >= 0 and grid[x1][y1 - 1] and not r1_at_dest:
        y1_4 = y1 - 1
    else:
        y1_4 = y1
    if x2 + 1 <= x_max and grid[x2 + 1][y2] and not r2_at_dest:
        x2_4 = x2 + 1
    else:
        x2_4 = x2

    pos_4 = (x1, y1_4, x2_4, y2)

    positions_set.add(pos_1)
    positions_set.add(pos_2)
    positions_set.add(pos_3)
    positions_set.add(pos_4)

    return positions_set


def bfs(s, grid):

    queue = [s]
    possible_pos_set = set()
    possible_pos_set.add(s)

    while queue:
        u = queue.pop(0)

        if u[0] == 1 and u[1] == 0 and u[2] == 1 and u[3] == 1:
            x = 5

        adj = get_next_pos(u, grid, dest=(-1, -1, -1, -1))

        for v in adj:
            # if u != v:
            #     print(str(u)  + ' --> ' + str(v))

            if v[1] == 0 and v[2] == 1:
                x = 5

            if v not in possible_pos_set:
                possible_pos_set.add(v)
                queue.append(v)

                # print(f'{u[0]}{u[3]}-{u[1]}{u[2]}')

    return possible_pos_set


def dijkstra(root, dest):

    dist = {}
    dist[root] = 0
    prev = {}
    prev[root] = None

    pq = [(dist[root], root)]

    while pq:
        current_dist, vertex = heapq.heappop(pq)

        if vertex == dest:
            break

        adj_vertices = get_next_pos(vertex, grid, dest)

        for adj_vertex in adj_vertices:

            # Assign distances
            if adj_vertex not in dist:
                dist[adj_vertex] = float('inf')

            cost_1 = abs(adj_vertex[0] - vertex[0]) + abs(adj_vertex[1] - vertex[1])
            cost_2 = abs(adj_vertex[2] - vertex[2]) + abs(adj_vertex[3] - vertex[3])

            if dist[adj_vertex] > dist[vertex] + cost_1 + cost_2:
                dist[adj_vertex] = dist[vertex] + cost_1 + cost_2
                prev[adj_vertex] = vertex
                heapq.heappush(pq, (dist[adj_vertex], adj_vertex))

    return dist, prev


if __name__ == '__main__':
    x1 = randint(0, 10)
    y1 = randint(0, 10)
    x2 = randint(0, 10)
    y2 = randint(0, 10)

    x1 = 3
    y1 = 3
    x2 = 3
    y2 = 0

    grid = [
        [1, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]

    s = (x1, y1, x2, y2)
    possible_pos_set = bfs(s, grid)

    # max_num_vertices = 0
    # for x1 in range(2):
    #     for y1 in range(2):
    #         for x2 in range(2):
    #             for y2 in range(2):
    #                 s = (x1, y1, x2, y2)
    #
    #                 if grid[x1][y1] == 0 or grid[x2][y2] == 0:
    #                     continue
    #
    #                 possible_pos_set = bfs(s, grid)
    #                 if max_num_vertices <= len(possible_pos_set):
    #                     max_num_vertices = len(possible_pos_set)
    #                     print(f'{len(possible_pos_set)}    {x1} {y1} {x2} {y2}')

    # print
    for pos in possible_pos_set:
        # print(f'({pos[0]}, {pos[3]}) ({pos[1]}, {pos[2]})')
        print(f'({pos[0]}-{pos[1]}),({pos[2]}-{pos[3]})')

    print(len(possible_pos_set))

    # # Shortest path
    # s = (x1, y1, x2, y2)
    # dest = (1, 0, 1, 0)
    # dist, prev = dijkstra(s, dest)
    #
    # if dest in dist:
    #     v = dest
    #     path = []
    #
    #     while v:
    #         path.insert(0, v)
    #         v = prev[v]
    #
    #     for v in path:
    #         print(v)
    #     print(f'Dist:{dist[dest]}')





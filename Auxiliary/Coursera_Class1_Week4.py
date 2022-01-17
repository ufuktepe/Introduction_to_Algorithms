import copy
from random import randint

def min_cut(vertices):
    max_vertex_id = len(vertices) + 1
    while len(vertices) > 2:
        vertex_numbers = list()
        for vertex, adjacent_vertices in vertices.items():
            vertex_numbers.append(vertex)

        rand_num = randint(0, len(vertex_numbers) - 1)

        vertex_1 = vertex_numbers[rand_num]

        adjacent_vertices = vertices[vertex_1]

        rand_num = randint(0, len(adjacent_vertices) - 1)

        vertex_2 = adjacent_vertices[rand_num]

        new_adjacent_vertices = list()
        for v in adjacent_vertices:
            if v != vertex_1 and v != vertex_2:
                new_adjacent_vertices.append(v)

        for v in vertices[vertex_2]:
            if v != vertex_1 and v != vertex_2:
                new_adjacent_vertices.append(v)

        vertices[max_vertex_id] = new_adjacent_vertices

        del vertices[vertex_1]
        del vertices[vertex_2]

        # Update the adjacent vertices
        for v in new_adjacent_vertices:
            for i, adj_v in enumerate(vertices[v]):
                if adj_v == vertex_1 or adj_v == vertex_2:
                    vertices[v][i] = max_vertex_id

        max_vertex_id += 1

    for k, v in vertices.items():
        return len(v)


txt_file = open("/Users/burak/Downloads/sample.txt", 'r')

vertices = dict()

for line in txt_file:
    line_content = line.split()

    main_vertex = None
    for v in line_content:
        if main_vertex is None:
            main_vertex = int(v)
            vertices[main_vertex] = list()
        else:
            vertices[main_vertex].append(int(v))

# vertices[1] = [2, 4]
# vertices[2] = [1, 3, 4]
# vertices[3] = [2, 4]
# vertices[4] = [1, 2, 3]

min = None
for i in range(100):

    vertices_copy = copy.deepcopy(vertices)

    current_min = min_cut(vertices_copy)

    print(current_min)

    if min is None or current_min < min:
        min = current_min



print(min)
print("DONE")

from collections import defaultdict
import sys

sys.setrecursionlimit(2 ** 17)


class Graph:

    def __init__(self, adj_list):
        self.graph = adj_list

    def add_edge(self, u, v):
        self.graph[u].add(v)

    def reverse_graph(self):
        g = Graph(defaultdict(set))

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)

        return g

    def dfs(self, vertex, visited, scc):
        scc.append(vertex)
        visited[vertex] = True

        for i in self.graph[vertex]:
            if not visited[i]:
                self.dfs(i, visited, scc)

    def create_stack(self, vertex, visited, stack):
        visited[vertex] = True
        for i in self.graph[vertex]:
            if not visited[i]:
                self.create_stack(i, visited, stack)
        stack.append(vertex)

    def print_scc(self):
        stack = list()

        visited = defaultdict(bool)

        for i in self.graph:
            if not visited[i]:
                self.create_stack(i, visited, stack)

        g_rev = self.reverse_graph()

        # Second DFS
        scc_list = list()
        visited = defaultdict(bool)

        while stack:
            vertex = stack.pop()

            if not visited[vertex]:
                scc = list()
                g_rev.dfs(vertex, visited, scc)
                scc_list.append(scc)

        print(scc_list)
        return scc_list


adj_set = defaultdict(set,
            {7: {1},
             4: {7},
             1: {4},
             9: {7, 3},
             6: {9},
             8: {6, 5},
             2: {8},
             5: {2},
             3: {6}})


g = Graph(adj_set)

g.print_scc()











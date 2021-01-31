from math import inf


class BellmanFord(object):
    def __init__(self, graph, num_of_vertices):
        self.__graph = graph
        self.__num_of_vertices = num_of_vertices
        n = self.__num_of_vertices + 1
        self.__shortest_weights = [[0 for _ in range(n)] for _ in range(n)]
        self.__before_vertices = None

    def run(self, start_vertex, enable_path_trace=False):
        n = self.__num_of_vertices + 1
        if enable_path_trace:
            self.__before_vertices = [[None for _ in range(n)] for _ in range(n)]

        for i in range(n):  # iteration
            for j in range(1, n):  # destination
                # Initialize
                if i == 0:
                    if start_vertex == j:
                        self.__shortest_weights[start_vertex][i][j] = 0
                    else:
                        self.__shortest_weights[start_vertex][i][j] = inf
                        continue

                case1 = self.__shortest_weights[start_vertex][i - 1][j]
                w = None
                min_case2 = inf
                for ei in range(1, n):
                    if self.__graph[j][ei] is None:
                        continue
                    else:
                        tmp = self.__shortest_weights[i - 1][ei] + self.__graph[j][ei]
                        if min_case2 > tmp:
                            min_case2 = tmp
                            w = ei

                self.__shortest_weights[i][j] = min(case1, min_case2)
                if enable_path_trace:
                    self.__before_vertices[i][j] = w

                if start_vertex == j and i == self.__num_of_vertices:
                    if self.__shortest_weights[i - 1][j] != self.__shortest_weights[i][j] and \
                            self.__shortest_weights[i][j] < 0:
                        self.__shortest_weights = None
                        return

        return

    def get_shortest_weight(self, destination):
        if self.__shortest_weights is None:
            return None
        else:
            return self.__shortest_weights[self.__num_of_vertices - 1][destination]

    def get_shortest_path(self, destination):
        if self.__before_vertices is None:
            return None

        g = self.__before_vertices[self.__num_of_vertices]
        pre = g[destination]
        if pre is None:
            return None

        path = [destination]

        while True:
            if pre is None:
                break
            path.append(pre)
            pre = g[pre]

        path.reverse()
        return path

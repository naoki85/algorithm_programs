from math import inf
from heapq import heappush, heappop


class Dijkstra(object):
    def __init__(self, graph, num_nodes):
        self.__graph = graph
        self.__num_nodes = num_nodes
        self.__shortest_path = None
        self.__shortest_path_weights = None

    def run(self, start_node):
        shortest_weights = [inf for _ in range(self.__num_nodes + 1)]
        shortest_weights[start_node] = 0

        shortest_path = [[] for _ in range(self.__num_nodes + 1)]
        shortest_path[start_node] = [start_node]

        queue = [(0, start_node)]

        while len(queue) != 0:
            weight, node = heappop(queue)
            if shortest_weights[node] < weight:
                continue
            for t, w in self.__graph[node]:
                new_weight = shortest_weights[node] + w
                if new_weight < shortest_weights[t]:
                    shortest_weights[t] = new_weight
                    shortest_path[t] = shortest_path[node] + [t]
                    heappush(queue, (shortest_weights[t], t))

        self.__shortest_path_weights = shortest_weights
        self.__shortest_path = shortest_path
        return

    def get_shortest_weight(self, target):
        return self.__shortest_path_weights[target]

    def get_shortest_path(self, target):
        return self.__shortest_path[target]

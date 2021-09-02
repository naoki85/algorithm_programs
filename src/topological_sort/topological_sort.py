class TopologicalSort(object):
    def __init__(self, num_vertices, num_edges, edges):
        self.__num_vertices = num_vertices
        self.__num_edges = num_edges
        self.__edges = edges
        self.__G = [[] for _ in range(num_vertices)]
        self.__inbound = [0 for _ in range(num_vertices)]
        for i in range(num_edges):
            u, v = edges[i]
            self.__G[u].append(v)
            self.__inbound[v] += 1

    def run(self):
        sorted_vertices = []
        queue = []
        for i in range(self.__num_vertices):
            if self.__inbound[i] == 0:
                queue.append(i)

        while len(queue) > 0:
            v = queue.pop(0)

            for u in self.__G[v]:
                self.__inbound[u] -= 1
                if self.__inbound[u] == 0:
                    queue.append(u)
            sorted_vertices.append(v)

        if not self.is_dag():
            return False

        return sorted_vertices

    def is_dag(self):
        return all(x == 0 for x in self.__inbound)

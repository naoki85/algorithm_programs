# import sys

# sys.path.append('../')
from src.union_find.union_find import UnionFind


class Kosaraju(object):
    def __init__(self, number_of_nodes, edges):
        self.__visited = [False for _ in range(number_of_nodes + 1)]
        self.__scc = UnionFind(number_of_nodes)
        self.__stack = []
        self.__order = []
        self.__edges = edges
        self.__number_of_nodes = number_of_nodes

    def run(self):
        rev_edges = self.__reverse_edges()

        for node in range(self.__number_of_nodes, 0, -1):
            if not self.__visited[node]:
                self.__stack.append(node)

                while self.__stack:
                    done = True
                    s = self.__stack.pop()
                    if not self.__visited[s]:
                        self.__visited[s] = True
                        for nbr in rev_edges[s]:
                            if not self.__visited[nbr]:
                                self.__stack.append(s)
                                self.__stack.append(nbr)
                                done = False
                    if done:
                        self.__order.append(s)

        # Initialize again
        self.__visited = [False] * len(self.__visited)
        self.__stack = []
        self.__order.reverse()

        for node in self.__order:
            if self.__visited[node]:
                continue
            self.__stack.append(node)
            while self.__stack:
                s = self.__stack.pop()
                if self.__visited[s]:
                    continue
                self.__visited[s] = True
                self.__scc.union(node, s)
                for nbr in self.__edges[s]:
                    if not self.__visited[nbr]:
                        self.__stack.append(nbr)
        return

    def is_same(self, x, y):
        return self.__scc.is_same(x, y)

    def get_summary(self):
        summary = [0 for _ in range(self.__number_of_nodes + 1)]
        for node in range(1, self.__number_of_nodes + 1):
            p = self.__scc.find(node)
            summary[p] += 1
        return summary

    def __reverse_edges(self):
        rev_edges = [[] for _ in range(self.__number_of_nodes + 1)]
        for index in range(1, len(self.__edges)):
            for e in self.__edges[index]:
                rev_edges[e] += [index]
        return rev_edges

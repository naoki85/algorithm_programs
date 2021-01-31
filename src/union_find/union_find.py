class UnionFind(object):
    def __init__(self, num_of_nodes=1):
        self.__parents = [i for i in range(num_of_nodes + 1)]
        self.__rank = [0 for _ in range(num_of_nodes + 1)]

    def find(self, x):
        if self.__parents[x] == x:
            return x
        else:
            self.__parents[x] = self.find(self.__parents[x])
            return self.__parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.__rank[x] < self.__rank[y]:
                x, y = y, x
            if self.__rank[x] == self.__rank[y]:
                self.__rank[x] += 1
            self.__parents[y] = x

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def get_leaders(self):
        leaders = set()
        for a in set(self.__parents[1:]):
            if a == self.__parents[a]:
                leaders.add(a)
        return leaders

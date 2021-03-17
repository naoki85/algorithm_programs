class Lcs(object):
    def __init__(self, string, other):
        self.__string = string
        self.__other = other
        self.__cache = [[-1 for _ in range(len(self.__other) + 1)] for _ in range(len(self.__string) + 1)]

    def calc(self):
        len_string = len(self.__string)
        len_other = len(self.__other)
        return self.__recursive_calc(len_string, len_other)

    def __recursive_calc(self, x, y):
        if x == 0 and y == 0:
            return 0

        if self.__cache[x][y] != -1:
            return self.__cache[x][y]

        res = 0
        if x > 0:
            res = max(res, self.__recursive_calc(x - 1, y))

        if y > 0:
            res = max(res, self.__recursive_calc(x, y - 1))

        if x > 0 and y > 0 and self.__string[x - 1] == self.__other[y - 1]:
            res = max(res, self.__recursive_calc(x - 1, y - 1) + 1)

        self.__cache[x][y] = res
        return res


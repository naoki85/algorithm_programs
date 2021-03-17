class Lcs(object):
    def __init__(self, string, other):
        self.__string = string
        self.__other = other
        self.__cache = [[0 for _ in range(len(self.__other) + 1)] for _ in range(len(self.__string) + 1)]

    def calc(self):
        len_string = len(self.__string)
        len_other = len(self.__other)

        for x in range(len_string + 1):
            for y in range(len_other + 1):
                if x > 0:
                    self.__cache[x][y] = max(self.__cache[x][y], self.__cache[x - 1][y])

                if y > 0:
                    self.__cache[x][y] = max(self.__cache[x][y], self.__cache[x][y - 1])

                if x > 0 and y > 0 and self.__string[x - 1] == self.__other[y - 1]:
                    self.__cache[x][y] = max(self.__cache[x][y], self.__cache[x - 1][y - 1] + 1)

        return self.__cache[len_string][len_other]

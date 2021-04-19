import math


class Rotate2dArray(object):
    def __init__(self, array):
        self.__array = array
        x_size = len(self.__array)
        if x_size > 0:
            for y in array:
                y_size = len(y)
                if x_size != y_size:
                    raise Exception("inappropriate matrix size")

    def turn_left90(self):
        self.__transpose()
        self.__reverse()
        return self.__array

    def turn_left180(self):
        self.turn_left90()
        self.turn_left90()
        return self.__array

    def turn_left270(self):
        self.turn_left180()
        self.turn_left90()
        return self.__array

    def turn_right90(self):
        return self.turn_left270()

    def turn_right180(self):
        return self.turn_left180()

    def turn_right270(self):
        return self.turn_left90()

    def __reverse(self):
        self.__array.reverse()

    def __transpose(self):
        self.__array = list(map(list, zip(*self.__array)))

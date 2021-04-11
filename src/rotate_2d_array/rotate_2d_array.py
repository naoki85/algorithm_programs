import math


class Rotate2dArray(object):
    def __init__(self, array):
        self.__array = array
        self.__n = 0
        x_size = len(self.__array)
        if x_size > 0:
            y_size = len(self.__array[0])
            if x_size != y_size:
                raise Exception("inappropriate matrix size")
            self.__n = x_size

    def turn_left90(self):
        self.__right_down_diagram_rotation()
        self.__horizontal_rotation()
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

    def __horizontal_rotation(self):
        x_max = math.floor(self.__n / 2)
        for x in range(x_max):
            target_x = self.__n - 1 - x
            for y in range(self.__n):
                self.__array[target_x][y], self.__array[x][y] = self.__array[x][y], self.__array[target_x][y]

    def __right_down_diagram_rotation(self):
        for y in range(self.__n):
            for x in range(self.__n):
                if x >= y:
                    break
                self.__array[y][x], self.__array[x][y] = self.__array[x][y], self.__array[y][x]

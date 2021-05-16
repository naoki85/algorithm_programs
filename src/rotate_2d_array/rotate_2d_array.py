class Rotate2dArray(object):
    @classmethod
    def turn_left90(cls, array):
        transposed = cls.__transpose(array)
        return cls.__reverse(transposed)

    @classmethod
    def turn_left180(cls, array):
        rotated = cls.turn_left90(array)
        return cls.turn_left90(rotated)

    @classmethod
    def turn_left270(cls, array):
        rotated = cls.turn_left180(array)
        return cls.turn_left90(rotated)

    @classmethod
    def turn_right90(cls, array):
        return cls.turn_left270(array)

    @classmethod
    def turn_right180(cls, array):
        return cls.turn_left180(array)

    @classmethod
    def turn_right270(cls, array):
        return cls.turn_left90(array)

    @classmethod
    def __reverse(cls, array):
        return list(reversed(array))

    @classmethod
    def __transpose(cls, array):
        x_size = len(array)
        if x_size > 0:
            for y in array:
                y_size = len(y)
                if x_size != y_size:
                    raise Exception("inappropriate matrix size")

        return list(map(list, zip(*array)))

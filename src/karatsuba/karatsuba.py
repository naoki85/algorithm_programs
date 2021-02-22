import math


class Karatsuba(object):
    @staticmethod
    def multiplication(a, b):
        sign = 1
        if (a < 0 and b >= 0) or (a >= 0 and b < 0):
            sign = -1
        abs_a = abs(a)
        abs_b = abs(b)
        len_a = len(str(abs_a))
        len_b = len(str(abs_b))

        if len_a <= 2 or len_b <= 2:
            return a * b

        if len_a >= len_b:
            split = math.ceil(len_a / 2)
        else:
            split = math.ceil(len_b / 2)
        x1, x0 = Karatsuba.split_number(abs_a, split)
        y1, y0 = Karatsuba.split_number(abs_b, split)
        c = 10 ** split

        if split <= 2:
            z2 = x1 * y1
            z0 = x0 * y0
            z1 = z2 + z0 - ((x1 - x0) * (y1 - y0))
            ret = z2 * c ** 2 + z1 * c + z0
            return sign * ret

        z2 = Karatsuba.multiplication(x1, y1)
        z0 = Karatsuba.multiplication(x0, y0)
        diff = Karatsuba.multiplication((x1 - x0), (y1 - y0))
        z1 = z2 + z0 - diff
        ret = z2 * c ** 2 + z1 * c + z0
        return sign * ret

    @staticmethod
    def split_number(a, n):
        operator = -1 if a < 0 else 1

        str_a = str(abs(a))
        sep = len(str_a) - n
        x1 = operator * int(str_a[:sep])
        x0 = int(str_a[sep:])
        return x1, x0

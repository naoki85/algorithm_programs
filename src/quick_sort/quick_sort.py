class QuickSort(object):
    @classmethod
    def exec(cls, array, pattern='first'):
        if len(array) <= 1:
            return array
        elif len(array) == 2:
            if array[0] > array[1]:
                array = cls.__swap(array, 0, 1)
            return array
        array = cls.__choose_pivot(array, pattern)
        left, right = cls.__partition(array, 0, len(array))
        left = cls.exec(left, pattern)
        right = cls.exec(right, pattern)
        return left + [array[0]] + right

    @classmethod
    def __choose_pivot(cls, array, pattern):
        if pattern == 'last':
            length = len(array) - 1
            return cls.__swap(array, 0, length)
        elif pattern == 'middle':
            length = len(array)
            first = array[0]
            last = array[length - 1]
            if length % 2 == 1:
                border = int(length / 2)
            else:
                border = int(length / 2) - 1
            middle = array[border]
            a = cls.exec([first, last, middle], 'first')
            if a[1] == first:
                return cls.__choose_pivot(array, 'first')
            elif a[1] == last:
                return cls.__choose_pivot(array, 'last')
            else:
                return cls.__swap(array, 0, border)
        else:
            return array

    @classmethod
    def __swap(cls, array, i, l):
        ith = array[i]
        lth = array[l]
        array[i] = lth
        array[l] = ith
        return array

    @classmethod
    def __partition(cls, array, l, r):
        p = array[l]
        i = l + 1
        for j in range(i, r):
            if array[j] < p:
                array = cls.__swap(array, j, i)
                i += 1

        left = array[l + 1:i]
        right = array[i:]
        if len(left) > 1:
            left = [left[len(left) - 1]] + left[:(len(left) - 1)]
        return left, right

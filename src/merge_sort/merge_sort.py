import math

class MergeSort(object):
    @classmethod
    def exec(cls, array):
        length = len(array)
        if length == 1:
            return array
        if length == 2:
            if array[0] > array[1]:
                return [array[1], array[0]]
            else:
                return array

        half_size = int(math.ceil(length / 2))
        left_array = cls.exec(array[:half_size])
        right_array = cls.exec(array[half_size:])
        merged_array = cls.merge_and_swap(left_array, right_array)

        return merged_array

    @classmethod
    def merge_and_swap(cls, left, right):
        sorted_list = []
        length = len(left) + len(right)
        l = 0
        r = 0
        for i in range(length):
            if r >= len(right) or (l < len(left) and left[l] < right[r]):
                sorted_list.append(left[l])
                l += 1
            else:
                sorted_list.append(right[r])
                r += 1
        return sorted_list

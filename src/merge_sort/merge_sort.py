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

# sample = [1, 3, 5, 2, 4, 6]
# sorted, count = sort_and_count(sample, len(sample))
# if count != 3:
#     print('mismatch: expected: %s, actual: %s' % (count, 3))
#     raise Exception
#
# print('========================')
#
# sample = [1,5,3,2,4]
# sorted, count = sort_and_count(sample, len(sample))
# if count != 4:
#     print('mismatch: expected: %s, actual: %s' % (count, 4))
#     raise Exception
#
#
# print('========================')
#
# sample = [1,6,3,2,4, 5]
# sorted, count = sort_and_count(sample, len(sample))
# if count != 5:
#     print('mismatch: expected: %s, actual: %s' % (count, 5))
#     raise Exception
#
# sample = [9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0]
# sorted, count = sort_and_count(sample, len(sample))
# print(sorted)
# print(count)
# if count != 56:
#     print('mismatch: expected: %s, actual: %s' % (count, 56))
#     raise Exception
#
# sample = [37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45]
# sorted, count = sort_and_count(sample, len(sample))
# if count != 590:
#     print('mismatch: expected: %s, actual: %s' % (count, 590))
#     raise Exception
#
# sample = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]
# sorted, count = sort_and_count(sample, len(sample))
# if count != 2372:
#     print('mismatch: expected: %s, actual: %s' % (count, 2372))
#     raise Exception
#
# #
# # print(count)
# # os.exit()
# sample = [1, 3, 6, 9, 4, 2, 8, 7]
#
# sorted, count = sort_and_count(sample, len(sample))
# # print(sorted)
# # print(count)
#
# # os.exit()
#
#
# file_path = '/Users/yoneyamanaoki/Desktop/algorisms_specialization/week2/input_array.txt'
# input = []
# with open(file_path) as f:
#     for line in f:
#         input.append(int(line.rstrip('\n')))
#
# print(len(input))
# sorted, count = sort_and_count(input, len(input))
# print(len(sorted))
# print(count)
# # 2499405460
# # 1198233847

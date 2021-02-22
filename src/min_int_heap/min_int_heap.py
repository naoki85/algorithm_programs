class MinIntHeap(object):
    def __init__(self):
        self.__capacity = 10
        self.__size = 0
        self.__items = [0] * self.__capacity

    def __get_left_child_index(self, parent_index):
        return 2 * parent_index + 1

    def __get_right_child_index(self, parent_index):
        return 2 * parent_index + 2

    def __get_parent_index(self, child_index):
        return int((child_index - 1) / 2)

    def __has_left_child(self, index):
        return self.__get_left_child_index(index) < self.__size

    def __has_right_child(self, index):
        return self.__get_right_child_index(index) < self.__size

    def __has_parent(self, index):
        return self.__get_parent_index(index) >= 0

    def __left_child(self, index):
        return self.__items[self.__get_left_child_index(index)]

    def __right_child(self, index):
        return self.__items[self.__get_right_child_index(index)]

    def __parent(self, index):
        return self.__items[self.__get_parent_index(index)]

    def __swap(self, index, other_index):
        self.__items[index], self.__items[other_index] = self.__items[other_index], self.__items[index]

    def __ensure_extra_capacity(self):
        if self.__size == self.__capacity:
            self.__items += [0] * self.__capacity * 2
            self.__capacity *= 2

    def peek(self):
        if self.__size == 0:
            raise IllegalStateException
        return self.__items[0]

    def poll(self):
        if self.__size == 0:
            raise IllegalStateException
        item = self.__items[0]
        self.__items[0] = self.__items[self.__size - 1]
        self.__size -= 1
        self.__heapify_down()
        return item

    def add(self, item):
        self.__ensure_extra_capacity()
        self.__items[self.__size] = item
        self.__size += 1
        self.__heapify_up()

    def __heapify_up(self):
        index = self.__size - 1
        while (self.__has_parent(index) and self.__parent(index) > self.__items[index]):
            self.__swap(self.__get_parent_index(index), index)
            index = self.__get_parent_index(index)

    def __heapify_down(self):
        index = 0
        while self.__has_left_child(index):
            smaller_child_index = self.__get_left_child_index(index)
            if self.__has_right_child(index) and self.__right_child(index) < self.__left_child(index):
                smaller_child_index = self.__get_right_child_index(index)

            if self.__items[index] < self.__items[smaller_child_index]:
                break
            else:
                self.__swap(index, smaller_child_index)
            index = smaller_child_index

    def print_items(self):
        print(self.__items)


class IllegalStateException(Exception):
    pass

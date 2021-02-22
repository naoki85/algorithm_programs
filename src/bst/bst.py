class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, new_value):
        if new_value <= self.value:
            if self.left == None:
                self.left = Node(new_value)
            else:
                self.left.insert(new_value)
        else:
            if self.right == None:
                self.right = Node(new_value)
            else:
                self.right.insert(new_value)

    def contains(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

    def find_value_from_order(self, order, now_index):
        result = None
        index = now_index
        if self.left is not None:
            result, index = self.left.find_value_from_order(order, index)
        if result is not None:
            return result, index
        index += 1
        if index == order:
            return self.value, index
        if self.right is not None:
            result, index = self.right.find_value_from_order(order, index)
        return result, index


class Bst(object):
    def __init__(self, value):
        root = Node(value)
        self.__queue = [value]
        self.__root = root

    def insert(self, new):
        self.__queue.append(new)
        self.__root.insert(new)

    def contains(self, number):
        return self.__root.contains(number)

    def find_value_from_order(self, order):
        return self.__root.find_value_from_order(order, 0)

from src.balanced_binary_search_tree.balanced_binary_search_tree import BalancedBinarySearchTree
from src.utils.main import assert_equals

if __name__ == '__main__':
    b = BalancedBinarySearchTree(5)
    b.append(3)
    b.append(20)
    b.append(5)
    b.append(10)
    b.append(13)
    b.append(8)
    b.delete(20)
    assert_equals(10, b.find_l(12))
    assert_equals(8, b.find_r(5))

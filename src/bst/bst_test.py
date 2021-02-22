from src.bst.bst import Bst

if __name__ == '__main__':
    b = Bst(8)
    if b.contains(8) is not True:
        print('mismatch: expected: %s, actual: %s' % (True, b.contains(8)))
        raise Exception

    b.insert(4)
    b.insert(10)
    res = b.find_value_from_order(3)
    if res[0] != 10:
        print('mismatch: expected: %s, actual: %s' % (10, res[0]))
        raise Exception

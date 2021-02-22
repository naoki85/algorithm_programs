from src.min_int_heap.min_int_heap import MinIntHeap

if __name__ == '__main__':
    h = MinIntHeap()
    h.add(10)
    h.add(15)
    h.add(20)
    h.add(8)
    a = h.poll()

    if 8 != a:
        print('mismatch: expected: %s, actual: %s' % (8, a))
        raise Exception

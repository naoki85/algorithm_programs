from union_find import UnionFind

if __name__ == '__main__':
    uf = UnionFind(4)
    uf.union(1, 2)
    uf.union(3, 4)
    uf.union(1, 3)
    output = set()
    output.add(1)

    if uf.get_leaders() != output:
        print('mismatch: expected: %s, actual: %s' % (output, uf.get_leaders()))
        raise Exception

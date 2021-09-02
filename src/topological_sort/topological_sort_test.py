from topological_sort import TopologicalSort


if __name__ == '__main__':
    number_of_vertices = 6
    number_of_edges = 6
    edges = [[0, 1], [1, 2], [3, 1], [3, 4], [4, 5], [5, 2]]

    ts = TopologicalSort(number_of_vertices, number_of_edges, edges)
    sorted_list = ts.run()
    expected = [0, 3, 1, 4, 5, 2]
    if sorted_list != expected:
        print('mismatch: expected: %s, actual: %s' % (expected, sorted_list))
        raise Exception

    number_of_vertices = 3
    number_of_edges = 3
    edges = [[2, 1], [1, 0], [0, 1]]

    ts = TopologicalSort(number_of_vertices, number_of_edges, edges)
    sorted_list = ts.run()
    expected = False
    if sorted_list != expected:
        print('mismatch: expected: %s, actual: %s' % (expected, sorted_list))
        raise Exception

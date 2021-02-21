import math
from bellman_ford import BellmanFord


def get_test_data():
    return [
        {'number_of_vertices': 4, 'number_of_edges': 3, 'edges': [[None, None, None, None, None], [None, None, None, None, None], [None, -6, None, None, None], [None, 44, -6, None, None], [None, None, None, None, None]], 'output': -12}
    ]


if __name__ == '__main__':
    test_data = get_test_data()
    for t in range(len(test_data)):
        test = test_data[t]
        edges = test['edges']
        number_of_vertices = test['number_of_vertices']
        number_of_edges = test['number_of_edges']
        output = test['output']

        bf = BellmanFord(edges, number_of_vertices)
        bf.run(1)
        min_shortest_weight = math.inf
        for i in range(2, number_of_vertices + 1):
            tmp = bf.get_shortest_weight(i)
            if tmp is None:
                continue
            if min_shortest_weight > tmp:
                min_shortest_weight = tmp

        if output != min_shortest_weight:
            print('mismatch: test no: %s, expected: %s, actual: %s' % (t, output, min_shortest_weight))
            raise Exception

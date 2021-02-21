from kosaraju import Kosaraju


def get_test_data():
    return [
        {'input': [[], [2], [1], [6], [], [8], [5], [3], [7]], 'number_of_nodes': 8, 'output': [5, 2, 1, 0, 0]},
        {'input': [[], [3], [7], [2], [1], [8], [], [5], [4]], 'number_of_nodes': 8, 'output': [7, 1, 0, 0, 0]}
    ]


if __name__ == '__main__':
    test_data = get_test_data()
    for t in range(len(test_data)):
        test = test_data[t]
        edges = test['input']
        number_of_nodes = test['number_of_nodes']
        output = test['output']

        kosaraju = Kosaraju(number_of_nodes, edges)
        kosaraju.run()
        summary = kosaraju.get_summary()
        summary.sort(reverse=True)
        result = summary[:5]

        for num in range(0, 5):
            if output[num] != result[num]:
                print('mismatch: test no: %s, expected: %s, actual: %s' % (t, output, result))
                raise Exception

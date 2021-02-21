import glob
import os
import re

from dijkstra import Dijkstra
from src.utils import main as utils


def parse_input_data(lines, number_of_vertices):
    graph = [[] for i in range(number_of_vertices + 1)]

    for line in lines:
        l = line.split("\t")
        vertex = int(l[0])
        for s in l[1:]:
            if len(s) == 0:
                continue
            e = s.split(',')
            graph[vertex] += [(int(e[0]), int(e[1]))]
    return graph


def parse_output_data(line):
    l = line.split(',')
    return list(map(int, l))


if __name__ == '__main__':
    input_file_pattern = 'input_*.txt'
    regexp = r'input_(\d*).txt'
    input_file_paths = glob.glob(input_file_pattern)
    for input_file_path in input_file_paths:
        j = re.findall(regexp, input_file_path)[0]
        output_file_path = 'output_%s.txt' % j
        input_data = utils.load_file(os.path.abspath(input_file_path))
        output_data = utils.load_file(os.path.abspath(output_file_path))

        graph = parse_input_data(input_data, 200)
        expected = parse_output_data(output_data[0])
        d = Dijkstra(graph, 200)
        d.run(1)

        target_keys = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
        for key in range(len(target_keys)):
            result = d.get_shortest_weight(target_keys[key])
            if expected[key] != result:
                print('mismatch: test no: %s, expected: %s, actual: %s' % (key, expected[key], result))
                raise Exception

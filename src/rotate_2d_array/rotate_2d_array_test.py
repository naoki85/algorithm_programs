from rotate_2d_array import Rotate2dArray


def test_left90(t, e):
    res = Rotate2dArray.turn_left90(t)

    if res == e:
        print("Test n = '%s' was successful." % len(res))
    else:
        raise Exception("Test n = '%s' failed. expected: %s, actual: %s" % (len(res), e, res))


if __name__ == '__main__':
    test_matrix = []
    expected = []
    test_left90(test_matrix, expected)

    test_matrix = [[1]]
    expected = [[1]]
    test_left90(test_matrix, expected)

    test_matrix = [[1, 2], [3, 4]]
    expected = [[2, 4], [1, 3]]
    test_left90(test_matrix, expected)

    test_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
    test_left90(test_matrix, expected)

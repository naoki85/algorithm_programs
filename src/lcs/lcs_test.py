from lcs import Lcs

if __name__ == '__main__':
    first_string = 'SOFT'
    second_string = 'OFF'
    output = 2
    lcs = Lcs(first_string, second_string)
    res = lcs.calc()

    if res != output:
        print('mismatch: expected: %s, actual: %s' % (output, res))
        raise Exception

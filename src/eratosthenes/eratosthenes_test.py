from eratosthenes import Eratosthenes

if __name__ == '__main__':
    test_cases = {
        "0": [],
        "1": [],
        "2": [2],
        "3": [2, 3],
        "10": [2, 3, 5, 7],
        "100": [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    }

    for n in test_cases:
        prime_numbers = Eratosthenes.search(int(n))
        expected = sorted(test_cases[n])
        if prime_numbers != expected:
            print('mismatch: expected: %s, actual: %s' % (expected, prime_numbers))
            raise Exception

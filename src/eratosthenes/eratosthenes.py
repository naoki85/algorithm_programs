class Eratosthenes(object):
    @classmethod
    def search(cls, n):
        p = [i for i in range(n + 1)]
        for i in p[3:]:
            if p[i] % 2 == 0:
                p[i] = 0

        square_n = n ** (1/2)
        for i in range(3, n):
            if i > square_n:
                break
            if p[i] == 0:
                continue
            for j in range(i, n + 1, 2):
                if i * j >= n + 1:
                    continue
                p[i * j] = 0

        primes = sorted(list(set(p)))[2:]
        return primes

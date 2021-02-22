from src.karatsuba.karatsuba import Karatsuba

if __name__ == '__main__':
    a = 3141592653589793238462643383279502884197169399375105820974944592  # 64-digits
    b = 2718281828459045235360287471352662497757247093699959574966967627  # 64-digits

    ans = a * b
    ans2 = Karatsuba.multiplication(a, b)
    if ans != ans2:
        print('mismatch: expected: %s, actual: %s' % (ans, ans2))
        raise Exception

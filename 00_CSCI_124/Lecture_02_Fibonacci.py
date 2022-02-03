import sys
from time import time

sys.setrecursionlimit(20000)


def fibonacci_iterative(n):
    lst = [0, 1]

    for i in range(2, n + 1):
        lst.append(lst[i - 1] + lst[i - 2])
        # lst.append((lst[i - 1] + lst[i - 2]) % 65536)

    return lst[n]


def fibonacci_recursive(n):
    if n < 2:
        return n

    # return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

    return (fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)) % 65536


def fibonacci_matrix(n):
    f = [1, 1, 1, 0]
    return matrix_power(f, n)[1]


def matrix_multiply(m1, m2):
    a, b, c, d = m1
    x, y, z, w = m2

    return (
        a * x + b * z,
        a * y + b * w,
        c * x + d * z,
        c * y + d * w
    )

    # return (
    #     (a * x + b * z) % 65536,
    #     (a * y + b * w) % 65536,
    #     (c * x + d * z) % 65536,
    #     (c * y + d * w) % 65536
    # )


def matrix_power(f, m):
    if m == 0:
        return [1, 0, 0, 1]
    elif m == 1:
        return f
    else:
        b = f
        n = 2
        while n <= m:
            # Repeatedly square b until n > m
            b = matrix_multiply(b, b)
            n = n * 2

        # add on the remainder
        r = matrix_power(f, m-n//2)
        return matrix_multiply(b, r)


if __name__ == '__main__':

    start = time()

    n = 10**6

    # print(fibonacci_recursive(n))
    # print(fibonacci_iterative(n))
    print(fibonacci_matrix(n))


    # x = 0
    # n = 10
    #
    # while x <= 2**31:
    #     x = fibonacci_matrix(n)
    #     n += 1
    #     print(n)
    #
    # print(x)


    print(time() - start)

    # thread = threading.Timer(2, fibonacci_matrix)
    # thread.start()
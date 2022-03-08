import sys
sys.setrecursionlimit(2000)

def karatsuba(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        m = max(len(str(x)),len(str(y)))
        m2 = m // 2

        a = x // 10**(m2)
        b = x % 10**(m2)
        c = y // 10**(m2)
        d = y % 10**(m2)

        z0 = karatsuba(b,d)
        z1 = karatsuba((a+b),(c+d))
        z2 = karatsuba(a,c)

        return (z2 * 10**(2*m2)) + ((z1 - z2 - z0) * 10**(m2)) + (z0)


def karatsuba3(x, y):
    n_x = len(str(x))
    y_x = len(str(y))

    if len(str(x)) < 3 or len(str(y)) < 3:
        return x*y
    else:
        m = max(len(str(x)), len(str(y)))
        s = int(m / 3)

        a = int(str(x)[:n_x - 2*s])
        b = int(str(x)[n_x - 2*s: n_x - s])
        c = int(str(x)[n_x - s:])

        d = int(str(y)[:y_x - 2*s])
        e = int(str(y)[y_x - 2*s: y_x - s])
        f = int(str(y)[y_x - s:])

        ad = karatsuba3(a, d)
        be = karatsuba3(b, e)
        cf = karatsuba3(c, f)

        p = karatsuba3(a + b, e + d) - ad - be
        q = karatsuba3(a + c, d + f) - ad - cf
        r = karatsuba3(b + c, e + f) - be - cf

        return (ad * 10**(4*s)) + (be * 10**(2*s)) + cf + p * 10**(3*s) + q * 10**(2*s) + r * 10**(s)


if __name__ == '__main__':
    print(karatsuba3(123456, 659782))
import gmpy2


def fermat_factorization(n):
    a = gmpy2.isqrt(n)
    b2 = gmpy2.square(a) - n
    while not gmpy2.is_square(b2):
        a += 1
        b2 = gmpy2.square(a) - n
    p = a + gmpy2.isqrt(b2)
    q = a - gmpy2.isqrt(b2)
    return int(p), int(q)


n = 476714679652321667
p, q = fermat_factorization(n)

print("p: ", p)
print("q: ", q)

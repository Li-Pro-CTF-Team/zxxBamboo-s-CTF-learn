import random
from gmpy2 import invert


def gcd(m, n):
    if n == 0:
        return x
    else:
        return gcd(n, m % n)


def husu(n):  # 随机选取与n互素的数
    m = random.randint(0, n)
    if gcd(m, n) == 1:
        return m
    return husu(n)


p = 1553
g = 3
m = 541
x = 423
# h = husu(p-1)
h = 121
b = pow(g, h, p)  # β
# k = husu(p-1)
k = 133
r2 = pow(b, k, p)  # r'
# a = husu(p-1)
a = 599  # α
r = pow(r2, a, p)
r_ni = invert(r, p - 1)  # 求逆
m2 = (m * r2 * r_ni) % (p - 1)  # m'
k_ni = invert(k, p - 1)
s2 = (k_ni * (m2 * x - r2)) % (p - 1)  # s'
a_ni = invert(a, p - 1)
h_ni = invert(h, p - 1)
r2_ni = invert(r2, p - 1)
s = (a_ni * h_ni * r * r2_ni * s2) % (p - 1)
y = pow(g, x, p)
t1 = pow(y, m, p)
t2 = (pow(r, s) * pow(g, r)) % p
if t1 == t2:
    print(t1, '=', t2)
    print("签名有效")
else:
    print(t1, '!=', t2)
    print("签名无效")
print("素数p =", p)
print("模p本元g =", g)
print("明文m =", m)
print("私钥x =", x)
print("公钥y =", y)
print("随机数h =", h)
print("β =", b)
print("随机数k =", k)
print("r′ =", r2)
print("随机数α =", a)
print("r =", r)
print("m′ =", m2)
print("s′ =", s2)
print("s =", s)

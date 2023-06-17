import random
import math


def is_prime(x):  # 检测是否为素数
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def encry(x, p, n):  # RSA加密
    c = pow(x, p, n)
    return c


def decry(y, q, n):  # RSA解密
    m = pow(y, q, n)
    return m


N = 10
i = int(input("A的财富（1-9）百万："))
j = int(input("B的财富（1-9）百万："))
print("采用RSA加密算法")
pb = int(input("B的公钥："))
sb = int(input("B的私钥："))
n = int(input("n="))
y = []
while True:
    x = random.randint(10, 100)
    if is_prime(x):
        break
print("随机整数x =", x)
c = decry(x, pb, n)
c = c - i
print("A发送给B { c-i =", c, "}")
for u in range(N):
    t = decry(c + u + 1, sb, n)
    y.append(t)
p = int(input("选取大素数p="))
for s in range(N):
    y[s] %= p
t2 = j
while t2 < N:
    y[t2] += 1
    t2 += 1
print("B发送给A {", y, ",",p, "}")
if y[i - 1] == x:
    print("B的财富大于等于A")
else:
    print("A的财富大于B")

# python实现RSA加密
import gmpy2
import random
import math
from Crypto.Util.number import *


def randchose_e(phi):
    while True:
        e = random.randint(2, phi-1)
        if math.gcd(e, phi) == 1:
            break
    print("公钥e:", e)
    return e


# p, q 是两个大质数
p = 61
q = 53
# n 是RSA模数
n = p*q
# 求欧拉函数 φ(n)
phi = (p-1)*(q-1)

# 随机生成的公钥e
e = randchose_e(phi)
# 用扩展的欧几里得算法计算 e 对于 φ(n) 的模逆元 d
d = gmpy2.invert(e, phi)
# 计算明文 m 的 RSA 加密结果
m = bytes_to_long(b'hello world')
c = pow(m, e, n)

print("公钥 (n, e):", (n, e))
print("私钥 (n, d):", (n, d))
print("加密后的密文：", c)

# 解密
m_decr = pow(c, d, n)
print("解密后的明文：", long_to_bytes(m_decr))

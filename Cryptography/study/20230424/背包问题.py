import numpy as np
import random


# 计算模反元素
def modular_inverse(u, p):
    for v in range(1, p):
        if (u * v) % p == 1:
            return v
    return None


# 加密
def encrypt(message, public_key):
    return sum([message[i] * public_key[i] for i in range(len(message))])


# 解密
def decrypt(ciphertext, private_key, u, p):
    # 计算模反元素
    v = modular_inverse(u, p)
    w = (ciphertext * v) % p
    decrypted = [0] * len(private_key)
    # Knapsack 问题解法
    for i in range(len(private_key) - 1, -1, -1):
        if w >= private_key[i]:
            decrypted[i] = 1
            w -= private_key[i]
    return decrypted


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# 设置私钥、质数、公钥
private_key_b = np.array([1, 3, 7, 13, 26, 65, 119, 267])
p = sum(private_key_b) + 1
while not np.all(np.array([p % i for i in range(2, int(np.sqrt(p))+1)]) != 0):
    p += 1
u = random.randint(1, p-1)
while not is_prime(u):
    u = random.randint(1, p-1)

v = modular_inverse(u, p)
s = f"u = {u}, v = {v}, p = {p}"
public_key_a = np.array([u * x % p for x in private_key_b])
print(s)
print("public_key_a:", public_key_a)

# 待加密信息
message_m = np.array([1, 0, 1, 0, 1, 1, 0, 0])

# 加密
ciphertext = encrypt(message_m, public_key_a)
print("Ciphertext:", ciphertext)

# 解密
decrypted_message = np.array(decrypt(ciphertext, private_key_b, u, p))
print("Decrypted message:", decrypted_message)

def ElGamal_encrypt(p, g, a, m):
    """
    ElGamal 加密
    p: 大素数
    g: 生成元
    a: 私钥
    m: 明文
    """
    # 公钥 b
    b = pow(g, a, p)
    # 随机选择 k
    import random
    k = random.randint(1, p-2)
    # 密文
    c1 = pow(g, k, p)
    c2 = (pow(b, k, p) * m) % p
    return c1, c2


def ElGamal_decrypt(p, a, c1, c2):
    """
    ElGamal 解密
    p: 大素数
    a: 私钥
    c1, c2: 密文
    """
    # 明文
    m = (c2 * pow(c1, p-1-a, p)) % p
    return m


def baby_step_giant_step(p, g, b):
    """
    大步小步法求离散对数
    p: 大素数
    g: 生成元
    b: 公钥
    """
    import math
    m = math.ceil(math.sqrt(p - 1))

    # Baby-step.
    baby_steps = {pow(g, j, p): j for j in range(m)}

    # Giant-step.
    g_inv_m = pow(g, m * (p - 2), p)  # g^(-m)
    giant_step = b
    for i in range(m):
        if giant_step in baby_steps:
            return i * m + baby_steps[giant_step]
        else:
            giant_step = giant_step * g_inv_m % p

    return None  # 如果没有找到结果


# 加密 "HelloWorld"
p = 659
g = 163
a = 51
plaintext = "HelloWorld"
ciphertext_given = [(288, 510), (180, 724), (767, 75), (499, 785), (247, 764), (757, 40), (772, 39), (118, 561), (212, 769), (153, 391)]

ciphertext = []
for ch in plaintext:
    m = ord(ch)
    c = ElGamal_encrypt(p, g, a, m)
    ciphertext.append(c)

# 检查密文是否正确
if ciphertext == ciphertext_given:
    print("Ciphertext is correct!")
    plaintext_decrypted = ""
    for c in ciphertext:
        m = ElGamal_decrypt(p, a, *c)
        plaintext_decrypted += chr(m)
    print("Decrypted plaintext:", plaintext_decrypted)
else:
    print("Ciphertext is incorrect!")
    print("Correct ciphertext:", ciphertext)

# 寻找私钥
p = 65867
g = 15012
b = 48541
a = baby_step_giant_step(p, g, b)
print("Private key:", a)

# 给定的参数
p = 691
g = 29
a = 259
ciphertext = [(46, 236), (567, 244), (123, 390), (619, 11), (608, 237), (464, 19), (393, 682), (112, 512), (601, 237), (536, 146)]

# 加密
my_id = "32116160247"
ciphertext_new = []
for ch in my_id:
    m = ord(ch)
    import random
    r = random.randint(1, p-2)
    c = ElGamal_encrypt(p, g, r, m)
    ciphertext_new.append(c)
print("Encrypted ID:", ciphertext_new)

# 解密
plaintext_decrypted = ""
for c in ciphertext:
    m = ElGamal_decrypt(p, a, *c)
    plaintext_decrypted += chr(m)
print("Decrypted plaintext:", plaintext_decrypted)

# 导入必要的库

# 已知参数
p = 1553  # 素数 p
g = 3  # 模 p 的原根 g
m = 541  # 明文 m
x = 423  # 私钥 x
y = 1304  # 公钥 y
h = 121  # 随机数 h
k = 133  # 随机数 k
a = 599  # 随机数 a

# Alice 随机选取 h，计算 B，然后发送给 Bob
B = pow(g, h, p)

# Bob 随机选取 k，计算 r，然后发送给 Alice
r_prime = pow(B, k, p)

# Alice 计算 r，然后计算 m'
r = pow(r_prime, a, p)
m_prime = m * pow(r, -1, p - 1) % (p - 1)

# Bob 根据 m' 计算 s'
s_prime = pow(k, -1, p - 1) * (m_prime * x - r_prime) % (p - 1)

# Alice 根据 s' 计算 s
s = pow(a, -1, p - 1) * pow(h, -1, p - 1) * s_prime % (p - 1)

# 验证签名是否有效
is_valid = pow(g, s, p) == pow(y, m, p) * pow(r_prime, s, p) % p
print('签名有效' if is_valid else '签名无效')

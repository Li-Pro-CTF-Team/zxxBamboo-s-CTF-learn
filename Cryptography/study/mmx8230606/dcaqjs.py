import random


def check_inputs(S, p, x, k):
    """
    检查输入是否满足Shamir秘密共享方案的条件。
    S: 秘密
    p: 一个素数
    x: 私钥列表
    k: 重构秘密所需的最小共享数量
    """
    if not isinstance(S, int) or not isinstance(p, int) or not isinstance(k, int):
        return False
    if not all(isinstance(xi, int) for xi in x):
        return False
    if S >= p or any(xi >= p for xi in x):
        return False
    if k > len(x):
        return False
    return True


def shamir_share(S, p, x, k):
    """
    S: 秘密
    p: 一个素数
    x: 私钥列表
    k: 重构秘密所需的最小共享数量
    """
    # 检查输入的有效性
    if not check_inputs(S, p, x, k):
        raise ValueError("无效的输入。")

    # 随机生成系数 S1 和 S2
    S1 = random.randint(1, p-1)
    S2 = random.randint(1, p-1)

    # 计算公钥
    y = [(S + S1*xi + S2*xi**2) % p for xi in x]

    return y, S1, S2


def lagrange_interpolation(x, y, p):
    """
    x: x坐标列表
    y: y坐标列表
    p: 一个素数
    """
    n = len(x)
    total = 0
    for i in range(n):
        xi, yi = x[i], y[i]
        prod = 1
        for j in range(n):
            if i != j:
                xj = x[j]
                prod = (prod * (0 - xj) * pow(xi - xj, p-2, p)) % p
        total = (total + yi*prod) % p
    return total


def shamir_reconstruct(y, x, p, k):
    """
    y: 公钥列表
    x: 与公钥对应的私钥列表
    p: 一个素数
    k: 重构秘密所需的最小共享数量
    """
    # 随机选择 k 个共享
    shares = random.sample(list(zip(y, x)), k)
    # 使用Lagrange插值求解秘密 S
    x_coords, y_coords = zip(*shares)
    secret = lagrange_interpolation(x_coords, y_coords, p) 
    return secret


# 参数
S = 54321
p = 727
x = [628, 635, 55, 295, 502, 683, 105]
k = 4

# 生成共享
y, S1, S2 = shamir_share(S, p, x, k)
print("公钥列表:", y)

# 两次重构秘密
secret1 = shamir_reconstruct(y, x, p, k)
print("重构的秘密（第一次）:", secret1)

secret2 = shamir_reconstruct(y, x, p, k)
print("重构的秘密（第二次）:", secret2)

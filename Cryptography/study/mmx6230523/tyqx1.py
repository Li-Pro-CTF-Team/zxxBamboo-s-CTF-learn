import random


def get_ng(x, y, n, a, p):
    for _ in range(n):
        lam = ((3 * x * x + a) * pow(2 * y, p - 2, p)) % p
        x = (lam ** 2 - 2 * x) % p
        y = (lam * (x - x) - y) % p
    return x, y


def map_plain_text_to_point(plain_text, P_x, P_y, a, p):
    mapping_point = []
    print("明文映射的点为: ", end="")
    for char in plain_text:
        intchar = ord(char)
        mapping_k = intchar + 1
        (G_x, G_y) = P_x, P_y
        (k_G_x, k_G_y) = get_ng(G_x, G_y, mapping_k, a, p)
        mapping_point.append([k_G_x, k_G_y])
        print(f"{char}=>({k_G_x},{k_G_y})", end="---")
    print()
    return mapping_point


def encrypt(mapping_point, P_x, P_y, a, p, d):
    c1, c2 = [], []
    for point in mapping_point:
        k = random.randint(1, 127)
        kP_x, kP_y = get_ng(P_x, P_y, k, a, p)
        kG_x, kG_y = get_ng(P_x, P_y, k * d, a, p)
        c1.append([kP_x, kP_y])
        c2.append([kG_x + point[0], kG_y + point[1]])
    return c1, c2


def decrypt(c1, c2, P_x, P_y, a, p, d):
    plain_text = ''
    print("解密得到明文映射的点: ", end="")
    for i in range(len(c1)):
        kP_x, kP_y = get_ng(c1[i][0], c1[i][1], d, a, p)
        mapping_x, mapping_y = c2[i][0] - kP_x, c2[i][1] - kP_y
        for j in range(128):
            point_x, point_y = get_ng(P_x, P_y, j, a, p)
            if point_x == mapping_x and point_y == mapping_y:
                plain_text += chr(j - 1)
                print(f"({mapping_x},{mapping_y})", end="---")
                break
    print()
    return plain_text


a = int(input("请输入椭圆曲线参数a(a>0)的值:"))
b = int(input("请输入椭圆曲线参数b(b>e)的值:"))
p = int(input("请输入圆曲线参数p(p为素数)的值:"))
P_x = int(input("请输入选取的x坐标值:"))
P_y = int(input("请输入选取的y坐标值:"))
d = int(input("请输入用于生成公钥的私钥 d (<129) :"))
Q_x, Q_y = get_ng(P_x, P_y, d, a, p)
print(f"user1:计算Q = dP得公钥Q为: ({Q_x},{Q_y})")

plain_text = input("请输入需要加密的字符串:")
mapping_point = map_plain_text_to_point(plain_text, P_x, P_y, a, p)

k = int(input("请输入秘密选择的k (<129) :"))
c1, c2 = encrypt(mapping_point, P_x, P_y, a, p, d)
print(f"user2:计算得密文为: c1: {c1}\nc2: {c2}")

plain_text = decrypt(c1, c2, P_x, P_y, a, p, d)
print("user1解密得到明文: ", plain_text)

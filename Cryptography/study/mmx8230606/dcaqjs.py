import random


def get_inverse(value, p):  # 求逆
    for i in range(1, p):
        if (i * value) % p == 1:
            return i
    return -1


s = 321
n = 7
t = 4
x = [628, 635, 55, 295, 502, 683, 105]
p = 727
sm = []
y = []
for i in range(t - 1):
    si = random.randint(1, p)
    sm.append(si)
for i in range(n):  # 求yi
    tmp = 1
    yi = s
    for j in range(t - 1):
        yi = (yi + sm[j] * pow(x[i], tmp, p)) % p
        tmp += 1
    y.append(yi)
print("x:", x)
print("y:", y)
peo = []
for i in range(n):
    peo.append([x[i], y[i]])
# 秘密恢复
for i in range(2):
    a = random.sample(peo, t)
    print("随机选取", t, "个人", a)
    st = 0
    for k in range(t):
        t1 = 1
        for j in range(t):
            if j != k:
                t2 = get_inverse(a[k][0] - a[j][0], p)
                t1 = (t1 * (p - a[j][0]) * t2) % p
        st += a[k][1] * t1
    st = st % p
print("秘密S =", st)

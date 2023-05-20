import gmpy2

# 设置公钥指数
e = 3

# 从文件读取密文和模
with open('c.txt', 'r') as f:
    c = int(f.read())
with open('n.txt', 'r') as f:
    n = int(f.read())

# 检查是否满足小指数攻击的条件
if gmpy2.iroot(c, e)[1]:
    # 计算密文的e次方根
    m = gmpy2.iroot(c, e)[0]

    # 将解密后的消息从整数转换为字符串
    decrypted_m = (int(m).to_bytes((int(m).bit_length() + 7) // 8, 'big')).decode()

    # 打印解密后的消息
    print("Decrypted message: ", decrypted_m)
else:
    print('The cipher text does not meet the conditions for a small exponent attack.')

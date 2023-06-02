from gmssl import sm2, func


# 初始化椭圆曲线参数
sm2_crypt = sm2.CryptSM2(
    public_key=EllipseG,
    private_key=None
)
sm2_crypt.set_curve_params(Ellipse_a, Ellipse_b, EllipseG, EllipseN, EllipseP, Fp)

# 生成SM2密钥对
keypair = sm2_crypt.gen_key_pair()

# 使用公钥加密字符串
msg = 'hElloworld'
ciphertext = sm2_crypt.encrypt(msg, keypair.get('public_key'))

# 使用私钥解密加密后的字符串
plaintext = sm2_crypt.decrypt(ciphertext, keypair.get('private_key'))

# 打印结果
print("原文: ", msg)
print("密文: ", ciphertext)
print("解密后: ", plaintext)

from gmssl import sm2, sm3, func


# 首先定义参数
ID = b'1234567812345678'  # ID用于SM3
msg = b'helloworld'  # 需要加密的消息
msg = sm3.sm3_hash(func.bytes_to_list(msg))  # 使用SM3进行哈希
ellipseN = int('8542D69E4C044F18E8B92435BF6FF7DD297720630485628D5AE74EE7C32E79B7', 16)  # g的阶
ellipseP = int('8542D69E4C044F18E8B92435BF6FF7DE457283915C45517D722EDB8B08F1DFC3', 16)
ellipseG = '421DEBD61B62EAB6746434EBC3CC315E32220B3BADD50BDC4C4E6C147FEDD43D0680512BCBB42C07D47349D2153B70C4E5D7FDFCBFA36EA1A85841B9E46E09A2'
ellipse_a = int('787968B4FA32C3FD2417842E73BBFEFF2F3C848B6831D7E0EC65228B3937E498', 16)
ellipse_b = int('63E4C6D3B23B0C849CF84241484BFE48F61D59A5B16BA06E6E12D1DA27C5249A', 16)
ellipse_a_3 = (ellipse_a + 3) % ellipseP  # 倍点用到的中间值
Fp = 256
# 然后生成SM2的密钥对
# 创建一个SM2对象
sm2_crypt = sm2.CryptSM2(public_key=ellipseG, private_key=ellipseN)

# 生成密钥对
private_key, public_key = sm2_crypt.gen_key_pair()

# 使用公钥进行加密
crypt_sm2 = sm2.CryptSM2(public_key=public_key, private_key=private_key)
cipher_text = crypt_sm2.encrypt(msg)

# 使用私钥进行解密
decrypt_text = crypt_sm2.decrypt(cipher_text)

# 打印加密后的消息和解密后的消息
print("Cipher text: ", cipher_text)
print("Decrypt text: ", decrypt_text)

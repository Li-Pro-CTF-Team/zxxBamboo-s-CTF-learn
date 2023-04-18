# 用python逆加密：用维吉尼亚密码加密明文“please keep this message in secret.”
# ,其中使用的密钥为“computer”,试求其密文。

def vigenere_cipher(text, key, encrypt=True):
    text = text.lower()
    key = key.lower()   # 使用 lower() 方法将明文转换为小写，并对密钥执行相同操作。
    key_length = len(key)
    key_as_int = [ord(i) - ord('a') for i in key]  # 整数列表，密钥中每个字符的移位值
    result = []  # 初始化结果列表为空列表。
    # for 循环用于遍历文本字符串中的每个字符。
    # enumerate() 函数用于跟踪每个字符的索引。
    for i, c in enumerate(text):
        if c.isalpha():
            shift = key_as_int[i % key_length]  # 如果字符是字母，则通过将模运算符 (%) 与 key_length 变量一起使用，从 key_as_int 列表中获取移位值。 如果 encrypt 为 False，则移位值取反。
            if not encrypt:
                shift = -shift
            new_c = chr(((ord(c) - ord('a') + shift) % 26) + ord('a'))
            result.append(new_c)  # 新字符是通过将移位值与原始字符的 ASCII 值相加，减去小写字母 'a' 的 ASCII 值，将结果取模 26 并在必要时环绕到字母表的开头，然后 添加字母“a”的 ASCII 值。 此计算是使用 ord() 和 chr() 函数执行的。
        else:
            result.append(c)  # 如果字符不是字母，则按原样附加到结果列表。
    return ''.join(result)  # 使用 join() 方法将结果列表转换为字符串，并作为密文返回


plaintext = "ATTACKATDAWN"  # 将要加密的明文消息分配给可变文本。
key = "LEMONLEMONLE"  # 用于加密的密钥被分配给变量密钥。
ciphertext = vigenere_cipher(plaintext, key)  # 密文被分配给密文变量。
print("Ciphertext:", ciphertext.upper())  # 使用 print() 函数将密文打印到控制台。

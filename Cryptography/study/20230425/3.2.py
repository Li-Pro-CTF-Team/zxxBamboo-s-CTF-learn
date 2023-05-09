# 导入NumPy库
import numpy as np


# 定义一个函数find_coefficients，接受明文plaintext、密文ciphertext和初始状态initial_state作为参数
def find_coefficients(plaintext, ciphertext, initial_state):
    # 将初始状态赋值给状态变量state，并获取状态长度n
    state = initial_state
    # n = len(initial_state)
    # 初始化两个空的列表，用于存储矩阵A和向量B的元素
    A = []
    B = []
    # 遍历明文和密文的每个字符，生成矩阵A和向量B
    for p, c in zip(plaintext, ciphertext):
        # 将当前状态添加到矩阵A的末尾
        A.append(state)
        # 将密文和明文的异或结果添加到向量B中
        B.append(c ^ p)
        # 更新状态，将当前明文添加到状态序列的末尾，并删除状态序列的第一个元素
        state = state[1:] + [p]
    # 将列表A和B转换为NumPy数组
    A = np.array(A)
    B = np.array(B)
    coefficients, _, _, _ = np.linalg.lstsq(A, B, rcond=None)
    return coefficients.round().astype(int)


# 定义初始状态、明文和密文
initial_state = [1, 0, 0]
plaintext = [0, 1, 0, 0, 0, 1]
ciphertext = [1, 0, 0, 1, 0, 1]

# 调用函数find_coefficients，破解LFSR的系数并打印结果
coefficients = find_coefficients(plaintext, ciphertext, initial_state)
print("线性移位寄存器的系数:", coefficients)

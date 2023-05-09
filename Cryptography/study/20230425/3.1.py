# 定义一个函数lfsr，接受初始状态initial_state和迭代轮数rounds作为参数
def lfsr(initial_state, rounds):
    # 将初始状态赋值给状态变量state
    state = initial_state
    # 初始化一个空的列表，用于存储输出序列
    output = []
    # 迭代轮数次，生成LFSR序列
    for _ in range(rounds):
        # 计算反馈位，即第0位和第3位异或的结果
        feedback = state[0] ^ state[3]
        # 将反馈位添加到状态序列的末尾，并删除状态序列的第一个元素
        state = state[1:] + [feedback]
        # 将反馈位添加到输出序列中
        output.append(feedback)
    # 返回输出序列和最终状态序列
    return output, state


# 定义一个函数find_cycle，接受初始状态initial_state作为参数
def find_cycle(initial_state):
    # 将初始状态赋值给状态变量state
    state = initial_state
    # 初始化周期长度为0
    cycle = 0
    # 循环计算LFSR序列，直到状态序列与初始状态序列相等
    while True:
        # 计算反馈位，即第0位和第3位异或的结果
        feedback = state[0] ^ state[3]
        # 将反馈位添加到状态序列的末尾，并删除状态序列的第一个元素
        state = state[1:] + [feedback]
        # 增加周期长度
        cycle += 1
        # 如果状态序列与初始状态序列相等，退出循环
        if state == initial_state:
            break
    # 返回周期长度
    return cycle


# 定义初始状态和迭代轮数
initial_state = [1, 0, 0, 1]
rounds = 20

# 调用函数lfsr，生成LFSR序列并打印输出序列和最终状态序列
output, final_state = lfsr(initial_state, rounds)
print("输出序列:", output)
print("状态序列:", final_state)

# 调用函数find_cycle，计算LFSR序列的周期长度并打印结果
cycle_length = find_cycle(initial_state)
print("周期长度:", cycle_length)

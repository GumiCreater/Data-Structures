import random


def temp_creat(n):  # 生成1到100的随机数
    temp = list()
    i = 1
    while i <= n:
        temp.append(random.randint(1,100))
        i += 1
    print("原列表:",temp)
    return temp
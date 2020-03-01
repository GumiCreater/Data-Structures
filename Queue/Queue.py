class Queue():
    def __init__(self):
        self.q = list()

    def enqueue(self,s):  # 入列
        self.q.insert(0,s)

    def dequeue(self):  # 出列
        return self.q.pop()

    def isEmpty(self):  # 判断是否为空
        return self.q == []

    def size(self):  # 计算队列中的元素
        return len(self.q)
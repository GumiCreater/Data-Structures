"""此算法是将‘土豆’传递某个次数后，拥有‘土豆’的成员退出，循环至得到最后一个成员"""
from Queue import Queue


def Filter(s,num):  # s是成员名字列表，num是传递次数
    q = Queue()
    for i in s:  # 将所有成员按顺序入列
        q.enqueue(i)
    while q.size() > 1:  # 循环直至只剩一个人
        count = 0  # 每次重置传递土豆次数
        while count <= num:
            q.enqueue(q.dequeue())  # 队首出列后到队尾算是将土豆传递给下一个人
            count += 1
        q.dequeue()  # 传递一个次数后 队首的人算为“持有土豆” 则退出
    return q.dequeue()


def main():
    s = "qertyui"
    num = 5  # input
    last = Filter(s,num)
    print(last)


if __name__ == "__main__":
    main()
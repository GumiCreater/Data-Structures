"""二叉堆————一个用列表实现的完全二叉树，并且子树的根的数值一定小于父结点，每个子树也是二叉堆，可用来进行堆排序"""


class BinHeap():
    def __init__(self):  # heaplist存储所有数据 因为数据从1开始 所有下标为0的数据设为0
        self.heapList = [0]
        self.listSize = 0  # 列表存储的数据个数

    def percUp(self, i):  # 上浮函数————第i个结点与父结点比较大小，较大则交换位置
        exchange = True
        while i // 2 > 0 and exchange:  # i整除2为父结点的序号
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            else:
                exchange = False
            i //= 2

    def insert(self, data):  # 插入函数 先将要插入的数据放在最后，再将此结点调用上浮函数，直至不再交换位置
        self.heapList.append(data)
        self.listSize += 1
        self.percUp(self.listSize)

    def minChild(self, i):  # 返回第i个结点最小的孩子的序号
        if i * 2 + 1 > self.listSize:
            return i * 2
        else:
            if self.heapList[i * 2] > self.heapList[i * 2 + 1]:
                return i * 2 + 1
            else:
                return i * 2

    def percDown(self, i):  # 下沉函数————和上浮类似，通过和孩子比较大小，不断交换位置直至孩子结点大于自己
        exchange = True
        while (i * 2) <= self.listSize and exchange:
            j = self.minChild(i)
            if self.heapList[i] > self.heapList[j]:
                self.heapList[i], self.heapList[j] = self.heapList[j], self.heapList[i]
            else:
                exchange = False
            i = j

    def delMin(self):  # 删除并返回堆顶的数据，即是此数据结构中最小的数据
        retVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.listSize]  # 将最后一个数放在堆顶，再用此数调用下沉函数移到合适的位置
        self.heapList.pop()
        self.listSize -= 1
        self.percDown(1)
        return retVal

    def buildHeap(self, List):  # 生成函数，传入无序的列表，生成一个二叉堆
        i  = len(List) // 2
        self.heapList.extend(List)
        self.listSize = len(List)
        while i > 0:
            self.percDown(i)  # 由下至上 对倒数第二层开始每个结点调用一次下沉函数
            i -= 1
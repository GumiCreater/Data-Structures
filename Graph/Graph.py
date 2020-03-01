from Queue import Queue


'''图数据结构的实现，包含邻接表和邻接矩阵两种表示方式'''
class Vertex():  # 顶点类 存放结点的值 和结点的所有邻点信息
    def __init__(self, key):
        self.key = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight):  # 插入一个结点 weight为权重
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.key) + 'connected to' + str(x.key for x in self.connectedTo)

    def getConnections(self):
        return self.connectedTo.keys()

    def getKey(self):
        return self.key

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class SparseGraph():  # 用邻接表表示图 一般存放边稀疏的图,有每个结点信息和定点数
    def __init__(self, directed):
        self.verList = {}
        self.verNum = 0
        self.directed = directed  # directed为True则为有向图 False则为无向图

    def addVertice(self, key):  # 给图添加结点
        self.verNum += 1
        newVer = Vertex(key)
        self.verList[key] = newVer

    def getVertice(self, key):  # 获取某个结点
        if key in self.verList:
            return self.verList[key]
        else:
            return None

    def __contains__(self, key):  # 可以使用成员操作符
        return key in self.verList

    def addEdge(self, ver1, ver2, weight):  # 给两个结点添加一条边
        if ver1 not in self.verList:  # 若无此结点 则先添加到图中
            self.addVertice(ver1)
        if ver2 not in self.verList:
            self.addVertice(ver2)
        self.verList[ver1].addNeighbor(ver2, weight)
        if not self.directed:  # 若是无向图,则直接在另一个结点添加同一个边
            self.verList[ver2].addNeighbor(ver1, weight)

    def wideTraversal(self):
        isTraverlled = []  # 用来存储某个结点遍历到与否
        for i in range(self.verNum):  # 初始全部设置为False
            isTraverlled.append(False)
        q = Queue()
        for ver in self.verList:  # 若没有联通则从下一个
            self.wideTraversalHelper(int(ver), isTraverlled, q)

    def wideTraversalHelper(self, key, isTraverlled, q):
        if isTraverlled[key] == False:
            print(key)
            q.enqueue(key)
            isTraverlled[key] = True
        for i in self.verList[str(key)].connectedTo:
            i = int(i)  # 67-71将所有未输出过的相邻结点输出并且入队列
            if isTraverlled[i] == False:
                print(i)
                q.enqueue(i)
                isTraverlled[i] = True
        if not q.isEmpty():  # 输出完所有相邻结点后 对相邻结点进行广度优先遍历
            self.wideTraversalHelper(q.dequeue(), isTraverlled, q)

    def deepTraversal(self):  # 深度优先遍历方法 以连通分量数为返回值
        isTraverlled = []  # 用来存储某个结点遍历到与否
        count = 0
        for i in range(self.verNum):  # 初始全部设置为False
            isTraverlled.append(False)
        for ver in self.verList:
            ver = int(ver)
            if isTraverlled[ver] == False:
                self.deepTraversalHelp(ver, isTraverlled)  # 递归函数实现深度遍历,若结束一轮递归
                count += 1                                 # 说明一个联通分量被遍历完成 连通分量数加一
        return count

    def deepTraversalHelp(self, key, isTraverlled):
        if isTraverlled[key] == False:
            print(key)
            isTraverlled[key] = True
            for i in self.verList[str(key)].connectedTo:
                i = int(i)
                self.deepTraversalHelp(i, isTraverlled)  # 按连接顺序 对下一邻接点进行深度遍历
            

class DenseGraph():  # 用邻接矩阵表示图 (v1, v2) 的元素为True则说明v1有一条指向v2的边
    def __init__(self, n, directed):  # 属性有结点数,边数和判断有无向的布尔型 和字典实现的邻接矩阵
        self.verNum = n
        self.edgeNum = 0
        self.directed = directed
        self.matrix = {}
        for i in range(1, n + 1):  # 初始全部设为False
            self.matrix[i] = list(0)
            for j in range(1, n + 1):
                self.matrix[i].append(False)

    def addEdge(self, v1, v2):
        if v1 not in range(1, self.verNum + 1) or v2 not in range(1, self.verNum + 1):  # 判断是否越界
            raise ValueError('Value is out of range')
        else:
            if not self.hasEdge(v1, v2):
                return
            self.matrix[v1][v2] = True
            self.edgeNum += 1
            if not self.directed:
                self.matrix[v2][v1] = True

    def hasEdge(self, v1, v2):
        if v1 not in range(1, self.verNum + 1) or v2 not in range(1, self.verNum + 1):
            raise ValueError('Value is out of range')
        else:
            return self.matrix[v1][v2]
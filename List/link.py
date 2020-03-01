"""链表的实现"""


class UnorderHead():  # 链表头
    def __init__(self):
        self.head = None


class Node():  # 结点
    def __init__(self):
        self.data = 0
        self.next = None

    def setData(self, Newnum):
        self.data = Newnum

    def setNext(self, Newnext):
        self.next = Newnext

    def getData(self):
        return self.data

    def getNext(self):
        return self.next


class linklist():  # 链表
    def __init__(self):
        self.Head = UnorderHead()
        
    def add(self, num, *order):  # 插入方法，不传入序号则加在链表末尾，若传入则加在序号结点后面
        NewNode = Node()
        NewNode.setData(num)
        if self.Head.head == None:  # 若链表为空则直接将结点放在表头
            self.Head.head = NewNode
        else:
            temp = self.Head.head
            if order == ():  # 若没有指定将数据插到第几位则默认加到链表末尾
                while temp.getNext() != None:  # 遍历到尾端
                    temp = temp.getNext()
                temp.next = NewNode
            else:
                count = 1
                while count < order[0] - 1:  # 遍历到指定序号的前一个结点
                    temp = temp.getNext()
                    count += 1
                NewNode.setNext(temp.getNext())
                temp.setNext(NewNode)

    def remove(self, item):  # 删除指定元素的结点
        order = self.search(item)
        temp = self.Head.head
        if order == self.size():
            while temp.getNext() != None:
                previous = temp  # 用一个变量记录要删除的结点的前一个结点
                temp = temp.getNext()
            previous.setNext(None)  # 将前一个结点的Next设为None即为删除后一个结点
        else:
            count = 1
            while count < order -1:
                temp = temp.getNext()
                count += 1
            later = temp.getNext().getNext()
            temp.setNext(later)  # 将前一个结点的Next设为要删除的结点的后一个结点

    def travel(self):  # 遍历输出链表所有元素
        temp = self.Head.head
        while temp != None:
            print(temp.getData())
            temp = temp.getNext()

    def search(self, item):  # 通过遍历查询指定元素所在的结点位置
        temp = self.Head.head
        order = 1
        while temp != None:
            if temp.getData() == item:
                return order
            temp = temp.getNext()
            order += 1

    def size(self):  # 通过遍历查询链表长度
        if self.Head.head == None:
            return 0
        else:
            count = 1
            temp = self.Head.head
            while temp.getNext() != None:
                temp = temp.getNext()
                count += 1
            return count

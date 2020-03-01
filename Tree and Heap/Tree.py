class BinaryTree():
    def __init__(self, NewData):  # 构造函数 设定根的数据
        self.data = NewData
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, data):
        if self.leftChild == None:  # 左子树为空 直接新构造一个结点存入
            self.leftChild = BinaryTree(data)
        else:
            t = BinaryTree(data)  # 非空 则将原左子树放入新结点的左子树中 新节点作为新的左子树的根
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, data):  # 插入到右子树
        if self.rightChild == None:
            self.rightChild = BinaryTree(data)
        else:
            t = BinaryTree(data)
            t.rightChild = self.rightChild
            self.rightChild = t

    def setRootVal(self, NewData):  # 设置根的数据
        self.data = NewData

    def getRootVal(self):  # 获取根的数据
        return self.data

    def getLeftChild(self):  # 获得左子树的根
        return self.leftChild

    def getRightChild(self):  # 获得右子树的根
        return self.rightChild

    def preTraversal(self):  # 先序遍历
        print(self.getRootVal())
        if self.leftChild:
            self.leftChild.preTraversal()
        if self.rightChild:
            self.rightChild.preTraversal()
    
    def inTraversal(self):  # 中序遍历
        if self.leftChild:
            self.leftChild.inTraversal()
        print(self.getRootVal())
        if self.rightChild:
            self.rightChild.inTraversal()

    def postTraversal(self):  # 后序遍历
        if self.leftChild:
            self.leftChild.postTraversal()
        if self.rightChild:
            self.rightChild.postTraversal()
        print(self.getRootVal())


# def preTraversal(Tree): # 前序遍历
#         if Tree:
#             print(Tree.getRootVal())
#             preTraversal(Tree.getLeftChild())
#             preTraversal(Tree.getRightChild())


# def inTraversal(Tree): # 中序遍历
#         if Tree:
#             inTraversal(Tree.getLeftChild())
#             print(Tree.getRootVal())
#             inTraversal(Tree.getRightChild())


# def postTraversal(Tree): # 后序遍历
#         if Tree:
#             postTraversal(Tree.getLeftChild())
#             postTraversal(Tree.getRightChild())
#             print(Tree.getRootVal())
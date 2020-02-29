from Graph import Vertex, SparseGraph


def main():
    g1 = SparseGraph(False)  # 第一个测试用例
    f = open("temp1.txt", "r")
    s = f.read(4)
    while s:
        g1.addEdge(s[0], s[2], 1)
        s = f.read(4)
    print("广度优先遍历")
    g1.wideTraversal()
    print("-------")
    print("深度优先遍历")
    print("连通分量有%d个" % g1.deepTraversal())
    g2 = SparseGraph(False)  # 第二个测试用例
    f = open("temp2.txt", "r")
    s = f.read(4)
    while s:
        g2.addEdge(s[0], s[2], 1)
        s = f.read(4)
    print("广度优先遍历")
    g2.wideTraversal()
    print("------")
    print("深度优先遍历")
    print("连通分量有%d个" % g2.deepTraversal())


if __name__ == "__main__":
    main()
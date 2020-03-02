import random


def temp_creat(n):  # 生成1到100的随机数
    temp = list()
    i = 1
    while i <= n:
        temp.append(random.randint(1,100))
        i += 1
    print("原列表:",temp)
    return temp


def bubbleSort(List):  # 冒泡排序
    for i in range(len(List) - 1, 0, -1):
        for j in range(i):
            if List[j] > List[j+1]:  # 依次前后对比 较大的数换到后面
                List[j], List[j+1] = List[j+1], List[j]
    return List


def selectSort(List):  #选择排序
    for i in range(len(List) - 1, 1, -1):
        max_num = 0
        for j in range(1,i + 1):
            if List[j] > List[max_num]:  # 记录数列中最大的数所在位置，最后和最后一个数交换位置
                max_num = j
        List[max_num], List[i] = List[i], List[max_num]
    return List


def insertSort(List):  # 插入排序
    for i in range(1, len(List)):
        current = List[i]  # 用一个变量临时存放无序组第一个元素
        position = i
        while current < List[position - 1] and position > 0:  
            List[position] = List[position - 1]  # 有序组逐个元素后移直至找到合适的位置插入临时变量的值
            position -= 1
        List[position] = current
    return List


def gapInsertSort(List, start, gap):  # 带有固定间隔的插入排序,在希尔排序函数中被调用
    for i in range(start + gap, len(List), gap):
        current = List[i]
        position = i
        while current < List[position - gap] and position > 0:
            List[position] = List[position - gap]
            position -= gap
        List[position] = current
    return List


def shellSort(List):
    gap = len(List) // 2  # 间隔从列表长度的二分之一开始 逐步二分
    while gap > 0:
        for startposition in range(gap): #  每一轮有间隔的插入排序开始的位置都有gap个
            gapInsertSort(List, startposition, gap)
        gap //= 2
    return List


def mergeSort(List):
    if len(List) <= 1:  # 列表二分至只剩一个元素或没有元素为递归结束条件
        return List
    mid = len(List) // 2
    left = mergeSort(List[:mid])  # 将左右列表用归并法排序
    right = mergeSort(List[mid:])
    merged = []
    while left and right:  # 左右列表中选出小的进入合并好的列表
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)  # 最后将不空的列表直接并在最后
    return merged


def partition(List, first, last):  # 遍历整个列表，若小于第一个值则分裂点后移 并且此值和分裂点交换位置
    splitpoint = first             # 若大于 则不做任何操作
    for traveler in range(first + 1, last + 1):
        if List[traveler] <= List[first]:
            splitpoint += 1
            List[splitpoint], List[traveler] = List[traveler], List[splitpoint]
    List[splitpoint], List[first] = List[first], List[splitpoint]
    return splitpoint


def quickHelper(List, first, last):
    if first < last:
        splitpoint = partition(List, first, last)  # 此函数将列表以第一个元素为中心 分成两半
        quickHelper(List, first, splitpoint - 1)   # 前一半全部小于分裂点，后一半全部大于
        quickHelper(List, splitpoint + 1, last)  # 接着对左右两半继续做这个操作
    return List


def quickSort(List):  # 快速排序法
    return quickHelper(List, 0, len(List) - 1)  # 递归在此函数里实现


def main():
    temp = temp_creat(10)  # 随机生成一个长度为10的随机列表
    print("冒泡法排序:",bubbleSort(temp))
    print("选择法排序:",selectSort(temp))
    print("插入法排序:",insertSort(temp))
    print("希尔排序:",shellSort(temp))
    print("归并排序:",mergeSort(temp))
    print("快速排序:",quickSort(temp))


if __name__ == "__main__":
    main()
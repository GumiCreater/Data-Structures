
def BinarySearch(List, item):  # 二分法查找
    front = 0
    rear = len(List) - 1
    while front <= rear:
        mid = (front + rear) // 2
        if List[mid] == item:
            return mid + 1
        elif item < List[mid]:
            rear = mid - 1
        else:
            front = mid + 1
    return False


def main(): 
    temp = [1, 2, 3, 4, 6, 7, 8, 10]      
    order = BinarySearch(temp, 6)
    if order:
        print("6的所在位置为 %d" % order)
    else:
        print("列表中无此元素")


if __name__ == "__main__":
    main()
from Stack import Stack


'''用栈解决括号匹配问题'''
def patch(Str):
    s = Stack()
    for temp in Str:
        if temp == "(":  # 左括号入栈
            s.push(temp)
        elif s.isEmpty():  # 若为右括号且栈空 说明缺少左括号
            print("匹配失败")
            return 0
        else:
            s.pop()
    if s.isEmpty():  # 最后仍为空则是缺少右括号
        print("匹配成功")
    else:
        print("匹配失败")


def main():
    patch("((()))")
    patch("(()")
    patch("())")


if __name__ == "__main__":
    main()
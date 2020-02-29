from Stack import Stack


'''中缀表达式转换成后缀表达式'''
def switch(Str):
    prec = {}
    prec["*"] = 3  # 给运算符和括号设定优先级
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    s = Stack()
    Str_ed = []  # 存放后缀表达式的列表
    for temp in Str:
        if ord(temp) in range(97,122):  # 若字符是字母 则直接加进后缀表达式
            Str_ed.append(temp)
        elif temp == "(":  # 若为左括号 则入栈
            s.push(temp)
        elif temp == ")":
            while s.peek() != "(":  
                Str_ed.append(s.pop())
        else:
            while (not s.isEmpty()) and prec[s.peek()] >= prec[temp]:
                if s.peek() != "(":  # 每次入栈都需要输出栈中元素 直至栈顶元素优先级小于等于当前元素
                    Str_ed.append(s.pop())
                else:
                    s.pop()
            s.push(temp)
    while not s.isEmpty():  # 最后若栈不空 则全部输出到后缀表达式
        if s.peek() != "(":
            Str_ed.append(s.pop())
        else:
            s.pop()
    return Str_ed


def main():
    Str = "(a+b)*c"
    S = switch(Str)
    print(S)


if __name__ == "__main__":
    main()